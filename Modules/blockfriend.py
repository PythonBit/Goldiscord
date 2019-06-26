import requests
def block(token, target_id):
    try:
        requests.put(
            url=f"https://discordapp.com/api/v6/users/@me/relationships/{target_id}",
            headers={"Authorization":token},
            json={"type":"2"}
        )
    except Exception as e: print(e)