# Борисова Юлия, 26 когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data




def get_new_track(order_response):
    return order_response.json().get("track")




def positive_assert(order_response):
    data.params_get["t"] = get_new_track(order_response)
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200

def test_order():
    order_response = sender_stand_request.post_new_order(data.order_body)
    positive_assert(order_response)

if __name__ == "__main__":
    import pytest
    pytest.main()

