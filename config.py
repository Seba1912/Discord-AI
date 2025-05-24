# config.py

import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

ROK_KEYWORDS = [
    "rise of kingdoms", "rok", "commander", "talent", "kvk", "rally", 
    "troops", "gathering", "expedition", "civilization", "legendary", 
    "f2p", "pay to win", "farm account"
]
