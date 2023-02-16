from application import db, app

class Spending(db.Model):
    __tablename__ = 'spending'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    cost_per_installment = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, title, description, date, installments, cost_per_installment, total):
        self.title = title
        self.description = description
        self.date = date
        self.installments = installments
        self.cost_per_installment = cost_per_installment
        self.total = total
        self.paid = False
