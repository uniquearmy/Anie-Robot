import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
      "Yup! I've Mentioned Everyone.",
      "There Was A Problem In Mentioning All.. Please Contact @Unknown_Hacker_X .",
      "Sed.. I Don't Wanna Mention.", 
      "Sed Loife.. Go Cry In D-Corner. I'm Not Gonna Tag/Mention All.",
  )

@run_async
def all(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /all Mentions Every In Group[s].
"""

__mod_name__ = "Everyone"

KILL_HANDLER = DisableAbleCommandHandler("all", all)

dispatcher.add_handler(ALL_HANDLER)
