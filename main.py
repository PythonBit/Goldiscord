import threading
import ctypes
import colorama
import os
import Modules.serverspam as serverspam
import Modules.blockfriend as blockfriend
import Modules.leaveserver as leaveserver
import Modules.floodchat as floodchat

ctypes.windll.kernel32.SetConsoleTitleW("Goldiscord V1.6")
green = colorama.Fore.GREEN
normal = colorama.Style.RESET_ALL
colorama.init()

token = input("Authorization Token: ")
def main():
    print("__==Goldiscord V1.6==__")
    option = input("\n1) Server Spam\n2) Block Friend\n3) Leave Server\n4) Flood Chat\n>")

    if option == "1":
        print("Loaded module:"+green,"Server Spam"+normal)
        server_name = input("Server Name: ")
        serverspam.fuck_account(token, server_name)
        for _ in range(100): threading.Thread(target=serverspam.fuck_account).start()
        os.system("cls")
        print("Successfully executed module: " + green + "Server Spam"+normal)
        main()

    if option == "2":
        print("Loaded module:"+green,"Block Friend"+normal)
        target_id = input("Target User ID: ")
        blockfriend.block(token, target_id)
        os.system("cls")
        print("Successfully executed module: " + green + "Block Friend"+normal)
        main()

    if option == "3":
        print("Loaded module:"+green,"Leave Server"+normal)
        server_id = input("Server ID: ")
        leaveserver.leave_server(token, server_id)
        os.system("cls")
        print("Successfully executed module: " + green + "Leave Server"+normal)
        main()
    
    if option == "4":
        print("Loaded module:"+green,"Flood Chat"+normal)
        channel_id = input("Channel ID: ")
        floodchat.flood_chat(token, channel_id)
        os.system("cls")
        print("Successfully executed module: " + green + "Flood Chat"+normal)
        main()
main()