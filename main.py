print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("(press any key). Exit")

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
FILE_PATH = PROJECT_DIR / "expenses.txt"

def check_file_exists():
    if not FILE_PATH.exists():
        FILE_PATH.touch()
        print("File created successfully.")
    else:
        print("File already exists.")

def file_list():
	with FILE_PATH.open('w',encoding='utf-8') as file:
		file.write(str(emp_list))

def get_item():
	item_name = input("Enter Item name: ")
	l_name = item_name.lower().strip()
	return l_name

def get_amount():
    while True:
        amount = int(input("Enter Amount: "))

        if amount <= 0:
            print("Invalid Amount. Try Again.")
        else:
            return amount

def add_expense():
	item_name = get_item()
	amount = get_amount()

	expense:dict = {}

	expense['item_name'] = item_name
	expense['amount'] = amount

	print('Added')

	emp_list.append(expense)

	file_list()

def view_expense():
	if emp_list == []:
		print("-"*15)
		print("Oops no records. Try Adding expense to see them.")
		print("-"*15)

	else:
		print("-"*15)
		print("Here is your current expense list")
		print("-"*15)
		for i in emp_list:
			for j,k in i.items():
				print(j,k)

def delete_expense():
	if emp_list == []:
		print("-"*15)
		print("Cannot Delete. No Records Available.")
		print("-"*15)
		return

	print("-"*15)
	print("Just type item name to delete it.")
	print("-"*15)

	delete_item = input("Enter item to delete: ").lower().strip()

	for expense in emp_list:
		if delete_item == expense['item_name']:
			emp_list.remove(expense)
			file_list()

			print(f"{delete_item} deleted successfully.")
			return

	print(f"No expense found with item name '{delete_item}'.")

emp_list = []

check_file_exists()

while True:
	user_input = int(input("Enter Choice(1-4): "))

	if user_input == 1:
		add_expense()
		
	elif user_input == 2:
		view_expense()

	elif user_input == 3:
		delete_expense()

	else:
		break

