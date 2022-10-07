import urllib.request as request
import json


src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
    data=json.load(response)


clist=data["result"]["results"]

with open("data.csv", "w", encoding="utf-8") as file:
    for attraction in clist:
        if int(attraction["xpostDate"][:4])>=2015:
            file.write(attraction["stitle"]+"," + attraction["address"][5:8]+"," + attraction["longitude"]+"," + attraction["latitude"]+"," + "https"+attraction["file"].split("https")[1]+"\n")
