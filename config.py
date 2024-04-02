# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "22037149"
    API_HASH = "641d8722a9ef1c178db736c1da3b7631"
    #TOKEN = "7065766253:AAEm3nSDHD8tS5YtwdFetX7jTJrsQM4Q_sc"
    TOKEN = os.environ.get("7065766253:AAEm3nSDHD8tS5YtwdFetX7jTJrsQM4Q_sc", None)
    MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["7179817235"])
