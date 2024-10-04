import requests

def get_coordinates(address: str) -> list:
    URL = "https://api-adresse.data.gouv.fr/search/?q="
    r = requests.get(URL + address)
    return r.json()['features'][0]['geometry']['coordinates'][::-1]
