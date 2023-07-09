def choose_file(files):
    print("Choose a file to view:")
    for index, file in enumerate(files):
        print(f"{index + 1}. {file['filename']} - {file['date']}")

    choice = int(input("Enter the file number: "))

    if 1 <= choice <= len(files):
        selected_file = files[choice - 1]
        file_path = f"{selected_file['filename']}_{selected_file['date']}"
        ViewData.view_file(file_path)
    else:
        print("Invalid choice.")

def view_file(file_path):
    choice = input("Choose an option:\n1. Generate CSV file\n2. View in terminal (Print)\nEnter your choice: ")

    if choice == "1":
        ViewData.generate_csv(file_path)
    elif choice == "2":
        ViewData.print_file(file_path)
    else:
        print("Invalid choice.")

def generate_csv(file_path):
    csv_filename = f"{file_path}.csv"
    json_filename = f"{file_path}.json"

    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for product in data:
            writer.writerow(product)

    print(f"CSV file generated: {csv_filename}")


def print_file(file_path):
    json_filename = f"{file_path}.json"

    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for product in data:
        print(f"Product Name: {product['Product Name']}")
        print(f"Item ID: {product['Item ID']}")
        print(f"ID: {product['ID']}")
        print(f"Price: {product['Price']}")
        print(f"Old Price: {product['Old Price']}")
        print(f"URL: {product['URL']}")
        print("-" * 20)

choose_file(files)
view_file(file_path)
generate_csv(file_path)
print_file(file_path)

