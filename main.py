import requests
import vk_api
import zulip
from dotenv import load_dotenv
import os


load_dotenv()
file = open("resume.txt", "w")


# Вконтакте
def info(parameter):
    return session.method('account.getProfileInfo')[parameter]


VK_TOKEN = os.getenv("VK_TOKEN")
session = vk_api.VkApi(token=VK_TOKEN)
vk = session.get_api()

file.write(info("last_name") + " " + info("first_name") + "\n")
file.write(info("status") + "\n")
file.write("Дата рождения: " + info("bdate") + "\n")
file.write("Родной город: " + info("home_town") + "\n")
file.write("Номер телефона: " + info("phone") + "\n")


# Zulip
client = zulip.Client(config_file="zuliprc")
data = zulip.Client(config_file="zuliprc").get_profile()

file.write("Email: " + data["email"] + "\n")


# GitHub
gitURL = "https://api.github.com/users/" + os.getenv("gitNickName")
gitData = requests.get(gitURL).json()

file.write("GitHub: " + gitData["html_url"] + "\n")
if gitData["company"] != None:
    file.write("Настоящее место работы: " + gitData["company"] + "\n")
file.write("Город: " + gitData["location"] + "\n")
file.write("О себе: " + gitData["bio"] + "\n")


file.close()
