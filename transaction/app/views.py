from app import app, db
from flask import Flask
from .models import Transaction

@app.route('/')
def hello():

	cashier_id = 7
	amount = 8.50
	transaction_type = 1
	parent_id = 5

	#Create a entry in the transaction table
	transaction = Transaction(cashier_id = cashier_id, amount = amount, transaction_type = transaction_type, parent_id = parent_id)
	
	#Add the created entry to the table
	db.session.add(transaction)

	#Save the changes in the database
	db.session.commit()

	a = db.session.query(Employee).filter_by(cashier_id = 7).all()

	return str(len(a))