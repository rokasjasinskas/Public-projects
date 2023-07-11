# run with two command lines. Need import sys and use sys.argv[1] and sys.argv[2]
# define each variable with name. first variable is email, secon name of API
# test email format, if it is correct. Do it be cheking if there is @ and dot
# test API name. Check if it is in list of apis use if AAAAAA in API_LIST. if not print message what it is wrong and sys.exit program.
# def API 1 call return value
# def API 2 call return value
# convert api value to human text. return text ready for email.
# send email via gmail acc.
#


# Imports:
import sys
import requests
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.message import EmailMessage
import time

load_dotenv()


def check_email(email_name):
    # check if it is not correct
    # if it is wrong:
    # print message and sys.exit
    # if correct exit function with True (?)

    while True:
        if "@" in email_name:
            username, domain = email_name.split("@")
            if "." in domain:
                return True

        print("You entered incorrect email name. Please run program once again")
        sys.exit(1)


def check_APINAME(api_name):
    # check if it is in list.
    # if yes - return name
    # if not - return false
    # try=except

    API_LIST = ["Trello", "Hunter", "AnimeFacts"]

    while api_name in API_LIST:
        return api_name
    else:
        print("You entered incorrect API name. Please run program once again")
        sys.exit(1)


def trello_API():
    trello_key = os.getenv("TRELLO_KEY")
    trello_token = os.getenv("TRELLO_TOKEN")

    urlboard = f"https://api.trello.com/1/members/me/boards?fields=name,url&key={trello_key}&token={trello_token}"

    response = requests.get(urlboard)

    if response.status_code == 200:
        data = response.json()
        email_values = [(board["name"], board["url"], board["id"]) for board in data]

        return email_values

    else:
        return None, None


def hunter_API():
    hunter_key = os.getenv("HUNTER_KEY")
    url = "https://api.hunter.io/v2/domain-search"
    domain = input("Enter domain which you was to test: ")
    company = input("Enter domain company name: ")

    params = {
        "domain": domain,
        "company": company,
        "api_key": hunter_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        emails = data["data"]["emails"]
        email_values = [email["value"] for email in emails]

        return email_values

    else:
        print(f"Request failed with status code {response.status_code}")


def animefacts_API():
    pass


def convert_text(email_values):
    # return email
    text = ""
    for item in email_values:
        if isinstance(item, tuple):
            text += "\n".join(item) + "\n\n"
        else:
            text += str(item) + "\n"

    human_text = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:

{text}

If you have any additional request, contact support.

Best regards,
Team
###########################################
        """
    return human_text


def gmail(email, email_name):
    pass_bp = os.getenv("APP_PASS_BP")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email_name
    print(f"Senders email is {email_name}")
    password = pass_bp

    receiver_email = input("Write receiver email address: ")

    check_email(receiver_email)

    subject = input("Subject: ")

    msg = EmailMessage()
    msg.set_content(email)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)


def main():
    try:
        length = len(sys.argv)
        if length < 4:
            email_name = sys.argv[1]
            api_name = sys.argv[2]
        else:
            print("Wrong input. Too many variables")
            sys.exit(1)

        time.sleep(1)

        try:
            check_email(email_name)
            api_name = check_APINAME(api_name)

            print(
                f"""
Hello user!

Thanks for using this program.

You will be able to use several APi services and receive answer to your email.

If you agree wait for net question.
                """
            )
            if check_APINAME(api_name) == "Trello":
                email_values = trello_API()
            elif check_APINAME(api_name) == "Hunter":
                email_values = hunter_API()
            elif check_APINAME(api_name) == "AnimeFacts":
                pass

            converted_text = convert_text(email_values)

            gmail(converted_text, email_name)

            print(
                f"""
*******************************************
What's it. Program was executed succesfully
Program generated and sent following email:
        {converted_text}
*******************************************
            """
            )
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            sys.exit(0)

    except IndexError:
        print("\nUps! You missed something...")
        sys.exit(1)


if __name__ == "__main__":
    main()


# keybinds:
# 1. ctr + shitf + d - open debug
# 2. ctr + shift + z - redo
# 3. (fn) + f5 - start debug
# 4. (fn) + shift + f5 - end debug
# 5. (fn) + ctrl + shift + f5 - restart debug
# 6. (fn) + alt + f11 - step into debug
# 7. (fn) + alt + f10 - step over debug
