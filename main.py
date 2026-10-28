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
	print("-"*15)
	print("Just type item name to delete it.")
	print("-"*15)

	delete_item = input("Enter item to delete: ")

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

