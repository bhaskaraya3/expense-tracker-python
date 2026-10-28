print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("(press any key). Exit")

def add_expense():
	item_name = input("Enter Item name: ")
	amount = int(input("Enter Amount: "))

	expense:dict = {}

	expense['item_name'] = item_name
	expense['amount'] = amount

	print('Added')

	emp_list.append(expense)

def view_expense():
	if emp_list == []:
		print("-"*15)
		print("Oops no records.Try Addin expense to see them.")
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
	else:
		print("-"*15)
		print("Just type item name to delete it.")
		print("-"*15)

		delete_item = input("Enter item to delete: ")

		for expense in emp_list:
			if delete_item == expense['item_name']:
				emp_list.remove(expense)
				print(f"{delete_item} deleted successfully.")
			else:
				print(f"No expense found with item name '{delete_item}'.")

# emp_list.remove({"item_name": "Bus", "amount": 40})
# {"item_name": "Lunch", "amount": 120}
emp_list = []

while True:
	user_input = int(input("Enter Choice(1-4): "))

	if user_input == 1:
		my_list = add_expense()
		
	elif user_input == 2:
		view_expense()

	elif user_input == 3:
		delete_expense()

	else:
		break