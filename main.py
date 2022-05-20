###############################################################################
#
# Name: HelloDear
# Purpose: Talk to scammers with an AI to waste their time.
# Maintainer: Team HelloDear
# Version: 0.1
#
# The admin's API info is located here. Your's will be different:
# https://my.telegram.org/apps
# 
# Installation of packages:
# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
# https://note.nkmk.me/en/python-pip-install-requirements/
#
# We use the following as a jump off point for our pretrained AI
# https://www.thepythoncode.com/article/conversational-ai-chatbot-with-huggingface-transformers-in-python
#
# These are other AI options:
# https://github.com/hyunwoongko/openchat
# https://medium.com/ai-network/everyones-ai-explore-ai-model-2-chatbot-open-chat-3ef6667a4788
#
###############################################################################


# Imports
import functions as f
import logging

# from utils import setup_logging
from telegram.client import Telegram

"""
Sends a message to a chat
Usage:
    python examples/send_message.py api_id api_hash phone chat_id text
"""

### TODO: Import Telegram Module!
if __name__ == '__main__':
    # setup_logging(level=logging.INFO)

    output = "pong"
    chat_id = 777000

    tg = Telegram(
        api_id='15928630',
        api_hash='0c6e608215ac598f07d44532bcae88d0',
        phone='+15092058617',
        database_encryption_key='changeme1234',
    )
    # you must call login method before others
    tg.login()

    # if this is the first run, library needs to preload all chats
    # otherwise the message will not be sent
    result = tg.get_chats()

    # `tdlib` is asynchronous, so `python-telegram` always returns you an `AsyncResult` object.
    # You can wait for a result with the blocking `wait` method.
    result.wait()

    if result.error:
        print(f'get chats error: {result.error_info}')
    else:
        print(f'chats: {result.update}')

    result = tg.send_message(
        chat_id=chat_id,
        text=output,
    )

    result.wait()
    if result.error:
        print(f'send message error: {result.error_info}')
    else:
        print(f'message has been sent: {result.update}')

    tg.stop()
