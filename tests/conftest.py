import pytest
from app import app, db

@pytest.fixture(scope="session")
def test_client():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="function", autouse=True)
def clean_db():
    yield
    db.session.rollback()
    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()
