import random
import re
import serial

ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["SWITCH", "LIGHT", "ON", "BRIGHTER"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  switch = bool(re.search(r'\bswitch the light on\b', text, re.IGNORECASE))
  brighter = bool(re.search(r'\bbrighter\b', text, re.IGNORECASE))

  if switch:
    return switch
   elif brighter:
	return brighter
   else:
	return False

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
