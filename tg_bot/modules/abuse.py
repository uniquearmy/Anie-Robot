import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Stfu and Gtfo U nub",
    "Ur dad gey bc",
    "Stfu bc",
    "Stfu go fuck yourself",
    "Bsdk",
    "Gay is here",
    "Ur mum gey",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Ur granny tranny",
    "Suck my dick",
    "Hey gey how are you?",
    "Fuck you hard",
    "Bitch",
    "U have breast",
    "You suck your dick?",
    "Wait I'm Fucking You", 
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /dark  🤬.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
