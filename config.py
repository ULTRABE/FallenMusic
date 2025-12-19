from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID") or 0)
if API_ID == 0:
    raise RuntimeError("API_ID is missing from environment variables")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

STRING_SESSION = getenv("STRING_SESSION")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "")

SUDO_USERS = list(
    map(int, getenv("SUDO_USERS", str(OWNER_ID)).split())
)

PING_IMG = getenv(
    "PING_IMG",
    "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg"
)

START_IMG = getenv(
    "START_IMG",
    "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg"
)

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
