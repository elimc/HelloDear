from numpy import random
from time import sleep

def delay_response(earliest=10, latest=30):
    """
    This function is used to delay the response of the bot.
    """
    sleeptime = random.uniform(earliest, latest)
    print("sleeping for:", sleeptime, "seconds")
    sleep(sleeptime)
    print("sleeping is over")
