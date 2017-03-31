import random
import re
import serial

ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["ROMANTIC", "LIGHT", "DIM", "TOO","BRIGHT"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\btoo bright\b', text, re.IGNORECASE))



def handle(text, mic, profile):
  messages = ["Is this better?",
                "As you wish."]
  message = random.choice(messages)
  ser.write('c')
  mic.say(message)
  ser.close()
