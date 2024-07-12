from models.db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    value = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    date = db.Column(db.String(80), unique=False, nullable=False)

    is_done = db.Column(db.Boolean, unique=False, nullable=False)
    # A coin_id é usada como chave estrangeira da coluna id da tabela coin.
    coin_id = db.Column(db.Integer, db.ForeignKey("coin.id"), nullable=False)
    coin_value_high = db.Column(db.Float(precision=2))  # Nova coluna
    coin_value_low = db.Column(db.Float(precision=2))   # Nova coluna

    # Define um relacionamento entre a classe ItemModel e a CoinModel.
    coin = db.relationship("CoinModel", back_populates="items", uselist=False)


