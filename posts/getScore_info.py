import re

class ScoreLive(object):
    def __init__(self):
        self.series_info = {}


    def getScore(self, data):
        self.series_info = {'series_id':data['series']['id'],
                            'match_id': data['id'],
                            'series_name': data['series']['shortName'],
                            'series_logo': data['series']['shieldImageUrl'],
                            'homeTeam': data['homeTeam']['shortName'],
                            'homeTeam_color': data['homeTeam']['teamColour'],
                            'homeTeam_logo': data['homeTeam']['logoUrl'],
                            'awayTeam':data['awayTeam']['shortName'],
                            'awayTeam_color': data['awayTeam']['teamColour'],
                            'awayTeam_logo':data['awayTeam']['logoUrl'],
                            'homeScore': data['scores']['homeScore'],
                            'homeOvers': data['scores']['homeOvers'],
                            'awayScore': data['scores']['awayScore'],
                            'awayOvers': data['scores']['awayOvers'],

                            }


class TeamInfo(object):
    def __init__(self):
        self.teams = {}
    def getTeam(self, data):
        self.teamInfo = {

                        'hometeam':data['homeTeam']['shortName'],
                        # 'hometeam_full': re.sub('\Men$', '', data['homeTeam']['name']),
                        'hometeam_full': data['homeTeam']['name'],
                        'awayteam_full': data['awayTeam']['name'],
                        'homelogo': data['homeTeam']['logoUrl'],
                        'homecolor': data['homeTeam']['teamColour'],
                        'awayteam': data['awayTeam']['shortName'],
                        'awaylogo': data['awayTeam']['logoUrl'],
                        'awaycolor': data['awayTeam']['teamColour'],
                        'homeScore':data['scores']['homeScore'],
                        'awayScore': data['scores']['awayScore'],
                        'startDate': data['localStartDate'],
                        'result': data['matchSummaryText'],
                        'venue': data['venue']['name'],


                        }

class ScoreCard(object):
    def __init__(self):
        # self.scorecard = {}
        self.batsmen = []
        self.bowlers= []
        self.other_info= {}


    def getScoreCard(self, data):
        for innings in data['innings']:
            self.batsmen.append(innings['batsmen'])
            self.bowlers.append(innings['bowlers'])
            # self.extras.append([innings['legBye'], innings['wide'], innings['noBall'],innings['bye']])
            # self.other_info ={
            #     'wickets': innings['wicket'],
            #     'runs': innings['run'],
            #     'over': innings['over'],
            #
            # }