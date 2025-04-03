import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root2:raposa312@localhost/test'



TESTING = os.getenv("TESTING", "False").lower() == "true"

if TESTING:
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Banco em memória para testes
else:
    SQLALCHEMY_DATABASE_URI = "sqlite:///banco_real.db"  # Banco de produção