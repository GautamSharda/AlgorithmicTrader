import requests
import os
import json

token = os.environ.get("apitoken") #enviroment variable to store the api token
baseurl = "https://sandbox.iexapis.com/" #to quickly switch from sandbox to actual


def get_appl():
    r = requests.get("https://sandbox.iexapis.com/stable/tops?token="+token+"&symbols=aapl")
    return r.text

def get_snp():
    #snp.json is formatted like: "Name", "Sector", "Symbol" - we only need Symbol
    #for each symbol in snp call iex and add that data into json that lists the symbols as well as the data
    print(os.getcwd())
    f = open(r"static\snp.json")
    s = json.load(f) #Load up the json file
    returner = ""
    for p in s:
        r = requests.get(baseurl+"stable/tops?token="+token+"&symbols="+p["Symbol"])
        print(r.text)
    return returner

get_snp()
