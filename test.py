
from flask import json
from urllib2 import urlopen
from posts.getScore_info import ScoreLive, ScoreCard, TeamInfo

#
# team_info = 'http://caprodseacs03.cloudapp.net/matches/1804/39746/detail?format=json'
# response = urlopen(team_info)
# data = json.loads(response.read())
#
# matchName = data['meta']['matchName']
# matchName = data['meta']['matchName']
#
# print matchName


# myList = [[{'a':1,'b':'Sadi'},{'a':2,'b':'Himel'}]]
myList = [[1,2,3,4]]
for i in myList:
    # for n in i:
        print i[0]