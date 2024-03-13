import requests

def get_last_three_opponents(username):
    url = f"https://lichess.org/api/games/user/{username}?max=3"
    response = requests.get(url, headers={"Accept": "application/x-ndjson"})

    if response.status_code != 200:
        print("Failed to retrieve data.")
        return

    games = response.text.strip().split("\n")
    opponents = []

    for game in games:
        game_data = eval(game)
        if game_data["players"]["white"]["user"]["name"] == username:
            opponent = game_data["players"]["black"]["user"]["name"]
        else:
            opponent = game_data["players"]["white"]["user"]["name"]
        opponents.append(opponent)

    return opponents

username = "your_lichess_username"
last_three_opponents = get_last_three_opponents(username)
print("Last three opponents:", last_three_opponents)

