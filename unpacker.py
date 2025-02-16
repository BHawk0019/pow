#gzip unpacker

import requests
import gzip
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
url = config["GlobalVariables"]["avStationcacheURL"]

unpacker = requests.get(url)



data = gzip.decompress(unpacker.content).decode("utf-8")

with open("stationinfo.json","wb") as file:
    file.write(data.encode("utf-8"))
    print("File unpacked and downloaded!")

file.close()