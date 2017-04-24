import random
import re
from amazonproduct import API
from libraryAmz import ReadAsin

api = API(locale = 'in')

WORDS = ["SHOPPING", "SHOP", "BUY", "ELECTRONICS", "AMAZON"]

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.
    Arguments:
    text -- user-input, typically transcribed speech
  """
  shopping = bool(re.search(r'\bshopping\b', text, re.IGNORECASE))
  buyelectronics = bool(re.search(r'\bbuy electronics\b', text, re.IGNORECASE))
  amazon = bool(re.search(r'\bamazon\b', text, re.IGNORECASE))
  shop = bool(re.search(r'\bshop\b', text, re.IGNORECASE))

  if shopping:
	return shopping
  elif buyelectronics:
	return buyelectronics
  elif amazon:
  	return amazon
  elif shop:
  	return shop
  else:
	return False


asin = ""
def scrapeAmazon(searchString):
    for item in api.item_search('Electronics', Keywords=searchString):
        return item.ASIN

def handle(text, mic, profile):
  messages = ["What would you like to buy?",
                "Anything in particular?"]
  message = random.choice(messages)
  mic.say(message)
  blah = mic.activeListen()
  mic.say("Searching for" + blah + "on Amazon.")
  product = ReadAsin(scrapeAmazon(blah))
  name = product["NAME"]
  price = product["SALE_PRICE"]
  mic.say("WE found" + name + ". costing " + price + ".")