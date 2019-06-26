import requests

def leave_server(token, server_id):
    requests.delete(
        url=f"https://discordapp.com/api/v6/users/@me/guilds/{server_id}",
        headers={"Authorization":token}
    )