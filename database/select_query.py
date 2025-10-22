from .connect import get_connect


def is_register_by_id(chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                
                dbc.execute("select * from users where chat_id = %s",(chat_id))
                return dbc.fetchone()
    except Exception as err:
        print(f"Register: {err}")
        return None


def get_filter_products(category_id,season,gender):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                
                dbc.execute("select * from product where category_id = %s and season =%s and gender_type = %s ",(category_id,season,gender))
                return dbc.fetchall()
    except Exception as err:
        print(f"Filter Category: {err}")
        return None


def get_category_by_id(category_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                
                dbc.execute("select name from category where id = %s ",(category_id,))
                return dbc.fetchone()
    except Exception as err:
        print(f"Filter Category: {err}")
        return None

def get_category():
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                
                dbc.execute("select id from category where is_active = true")
                return dbc.fetchall()
    except Exception as err:
        print(f"Filter Product: {err}")
        return None