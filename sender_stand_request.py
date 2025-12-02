import configuration
import requests


def post_create_orders(body):
    #Создание нового заказа.
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )


def get_order_by_track(track_number):
    #Получение заказа по трек-номеру.
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,
        params={"t": track_number}
    )