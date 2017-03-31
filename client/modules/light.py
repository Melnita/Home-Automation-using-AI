import random
import re
import serial

ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["FLASH"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\bflash\b', text, re.IGNORECASE))

def handle(text, mic, profile):
  messages = ["Lights are switched on.",
                "Switching lights on."]
  m1 = ["Lights will be switched on.",
	  "Be patient.",
	    "Don't annoy me."]
  message = random.choice(messages)
  m2 = random.choice(m1)
 # m1 = 'Lights will be on'
  mic.say(m2)
  ser.write('a')
  mic.say(message)
  ser.close()
