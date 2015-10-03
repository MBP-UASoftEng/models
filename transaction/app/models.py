from app import db
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Transaction(db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    # cashier_id = db.Column(db.Integer, ForeignKey("employee.id"), nullable=False)
    cashier_id = db.Column(db.Integer, nullable=True) # Just for tests. Should interact with the "employee" table, as the line above.
    amount = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None), nullable=False)
    transaction_type = db.Column(db.String, nullable=False)
    parent_id = db.Column(db.Integer, ForeignKey("transaction.id"), nullable=True)
    timestamp = db.Column(db.String, nullable=False)

    def __init__(self, cashier_id, amount, transaction_type, parent_id):
        self.cashier_id = cashier_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.parent_id = parent_id
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Transaction ID %r>' % self.id