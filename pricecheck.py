import argparse
import re

import requests

baseUrl = "https://api.nexushub.co/wow-classic/v1/items/firemaw-alliance/"


def goldSilverCopper(value):
    gold = int(value/(100*100))
    silver = int((value - (gold*100*100))/100)
    copper = (value - (gold*100*100) - silver*100)
    return f"{gold}g {silver}s {copper}c"

def prettyStats(stats):
    return f"\n    Min Buyout: {goldSilverCopper(stats['minBuyout'])}\n      (Historical Value: {goldSilverCopper(stats['historicalValue'])})\n      (Market Value: {goldSilverCopper(stats['marketValue'])})"

def getItem(item: str):
    item = item.replace(" ", "-")
    r = requests.get(baseUrl + item)
    data = r.json()
    stats = data["stats"]
    print(data["name"])
    print("  Current: ", prettyStats(stats["current"]))
    print("  Previous: ", prettyStats(stats["previous"]))


getItem("haste Potion")
