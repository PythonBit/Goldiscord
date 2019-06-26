import requests

def send_message(token, channel_id, message):
    requests.post(
        url=f"https://discordapp.com/api/v6/channels/{channel_id}/messages",
        json={"content": message},
        headers={"Authorization": token}
    )