import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

def get_new_track(body):
    return post_new_order(body).json().get("track")

def get_order(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.PUT_ORDER,
                        params=track_order)
