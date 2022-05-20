from numpy import random
from time import sleep

def delay_response():
    """
    This function is used to delay the response of the bot.
    """
    sleeptime = random.uniform(10, 30)
    print("sleeping for:", sleeptime, "seconds")
    sleep(sleeptime)
    print("sleeping is over")
    