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

``
# Imports
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import dbm
from pprint import pprint
from telegram.client import Telegram
import functions as fn
import user_info as ui

if __name__ == '__main__':

    # Open the database
    with dbm.open("hellodear", "c") as db:
        config = {str(key, "utf-8"): str(db.get(key), "utf-8")
                  for key in db.keys()}

    pprint(object=config, indent=4)

    # Choose size of pretrained model
    MODEL_NAME = "microsoft/DialoGPT-large"
    # MODEL_NAME = "microsoft/DialoGPT-medium"
    # MODEL_NAME = "microsoft/DialoGPT-small"

    # Set up conversationalai model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    # For Eli local chat.
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

    # Print status of program.
    print()
    print('Successfully logged in to Telegram! Waiting for messages...', '/n')

    def new_message_handler(update):
        """
        This is the main function that handles new messages.
        """

        # Grab the most recent message in the chat.
        message_content = update['message']['content']
        pprint(message_content)

        # Is it the scammer or me who sent last messae?
        sender_user_id = update['message']['sender']['user_id']
        print(f'ID of last message sender: {sender_user_id}')

        # Did we receive text?
        if message_content['@type'] == 'messageText':

            # Figure out if the last message was from the scammer or me.
            if message_content['text']['@type'] == 'formattedText' and sender_user_id == my_id:

                # If the last message was from me, then we need to respond.
                message_text = message_content['text']['text']

                # encode the input and add end of string token
                input_ids = tokenizer.encode(
                    message_text + tokenizer.eos_token, return_tensors="pt")
                # concatenate new user input with chat history (if there is)
                # bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids
                bot_input_ids = input_ids

                chat_history_ids = model.generate(
                    bot_input_ids,
                    max_length=1000,
                    do_sample=True,
                    top_p=0.95,
                    top_k=0,
                    temperature=0.75,
                    pad_token_id=tokenizer.eos_token_id
                )

                output = tokenizer.decode(
                    chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
                print(f'This is the output: {output}')

                # Make the AI seem more human with a delay.
                # fn.delay_response(0, 20)

                # Send a message to the chat.
                result = tg.send_message(
                    chat_id=chat_id,
                    text=output,
                )

                result.wait()
                if result.error:
                    print(f'send message error: {result.error_info}')
                # else:
                #     print(f'message has been sent: {result.update}')
            else:
                print(
                    'This is not a message from me. Or it is something other than text.')

        else:
            # A smile is a good default for the scammer.
            output = ':)'

            # Send a message to the chat.
            result = tg.send_message(
                chat_id=chat_id,
                text=output,
            )

            result.wait()
            if result.error:
                print(f'send message error: {result.error_info}')

    # Set up the new message handler.
    # Set off a script anytime a new message is received.
    tg.add_message_handler(new_message_handler)
    tg.idle()  # blocking waiting for CTRL+C
