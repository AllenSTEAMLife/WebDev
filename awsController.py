import boto.ses
import boto.dynamodb2
from boto.dynamodb2.table import Table

#establish a connection and get aws key and secret data from boto.config
#conn = boto.dynamodb2.connect_to_region('us-east-2')
conn = boto.dynamodb2.connect_to_region(
        'us-east-2',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_ACCESS_SECRET_KEY
    )

calendarTable = Table('STEAM-APP-Calendar', connection=conn)
clubsTable = Table('STEAM-APP-Clubs', connection=conn)

def get_club_items():
    clubItems = clubsTable.scan()
    listItems = list(clubItems)
    itemsList = []
    itemDictionary = {}
    socialList = []
    for item in listItems:
        itemDictionary = {}
        socialList = []
        #create the item dictionary
        try:
            itemDictionary.update({"Club-Name" : item["Club-Name"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"ID" : item["ID"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Dept" : item["Department"]})
        except:
            print("none of this type for object")
        try: 
            itemDictionary.update({"Description" : item["Description"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Leader" : item["Leader"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Location" : list(item["Location"])})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Meeting" : item["Meeting"]})
        except:
            print("none of this type for object")
        try:
            for network in item["Social"]:
                tempList = list(item["Social"][network])
                tempList.append(network)
                socialList.append(tempList)
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Social" : socialList})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Sponsor" : item["Sponsor"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Subtype" : item["Subtype"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Type" : str(item["Type"])})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Website" : item["Website"]})
        except:
            print("none of this type for object")
        itemsList.append(itemDictionary)
    return itemsList
def get_calendar_items():
    calendarItems = calendarTable.scan()
    listItems = list(calendarItems)
    itemsList = []
    itemDictionary = {}
    for item in listItems:
        itemDictionary = {}
        #create the item dictionary
        try:
            itemDictionary.update({"Event-Name" : item["Event-Name"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"ID" : item["ID"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Club" : str(item["Club"])})
        except:
            print("none of this type for object")
        try: 
            itemDictionary.update({"Description" : item["Description"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"End-Date" : item["End-Date"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"End-Time" : item["End-Time"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Max-Attendees" : str(item["Max-Attendees"])})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Start-Date" : item["Start-Date"]})
        except:
            print("none of this type for object")
        try:
            itemDictionary.update({"Start-Time" : item["Start-Time"]})
        except:
            print("none of this type for object")
        itemsList.append(itemDictionary)
    return itemsList
