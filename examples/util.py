def getKey():
  with open("../apikey.txt", "r") as fd:
    return fd.read()

def getMapboxToken():
  with open("../mapbox_token.txt", "r") as fd:
    return fd.read()
