import sys, getopt
from argparse import ArgumentParser
import requests as req
import json
import time

def get_location():
    r = req.get('http://api.open-notify.org/iss-now.json')
    return json.loads(r.text) 

def get_pass(latitude, longitude):
    url =  "http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s" % (latitude, longitude)
    r = req.get(url)
    return json.loads(r.text) 


def get_people():
    r = req.get('http://api.open-notify.org/astros.json')
    return json.loads(r.text)

def main(argv):
    print(argv[0])
    if(argv[0] == 'loc'):
        d = get_location()
        print("The ISS current location at %s is %s ,%s" % (time.ctime(int(d['timestamp'])), d['iss_position']['latitude'], d['iss_position']['longitude']))
    elif(argv[0] == 'pass'):
         d = get_location()     
         p = get_pass(d['iss_position']['latitude'], d['iss_position']['longitude'])
         print("The ISS will be overhead %s, %s at %s for %s seconds" % (d['iss_position']['latitude'], d['iss_position']['longitude'],time.ctime(int(p['response'][0]['risetime'])),p['response'][0]['duration']))
    elif(argv[0] == 'people'):
        d = get_people()
        for i in d['people']:
            print("%s is in craft %s" % (i['name'], i['craft']))
    else:
        print('You did  not provided any argument or it did not match as per expected')

if __name__ == "__main__":
    main(sys.argv[1:])