import requests
import os
from dotenv import load_dotenv

load_dotenv()

trello_key = os.getenv('TRELLO_KEY')
trello_token = os.getenv('TRELLO_TOKEN')

board_id = '646a385223a6b8872384754a'

urlboard = f"https://api.trello.com/1/members/me/boards?fields=name,url&key={trello_key}&token={trello_token}"

response = requests.get(urlboard)

if response.status_code == 200:
    data = response.json()
    for board in data:
        board_name = board['name']
        board_url = board['url']
        board_id = board['id']
        print('---')
        print(f'Board Name: {board_name}')
        print(f'Board URL: {board_url}')
        print(f'Board ID: {board_id}')

        urllists = f"https://api.trello.com/1/boards/{board_id}/lists?key={trello_key}&token={trello_token}"
        response_lists = requests.get(urllists)
        if response_lists.status_code == 200:
            lists_data = response_lists.json()
            for trello_list in lists_data:
                list_name = trello_list['name']
                list_id = trello_list['id']
                print(f'List Name: {list_name}')
                print(f'List ID: {list_id}')


        else:
            print(f'Error occurred while fetching lists for board {board_id}.')
else:
    print('Error occurred while fetching boards.')
