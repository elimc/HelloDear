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
from telegram.client import Telegram
import functions as fn
import user_info as ui

if __name__ == '__main__':

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

    # Grab scammers ID or return False
    scammer_id = ui.get_scammer_info(tg, '5395841799')

    # Grab my ID or return False
    my_id = ui.get_my_info(tg)

    def new_message_handler(update):
        """
        This is the main function that handles new messages.
        """

        # Grab the most recent message in the chat.
        message_content = update['message']['content']
        message_text = message_content['text']['text']

        # Grab the sender's ID
        sender_user_id = update['message']['sender']['user_id']
        print(f'ID of last message sender: {sender_user_id}')

        if message_content['@type'] == 'messageText' and message_text == 'ping' and sender_user_id == my_id:

            # Make the AI seem more human with a delay.
            # fn.delay_response(0, 20)

            # Send a message to the chat.
            result = tg.send_message(
                chat_id=chat_id,
                text='pong',
            )

            result.wait()
            if result.error:
                print(f'send message error: {result.error_info}')
            # else:
            #     print(f'message has been sent: {result.update}')

    # Set up the new message handler.
    # Set off a script anytime a new message is received.
    tg.add_message_handler(new_message_handler)
    tg.idle()  # blocking waiting for CTRL+C
