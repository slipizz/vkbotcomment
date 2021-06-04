from vk import *
import pyfiglet
from colorama import init, Fore, Back, Style
import random, vk, time
import os
import sys
banner = ("""
 By ItsSlipiz
 VK: vk.com/itsslipiz
 YT: ItsSlipiz
 """)
print(banner)

subscribe = input("Подписаться на автора YouTube? (Y/n) ")
if subscribe == "y":
    os.system("termux-open-url 'https://www.youtube.com/channel/UCoyRci2cqwhL9ikLG-bd_8Q'")
elif subscribe == "n":
    token = input("Введите токен: ")
    user_id = input("Введите айди страницы: ")
    posts_id = input("Введите айди поста: ")
    msgs = input("Введите сообщение: ")
    session = vk.Session(access_token=token)
    apivk = vk.API(session, v = 5.95)
while True:
    try:
        print(apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999)))
    except:
        pass
    time.sleep(3)
