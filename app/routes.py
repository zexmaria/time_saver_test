from email.policy import default
from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Item
from datetime import datetime, UTC

"""
    Aréa responsável por criar as rotas, a lógica de cada página e a renderização dos templates
"""

@app.route('/')
def index():
    items_ = Item.query.all()

    name = request.args.get('name', '').strip()
    service = request.args.get('service', '').strip()
    date = request.args.get('date', '').strip()

    all_names = db.session.query(Item.name).distinct().all()
    all_services = db.session.query(Item.service).distinct().all()

    all_names = [n[0] for n in all_names]
    all_services = [s[0] for s in all_services]

    query = Item.query

    if name:
        query = query.filter(Item.name == name)
    if service:
        query = query.filter(Item.service == service)
    if date:
        query = query.filter(Item.date == date)

    items_ = query.all()

    return render_template('index.html', items=items_, all_names=all_names,
                           all_services=all_services, name=name, service=service, date=date)


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

    now = datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M')

    return render_template('create.html', current_date=current_date, current_time=current_time)


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

