import random
from datetime import datetime, timedelta
from app import db, app
from app.models import Item

names = ["Alice", "Bruno", "Carla", "Diego", "Elisa", "Fernando", "Julia", "Henrique", "Isabela", "João", "Luiza"]

services = ["Consulta Geral", "Exame de Rotina", "Psicologia", "Fisioterapia", "Odontologia", "Psiquiatria"]


def random_date():
    today = datetime.today()
    future_date = today + timedelta(days=random.randint(1, 30))
    return future_date.strftime('%Y-%m-%d')


def populate_db(n=10):
    with app.app_context():
        for _ in range(n):
            new_item = Item(
                name=random.choice(names),
                service=random.choice(services),
                date=random_date(),
                time="14:00"
            )
            db.session.add(new_item)

        db.session.commit()
        print(f"\033[32m✅ {n} registros adicionados ao banco de dados!\033[0m")


if __name__ == "__main__":
    populate_db(20)