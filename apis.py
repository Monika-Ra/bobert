import requests

def get_cat_fact():
  r = requests.get("https://meowfacts.herokuapp.com/")
  data = r.json()
  return data['data'][0]

