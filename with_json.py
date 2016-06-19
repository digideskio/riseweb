

import urllib, json
url = "http://caprodseacs03.cloudapp.net/matches?completedLimit=2&inProgressLimit=2&upcomingLimit=2&format=json"
response = urllib.urlopen(url)
data = json.loads(response.read())

matches = data['matchList']['matches']

for match in matches:
    series_name = match['series']['shortName']
    homeTeam = match['homeTeam']['shortName']
    awayTeam = match['awayTeam']['shortName']

    print homeTeam + ' vs ' + awayTeam
