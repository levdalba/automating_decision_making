import requests

for anime_id in range(1, 1000):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()["data"]

        print(anime_data["title"])
    else:
        continue
