import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymongo
import random
import string
import dns



client = pymongo.MongoClient("mongodb+srv://srinikhv712:ghJ5sO4vWWQpqgec@app.8pqdh8n.mongodb.net/?retryWrites=true&w=majority")

db = client["app"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/flights")
async def getFlightInfo(user : str):
    collection = db["flight"]
    flights = collection.find({"user" : user}, {"_id": 0})
    l = []
    for i in flights:
        l.append(i)
        print(i)
    return {"flights": l}


@app.get("/addFlights")
async def createroom(user:str, fromloc : str, from_abbr : str, time: str, toloc : str, to_abbr : str, date: str, departure : str, seat : str):
    try:
        collection = db["flight"]
        # seat = "".join(c for c in seat if c.isalnum())
        document = {"user" : user, "from" : fromloc, "from_abbr" : from_abbr , "time": time, "to" : toloc, "to_abbr" : to_abbr, "date":date, "departure":departure, "seat":seat}
        collection.insert_one(document)
        # print(1,"________________________________________________________________________")
        return  ""
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


# user
# "srinikrish712@gmail.com"
# from
# "Mumbai"
# from_abbr
# "MUM"
# time
# "8H 30M"
# to
# "London"
# to_abbr
# "LND"
# date
# "2 May"
# departure
# "09:00 AM"
# seat
# "33"