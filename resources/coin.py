from models.db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models import CoinModel
from schemas.schemas import CoinSchema

blp = Blueprint("Coins", "coins", description="Operações nas coins")


@blp.route("/coin/<int:coin_id>")
class Coin(MethodView):

    @blp.response(200, CoinSchema)
    def get(self, coin_id):
        """Faz a busca do coin a partir do ID informado."""
        coin = CoinModel.query.get_or_404(coin_id)
        return coin

    def delete(self, coin_id):
        """Deleta o coin a partir do ID informado."""
        coin = CoinModel.query.get_or_404(coin_id)
        db.session.delete(coin)
        db.session.commit()
        return {"message": "Coin deleted."}


@blp.route("/coin")
class CoinList(MethodView):
    @blp.response(200, CoinSchema(many=True))
    def get(self):
        """Faz a busca de todos os coins cadastrados."""
        return CoinModel.query.all()

    @blp.arguments(CoinSchema)
    @blp.response(201, CoinSchema)
    def post(self, coin_data):
        """Adiciona um novo coin à base de dados."""
        coin = CoinModel(**coin_data)
        try:
            db.session.add(coin)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A coin with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the coin.")

        return coin