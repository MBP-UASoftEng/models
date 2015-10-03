from app import app, db
from flask import Flask
from .models import Transaction
import random

@app.route('/')
def hello():

	cashier_id = None
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

	return "Record created on database."