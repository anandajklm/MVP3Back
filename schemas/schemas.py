from marshmallow import Schema, fields


# Código organizado em Plain__Schema e Schema.
# Motivo: como vamos incorporar dados das packs na tabela de items e dados de items na tabela de packs,
# precisamos ter schemas de items sem as packs e schemas de packs sem os items. Caso contrário,
# entraríamos em um loop de o item ter pack --> a pack do item ter item e assim
# por diante.

class PlainItemSchema(Schema):

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    value = fields.Int(required=True)
    quantity = fields.Int(required=True)
    date = fields.Str(required=True)
    is_done = fields.Bool(required=True)


class PlainCoinSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    value = fields.Int()
    date = fields.Str()
    quantity = fields.Int()


    is_done = fields.Bool()


class ItemSchema(PlainItemSchema):
    coin_id = fields.Int(required=True, load_only=True)
    coin = fields.Nested(PlainCoinSchema(), dump_only=True)


class CoinSchema(PlainCoinSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)