from app import db
import datetime

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cashier_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    transaction_type = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    created_on = db.Column(db.String)

    def __init__(self, cashier_id, amount, transaction_type, parent_id):
        self.cashier_id = cashier_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.parent_id = parent_id
        self.created_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Transaction %r>' % self.id