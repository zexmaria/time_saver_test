
from app.models import Item
from datetime import datetime, UTC
from app import db


def test_create_item(test_client):
    item = Item(name="Cliente Teste", service="Serviço Teste",
                date=datetime.now(UTC).date(), time=datetime.now(UTC).time())
    db.session.add(item)
    db.session.commit()

    item_db = Item.query.first()
    assert item_db is not None
    assert item_db.name == "Cliente Teste"
    assert item_db.service == "Serviço Teste"

"""
def test_update_item(test_client):
    item = Item.query.first()
    item.name = "Nome Alterado"
    db.session.commit()

    updated_item = Item.query.first()
    assert updated_item.name == "Nome Alterado"

def test_delete_item(test_client):
    item = Item.query.first()
    db.session.delete(item)
    db.session.commit()

    assert Item.query.first() is None

"""