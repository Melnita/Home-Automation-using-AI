import random
import re
import serial

ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["LIGHT", "OFF"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\blight off\b', text, re.IGNORECASE))

def handle(text, mic, profile):
  m1 = ["Lights will be switched off.",
	        "Be patient.",
	          "Don't annoy me."]
  m2 = random.choice(m1)
  mic.say(m2)
  ser.write('b')
  ser.close()