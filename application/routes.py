from application import app, db
from flask import render_template, request, redirect, url_for
from .models import Spending

@app.route('/')
def homepage():
    spendings = Spending.query.filter_by(paid=False)
    total = 0
    for spending in spendings:
        total += float(spending.cost_per_installment)
    return render_template('homepage.html', total=total)

@app.route('/spendings')
def list_spendings():
    spendings = Spending.query.filter_by(paid=False).order_by()
    return render_template('list-spendings.html', spendings=spendings)

@app.route('/spendings/add', methods=['GET', 'POST'])
def add_spendings():
    if request.method == 'POST':
        db.session.add(Spending(
            request.form['title'],
            request.form['description'],
            request.form['date'],
            request.form['installment'],
            request.form['cost'],
            request.form['total'],
        ))
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('add-spendings.html')

@app.route('/spendings/<int:id>')
def edit_spending(id):
    spending = Spending.query.get(id)
    return render_template('edit-spending.html', spending=spending)