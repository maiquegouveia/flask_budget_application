from application import app, db
from flask import render_template, request, redirect, url_for
from .models import Spending, Installment
from datetime import datetime

@app.route('/')
def homepage():
    spendings = Spending.query.filter_by(paid=False)
    total = 0
    for spending in spendings:
        total += spending.cost_per_installment
    return render_template('homepage.html', total=total)

@app.route('/spendings')
def list_spendings():
    spendings = Spending.query.filter_by(paid=False).order_by(Spending.id.desc())
    return render_template('list-spendings.html', spendings=spendings)

@app.route('/spendings/add', methods=['GET', 'POST'])
def add_spendings():
    if request.method == 'POST':
        new_spending = Spending(
            title=request.form['title'],
            description=request.form['description'],
            date=request.form['date'],
            installments=request.form['installment'],
            cost_per_installment=round(float(request.form['total'])/int(request.form['installment']), 2),
            total=request.form['total'],
        )
        db.session.add(new_spending)
        for i in range(int(new_spending.installments)):
            db.session.add(Installment(
                num=i+1,
                spending=new_spending,
            ))
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('add-spendings.html')

@app.route('/spendings/<int:id>')
def edit_spending(id):
    spending = Spending.query.get(id)
    installments = Installment.query.filter_by(spending_id=spending.id).order_by(Installment.id.asc())
    return render_template('edit-spending.html', spending=spending, installments=installments)

@app.route('/spendings/<int:id_s>/<int:id_i>')
def pay_installment(id_s, id_i):
    installment = Installment.query.get(id_i)
    installment.paid = True
    installment.date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    installment.spending.installments -= 1
    db.session.commit()
    return redirect(url_for('list_spendings'))