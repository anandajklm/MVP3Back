from models.db import db


class CoinModel(db.Model):
    __tablename__ = "coin"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # cria uma relação na base de dados onde os "items" estão associados ao modelo "ItemModel" por meio do campo "coin",
    # permitindo acesso flexível e dinâmico aos itens relacionados.
    items = db.relationship(
        "ItemModel", back_populates="coin", lazy=True, cascade="all,delete")