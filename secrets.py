import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import Filters

BOT_TOKEN = os.environ.get("TOKEN", "5286431733:AAFFocRJlOCvsItakH_Mnswj21VgvlfNkcA")
DB_URI = os.environ.get("DATABASE_URL", "postgres://pnkjtuwr:yQPxxlQ0hCEl3KEaCjFsaAot7bzKYION@arjuna.db.elephantsql.com/pnkjtuwr" )
SUDO_USERS = [
    1383624879
]
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = -1001335947029
