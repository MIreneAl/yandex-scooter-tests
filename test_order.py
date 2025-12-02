# Ирина Маркова, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def test_create_order_and_get_by_track():
    response = sender_stand_request.post_create_orders(data.order_body)
    assert response.status_code == 201
    
    track_number = response.json()["track"]
    response_get = sender_stand_request.get_order_by_track(track_number)
    
    assert response_get.status_code == 200

     