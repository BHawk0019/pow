#avwx.py

import requests
import time
import csv
import configparser
import unpacker
import json


class WxBrief:

    def __init__(self, metar, taf, aptName):
        #initializes WxBriefing

        self.metar = metar
        self.taf = taf
        self.aptName = aptName
        self.pirep = {}
        self.airmet = {}


    def output(self):
        #print outputs to test variables are correctly assigned

        print(f"{self.metar}")
        print(f"{self.taf}")
        print(f"{self.aptName}")
        print(f"{self.pirep}")
        print(f"{self.airmet}")

        return
    
    def updateData(self,pireps,airmets):
        self.pirep.update(pireps)
        self.airmet.update(airmets)


def checkConnection(r):
    if r.status_code == 200:
        print("Connection Successful.")
    else:
        print(f"!!!Error!!! {r.status_code}")

def buildWxReport():
    print("Checking METAR Data Integrity...")
    checkConnection(metarRequest)
    print("Checking TAF Data Integrity...")
    checkConnection(tafRequest)
    print("Checking PIREP/AIREP Data Integrity...")
    checkConnection(pirepRequest)
    print("Checking AIRMET/SIGMET Data Inegrity...")
    checkConnection(airmetRequest)





#Parse through CSV and Format to Readable Data
def buildMETAR(metar):
    metar_read = metar.text
    csv_file = csv.reader(metar_read.splitlines())

    debug_count = 1
    for row in csv_file:
        debug_count+=1

    if len(row) >= 2:  # Make sure the row has at least 2 columns, correctly selects METAR row
            metarAPT = row[0]  # Second column METAR RAW

           
    
    return metarAPT
    

def buildTAF(taf):
    taf_read = taf.text
    csv_file = csv.reader(taf_read.splitlines())

    debug_count = 1
    for row in csv_file:
        debug_count+=1
    
    if len(row) >= 2:  # Make sure the row has at least 2 columns, correctly selects METAR row
            if debug_count != 6:
                tafAPT = row[0]

    
    return tafAPT

def buildPIREP(pirep):
    pirep_read = pirep.text
    csv_file = csv.reader(pirep_read.splitlines())

    debug_count = 1
    for row in csv_file:

        if len(row) >= 2:  # Ignore Headers
            if debug_count != 6:
                pireps[row[0]] = row[-1]
        
        debug_count+=1

    return pireps


def buildAIRMET(airmet):
    
    airmet_read = airmet.text
    csv_file = csv.reader(airmet_read.splitlines())

    debug_count = 1
    for row in csv_file:

        if len(row) >= 2:  # Ignore Headers
            if debug_count != 6:
                airmets[row[1]] = row[0]
        
        debug_count+=1
    
    return airmets
    

def buildAPTdata():
    #create file reader object
    with open("stationinfo.json","r", encoding = "utf-8") as file:
        aptInfo = json.load(file)
    
    return aptInfo
    

    

#empty arrays for pireps and airmets
pireps = {}
airmets = {}


#current time object
current_epoch_time = int(time.time())


#Create Config.ini Object
config = configparser.ConfigParser()
config.read("config.ini")

airportName = config["GlobalVariables"]["airportName"]
baseurl = config["GlobalVariables"]["avWeatherURL"]
radius = config["GlobalVariables"]["defaultRadius"]



#Airport Data Info
stationID = buildAPTdata()
for station in stationID:
    if station['icaoId'] == airportName:
        apt_lat = station["lat"]
        apt_lon = station["lon"]
        
    


#METAR PARAMETERS
metarParams = {
    "stationString" : airportName,
    "dataSource" : "metars",
    "requestType" : "retrieve",
    "format" : "csv",
    "startTime" : current_epoch_time - 86400,
    "mostRecent" : "true"
}

#TAF PARAMETERS
tafParams = {
    "stationString" : airportName,
    "dataSource" : "tafs",
    "requestType" : "retrieve",
    "format" : "csv",
    "startTime" : current_epoch_time - 86400,
    "endTime": current_epoch_time + 86400,
    "mostRecent" : "true"
}

#PIREP and AIREP PARAMETERS
pirepParams = {
   
    "dataSource" : "aircraftreports",
    "requestType" : "retrieve",
    "format" : "csv",
    "startTime" : current_epoch_time - 21600, #Checks PIREPS from last 6 hours
    "radialDistance" : f"{radius};{apt_lon},{apt_lat}"
    
}


#AIRMET Parameters
airmetParams = {

    "dataSource" : "airsigmets",
    "startTime":current_epoch_time - 21600, #Checks AIRMETS from last 6 hours
    "endTime":current_epoch_time + 21600,
    "requestType" : "retrieve",
    "format":"csv",
    "boundingBox": f"{apt_lat-15},{apt_lon-15},{apt_lat+15},{apt_lon+15}" #!!!Set to current airport Lat and Long +- 10 degrees box

}


#start code
metarRequest = requests.get(baseurl, params = metarParams)
tafRequest = requests.get(baseurl, params = tafParams)
pirepRequest = requests.get(baseurl, params = pirepParams)
airmetRequest = requests.get(baseurl, params = airmetParams)

buildWxReport()

metar = buildMETAR(metarRequest)
taf = buildTAF(tafRequest)
pirep = buildPIREP(pirepRequest)
airmet = buildAIRMET(airmetRequest)
unpacker
aptData = buildAPTdata()

#create class object for departure airport
depAirport = WxBrief(metar, taf, airportName)
depAirport.updateData(pirep, airmet)
print(depAirport.output())

