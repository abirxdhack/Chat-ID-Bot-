#Copyright @ISmartCoder 
#Updates Channel t.me/TheSmartDev
from bot import bot
from utils import LOGGER
from core.start import start
from modules.help import help_command
from modules.my import my_command
from modules.admin import admin_command
from modules.me import me_command
from modules.fwd import handle_forwarded_message
from modules.username import username_command
from shared.chatinfo import handle_message

LOGGER.info("Bot Started Successfully 💥")
bot.run()
