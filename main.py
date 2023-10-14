import json
from datetime import datetime
from download import download_json

if __name__ == '__main__':
    # download_json("https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json","stops.json")

    stops = []
    with open("stops.json", "r") as read_file:
        stopsJSON = json.load(read_file)
        knownIDs = []

        for stop in stopsJSON[list(stopsJSON.keys())[0]]['stops']:
            if stop['stopId'] not in knownIDs:
                knownIDs.append(stop['stopId'])
                stops.append(stop)

    stops = sorted(stops, key=lambda x: x["stopDesc"])

    chosenStop = input("Podaj nr przystanku: ")
    print(stops[int(chosenStop)]['stopDesc'])

    download_json("http://ckan2.multimediagdansk.pl/departures","departures.json")

    with open("departures.json", "r") as read_file:
        departuresJSON = json.load(read_file)
        for departure in departuresJSON[str(stops[int(chosenStop)]['stopId'])] ['departures']:
            iso_time = departure['estimatedTime']
            time = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
            time = time.strftime('%H:%M')
            print(time)

    iso_time = '2023-10-14T10:11:14Z'
    time = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
    time = time.strftime('%H:%M')
    print(time)