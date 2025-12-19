from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("12089203"))
API_HASH = getenv("7d85eb5ce156d35f22500fd8ef43e7c2")

BOT_TOKEN = getenv("8342240625:AAEfMiRk8lYx2FhDyWdRvNKqz9EIewzVgBM", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7363967303"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQC4d3MAnqMHo8tWfZ5NbMTXKQhKLWxE1FbYBya4_6Qcc6_vUTdQvcKOBP8BQTm6Q3LnByLc07oY7MGPZTgpAK7OnZvpokYkJkbXgClC0R6GiBPSf5W-J6qEybF0rRLbmcyVK0BLoyeyVebGIE5aq_skHTZ0Sru5q4iIHjKeyaE35x587LuMupTsjlYaYpRZ_gyjlDV96EWSeIjh6UeHGJfSbboCovFxe4-udOixGK7fop4fgRmlSyCce4j5eaK1NMqPVDD_07KV5qkDHwEAKIEDg7jXLExmirqPxlhtxV2c8vi4-bMta_m8VMdO_SAgae0RmNKTnIbb6HsBL2nWoacMw8wM0wAAAAHxPH1xAQ", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+ZaDtAQ6-o_JmYjNl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+cZLd9MDDE95jNjc1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7363967303").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
