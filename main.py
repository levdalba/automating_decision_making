from random import choice

anime = [
    ["naruto", "hype", "long", "series"],
    ["hayku", "sports", "short", "series"],
    ["bleach", "hype", "medium", "series"],
    ["one piece", "adventure", "long", "series"],
]

mood = input("enter your mood: ")

for item in anime:
    if item[1] == mood:
        print(mood + " anime: " + item[0])
