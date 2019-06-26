import requests

def flood_chat(token, channel_id):
    requests.post(
        url=f"https://discordapp.com/api/v6/channels/{channel_id}/messages",
        headers={"Authorization": token},
        json={"content":"."+"\n"*125+"."}
    )