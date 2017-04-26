import random
import re
import serial

PRIORITY=7
ser=serial.Serial('/dev/ttyACM0',9600)

WORDS = ["SWITCH", "LIGHT", "ON", "BRIGHTER", "TOO", "DIM" ,"DARK" ]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  switch = bool(re.search(r'\bswitch the light on\b', text, re.IGNORECASE))
  brighter = bool(re.search(r'\bbrighter\b', text, re.IGNORECASE))
  switch2 = bool(re.search(r'\bswitch on the light\b', text, re.IGNORECASE))
  dim = bool(re.search(r'\btoo dim\b', text, re.IGNORECASE))
  dark = bool(re.search(r'\bdark\b', text, re.IGNORECASE))

  if switch:
    return switch
  elif brighter:
	 return brighter
  elif switch2:
    return switch2
  elif dim:
    return dim
  elif dark:
    return dark
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
  ser.write('d')
  mic.say(message)