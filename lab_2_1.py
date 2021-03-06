import urllib.request, urllib.parse, urllib.error
import twurl
import folium
import json
import ssl

def main():
    """
    The main function for finding information from Twitter 
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        print('')
        acct = input('Enter Twitter Account:')
        if (len(acct) < 1): break
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '5'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        type_info = str(input("Which information you want to recieve?(Location/Name/Followers): "))
        js = json.loads(data)
        js_1 = js['users'][0]

        if type_info.lower() =="location":
            print(js_1['location'])
        elif type_info.lower()=="name":
            print(js_1["name"])
        elif type_info.lower()=="followers":
            for u in js['users']:
                print(u['screen_name'], ":", u['location'])
        else:
            print("Please try again!")

