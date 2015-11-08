from app import app, db
from flask import Flask
from .models import Employee
from .models import Transaction
import random

@app.route('/')
def hello():

	# Employee
	first_name1 = "Manager".lower()
	last_name1 = "Manager".lower()
	active1 = True;
	password1 = "harsha1233"
	classification1 = "manager".lower().replace(" ", "")
	unique1 = False
	employee_id1 = None
	while not unique1:
		emp_id = random.randint(100000, 999999)
		exists = Employee.query.filter_by(employee_id = emp_id).all()
		if len(exists) == 0:
			unique1 = True
			employee_id1 = emp_id

	manager = Employee(first_name = first_name1, last_name = last_name1, active = active1, classification = classification1, password = password1, employee_id = employee_id1, manager = None)

	#Add the created entry to the table
	db.session.add(manager)

	first_name = "Harsha".lower()
	last_name = "Bande".lower()
	active = True
	password = "harsha123"

	classifications = ["generalmanager", "shiftmanager", "cashier"]

	classification = "Cashier".lower().replace(" ", "")

	if classification not in classifications:
		return "Incorrect classification"

	unique = False
	employee_id = None
	while not unique:
		emp_id = random.randint(100000, 999999)
		exists = Employee.query.filter_by(employee_id = emp_id).all()
		if len(exists) == 0:
			unique = True
			employee_id = emp_id

	#Create a entry in the employee table
	employee = Employee(first_name = first_name, last_name = last_name, active = active, classification = classification, password = password, employee_id = employee_id, manager = manager)
	
	#Add the created entry to the table
	db.session.add(employee)

	#Save the changes in the database
	db.session.commit()

	a = Employee.query.filter_by(first_name = "harsha").all()

	# return str(len(a))

	# Transaction
	cashier_id = 3
	amount = "%.2f" % random.uniform(0.01, 1000.00)

	transaction_types = ["sale", "return", "void"]

	transaction_type = "Sale".lower().replace(" ", "")

	if transaction_type not in transaction_types:
		return "Incorrect transaction type."

	parent_id = None

	# Create a entry in the transaction table
	transaction = Transaction(cashier_id = cashier_id, amount = amount, transaction_type = transaction_type, parent_id = parent_id)

	# Add the created entry to the table
	db.session.add(transaction)

	# Save the changes in the database
	db.session.commit()

	return "Records created on database."

@app.route('/lookup', methods=['GET'])
def lookup(lookup_code):
	 product = db.session.query(Product).filter_by(ItemLookupCode = lookup_code).first()