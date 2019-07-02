import requests
import re
import sys

mac = raw_input("Enter one or more your MAC address with Spaces: ")
mac_address = mac.split(" ")

def getVendorName(x):

    if re.match("[0-9a-f]{2}([-:.])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower()):
        vendor = requests.get(
            'https://api.macaddress.io/v1?apiKey=at_vlI1yrNeMikipomW3wPWBoHzDZkOi&output=vendor&search='
            + x).text
        print "Vendor of ""\"%s\"" % x, "is :", vendor

    else:
        print "\"%s\"" % x, "is invalid MAC address"


for i in range(len(mac_address)):

    mac_val = mac_address[i].replace("'", " ")
    getVendorName(str(mac_val))
