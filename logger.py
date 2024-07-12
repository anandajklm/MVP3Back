from models.db import db
from models import CoinModel


def create_initial_coins():

    # Checa se a tabela está vazia, caso esteja, carrega os dados iniciais das stores (categorias).
    coin_count = db.session.query(CoinModel).count()
    if coin_count == 0:
        initial_coin_data = [
            {"name": "Real"},
            {"name": "Dólar"},
            {"name": "Euro"},
            {"name": "Bitcoin"},
            
        ]

        try:
            for coin_data in initial_coin_data:
                coin = CoinModel(**coin_data)
                db.session.add(coin)

            db.session.commit()
            print("Initial coins added successfully.")
        except Exception as e:
            db.session.rollback()
            print("Error adding initial coins:", e)