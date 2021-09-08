import os
import logging
from pyrogram import Client
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
logger = logging.getlogger(_name_)
logging.getLogger("pyrogram").setlevel(logging.WARNING)
if bool(os.environ.get("ENV", False)):
    from sampleconfig import config
else:
    from config import Config
if _name_ == "_main_":
    plugins = dict(root="plugins")
    bot = Client("pmbot",
    bot_token=Config.TG_BOT-TOKEN,
    api_id=Config.APP_ID,
    plugins=plugins)

.run()                                