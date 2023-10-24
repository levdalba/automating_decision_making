import requests

length = input("Do you want to see long or short anime? ").lower()

for anime_id in range(1, 1000):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()["data"].get("episodes")

        anime_title = response.json()["data"]["title"]
        if length == "long" and anime_data is not None and anime_data >= 100:
            print(f"{anime_title} has {anime_data} episodes")

        elif length == "short" and anime_data is not None and anime_data < 100:
            print(f"{anime_title} has {anime_data} episodes")
        else:
            continue

    else:
        continue
