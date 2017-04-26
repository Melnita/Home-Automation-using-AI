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
  switch = bool(re.search(r'\bswitch the light off\b', text, re.IGNORECASE))
  switch2 = bool(re.search(r'\bswitch off the light\b', text, re.IGNORECASE))
  off = bool(re.search(r'\boff\b', text, re.IGNORECASE))

  if switch:
    return switch
  elif switch2:
    return switch2
  elif off:
    return off
  else:
   return False

def handle(text, mic, profile):
  messages = ["Lights are switched off.",
                "Switching lights off."]
  m1 = ["Lights will be switched off.",
	        "Be patient.",
	          "Don't annoy me."]
  message = random.choice(messages)
  m2 = random.choice(m1)
  mic.say(m2)
  ser.write('b')
  mic.say(message)