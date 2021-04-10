import requests
import os
import json

token = os.environ.get("apitoken") #enviroment variable to store the api token
baseurl = "https://cloud.iexapis.com/" #to quickly switch from sandbox to actual


def get_appl():
    r = requests.get("https://cloud.iexapis.com/stable/stock/FB/chart/date/20191107?token=sk_666a7e90d070456194a5231a68f9ed5b")
    print(r.text)
    return r.text

def get_snp():
    #snp.json is formatted like: "Name", "Sector", "Symbol" - we only need Symbol
    #for each symbol in snp call iex and add that data into json that lists the symbols as well as the data
    print(os.getcwd())
    f = open(r"static\snp.json")
    s = json.load(f) #Load up the json file
    returner = ""
    for p in s:
        r = requests.get(baseurl+"stable/tops?token="+"sk_666a7e90d070456194a5231a68f9ed5b"+"&symbols="+p["Symbol"])
        print(r.text)
    return returner

get_appl()
