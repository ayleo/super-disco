import requests

API_KEY = "e4f5785e7886c4ec72622d733a26266b"


def get_data(cityname, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    nr_values = 8 * days
    filtered_content = filtered_content[:nr_values]
    return filtered_content

if __name__ == "__main__":
    print(get_data("ldon", 2))
