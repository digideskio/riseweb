from urllib2 import urlopen
from bs4 import BeautifulSoup
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from flask import json
from posts.getScore_info import ScoreLive, ScoreCard, TeamInfo
from posts.commentry_parser import Commentry
from posts.scoreboard import Score
from .models import Posts
import Get_Data

def index(request):
    try:
        post_list = Posts.objects.all().filter(featured_post = 'featured')
    except Posts.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    url = "http://caprodseacs03.cloudapp.net/matches?completedLimit=2&inProgressLimit=2&upcomingLimit=0&format=json"
    response = urlopen(url)
    data = json.loads(response.read())
    matches = data['matchList']['matches']
    # print matches

    match_list = []
    for match in matches:
        ob = ScoreLive()
        ob.getScore(match)
        match_list.append(ob.__dict__)

    print match_list
    context = {
        'post_list': post_list,
        'match_list': match_list,
    }
    return render(request, 'posts/main.html', context)


def score(request, series_id=None, match_id=None):

    team_info = 'http://caprodseacs03.cloudapp.net/matches/%s/%s/detail?format=json' % (series_id, match_id)
    response = urlopen(team_info)
    data = json.loads(response.read())
    teams = data['matchDetail']['matchSummary']
    toss  = data['matchDetail']['tossMessage']
    matchName = data['meta']['matchName']
    firstumpire= data['matchDetail']['umpires']['firstUmpire']['name'],
    secondumpire=  data['matchDetail']['umpires']['secondUmpire']['name'],
    ob= TeamInfo()
    ob.getTeam(teams)
    teamNames = ob.__dict__
    print teamNames['teamInfo']['homelogo']



    url = "http://caprodseacs03.cloudapp.net/scorecards/full/%s/%s?format=json" % (series_id, match_id)
    response = urlopen(url)
    data = json.loads(response.read())
    scoreCard = data['fullScorecard']
    ob = ScoreCard()
    ob.getScoreCard(scoreCard)
    scoreList = ob.__dict__

    team1_batsmen = scoreList['batsmen'][0]
    team2_batsmen = scoreList['batsmen'][1]
    team2_bowlers = scoreList['bowlers'][0]
    # team1_extra = scoreList['extras'][0]
    # team2_extra = scoreList['extras'][1]
    # otherInfo = scoreList['other_info'][1]
    # for scorelist in scoreList:
    #     print scoreList['batsmen']


    # manofthematchID = data['fullScorecardAwards']['manOfTheMatchId']
    # player_url = "http://caprodseacs03.cloudapp.net/players/%s/stats?format=json" % (manofthematchID)
    # response = urlopen(player_url)
    # player_profile = json.loads(response.read())
    # print player_profile['meta']['fullName']
    # player_name = player_profile['meta']['fullName']
    # player_image = player_profile['meta']['imageUrl']


    context = {
        'teamNames': teamNames,
        'toss': toss,
        'matchName': matchName,
        'firstumpire': firstumpire,
        'secondumpire': secondumpire,
        'team1_batsmen': team1_batsmen,
        'team2_bowlers': team2_bowlers,
        # 'team1_extra':team1_extra,
        # 'teamWin': scoreList['batsmen'][0],
        # 'teamLost': scoreList['batsmen'][1],
        # 'bowlersLost': scoreList['bowlers'][0]
    }


    return render(request, 'posts/score.html', context)

def article(request, id=None):
    post_detail = get_object_or_404(Posts, id=id)
    context= {
        'details' : post_detail
    }
    return render(request, 'posts/article.html', context)