from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCH2YslKHzdnFK_yJtTcIVBKW7t3Zhx-nYHKo7U18EcPDrZ_cR_C87EfAlYFg_jtm3uvsW7liCw38VEMmAjqD3MypJnrm3K6UjkRsIXyj7ziOFLHG0sbhnZKzvRfoZ6cQECtuj2tSx7-IcW3e5VrJlKdp_MmBr48N33upt2ZMXotY9MhHWWOHT4dpZRu8j16wMnO-BE971XhzgDyrTScAJABWuFtNRhjBDHSDyt1oU9IczdfDiY3OqQYch_sfguqWmp9wrI7PKIImozrkQthtuhzQaJIAcnY0H11dPGc2pE-H40cEzvRYClK8pFSYtbdEdOR_cL_j5I3fseIWmNbIyJZ7zMiwA     
")
BOT_TOKEN = getenv("BOT_TOKEN", "1801794399:AAHoclDv1kuZTFP2NguKqclUhtoV90cyXkQ")
BOT_NAME = getenv("BOT_NAME", "Jukebox")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Jukeboxsupport")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "3468784")
API_HASH = getenv("API_HASH", "da8b1b8ea605f64bb898cbc21d03527d")
BOT_USERNAME = getenv("BOT_USERNAME" ,"@virusjukeboxbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "virusjukebox")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "CapitalLondonRadio")
PROJECT_NAME = getenv("PROJECT_NAME", "Yui v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Yeagerist-Music-Streamer-Bot-V3/YuiHirasawaMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
