import requests

def ban_user(token, server_id, user_id):
    requests.put(
        url=f"https://discordapp.com/api/v6/guilds/{server_id}/bans/{user_id}?delete-message-days=0&reason=Goldiscord%20FTW",
        headers={"Authorization": token}
    )