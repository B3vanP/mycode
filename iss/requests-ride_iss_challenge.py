#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    ## Print the number of people in space
    print('\n\nPeople in Space:', helmetson['number'])

    ## Print the names and crafts of the people in space
    for person in helmetson['people']:
        print(f"{person['name']} on the {person['craft']}")

if __name__ == "__main__":
    main()

