from application import db, app
from sqlalchemy.sql import func

class Spending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    cost_per_installment = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False, nullable=False)
    installment = db.relationship('Installment', backref='spending')

class Installment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, default=False, nullable=False)
    spending_id = db.Column(db.Integer, db.ForeignKey('spending.id'))
    date = db.Column(db.String(20))


