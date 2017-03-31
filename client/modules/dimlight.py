import random
import re
import serial

PRIORITY=6
ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["ROMANTIC", "LIGHT", "DIM", "TOO","BRIGHT"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  romatic = bool(re.search(r'\bromantic light\b', text, re.IGNORECASE))
  dim = bool(re.search(r'\bdim\b', text, re.IGNORECASE))
  toobright = bool(re.search(r'\btoo bright\b', text, re.IGNORECASE))

  if romatic:
	return romatic
  elif dim:
	return dim
  elif toobright:
  	return toobright
  else:
	return False

def handle(text, mic, profile):
  messages = ["Is this better?",
                "As you wish."]
  message = random.choice(messages)
  ser.write('c')
  mic.say(message)
  ser.close()
