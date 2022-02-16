import argparse
import json
import urllib.request
import urllib.parse


baseUrl = "https://api.nexushub.co/wow-classic/v1/items"


def goldSilverCopper(value):
    gold = int(value/(100*100))
    silver = int((value - (gold*100*100))/100)
    copper = (value - (gold*100*100) - silver*100)
    return f"{gold}g {silver}s {copper}c"


def prettyStats(stats):
    return f"\n    Min Buyout: {goldSilverCopper(stats['minBuyout'])}\n      (Historical Value: {goldSilverCopper(stats['historicalValue'])})\n      (Market Value: {goldSilverCopper(stats['marketValue'])})"



def requestData(url):
    f = urllib.request.urlopen(url)
    data = f.read()
    encoding = f.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))


def getItem(item, realm, faction):
    item = "-".join(item)
    data = requestData("/".join([baseUrl, realm + "-" + faction, item]))
    stats = data["stats"]
    print(data["name"])
    print("  Current: ", prettyStats(stats["current"]))
    print("  Previous: ", prettyStats(stats["previous"]))


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--realm", default="firemaw",
                        help="Realm Name")
    parser.add_argument("-f", "--faction", default="alliance",
                        help="Faction")
    parser.add_argument('item',  nargs='+',
                        help='Item Name')
    return parser.parse_args()


if __name__ == "__main__":
    args = parseArgs()
    getItem(args.item, args.realm, args.faction)
