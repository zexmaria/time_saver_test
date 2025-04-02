from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Item
from datetime import datetime, UTC

@app.route('/')
def index():
    items_ = Item.query.all()
    return render_template('index.html', items=items_)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        service = request.form['service']
        date = request.form['date']
        time = request.form['time']

        new_item = Item(name=name, service=service, date=date, time=time)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.service = request.form['service']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

