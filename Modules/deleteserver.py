import requests

def delete_server(token, server_id):
    requests.post(
        url=f"https://discordapp.com/api/v6/guilds/{server_id}/delete",
        json={},
        headers={"Authorization": token}
    )