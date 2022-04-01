# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:47:51 2022

@author: Sam-Zhou
"""

import numpy as np
import json
import pandas as pd
import matplotlib as plt

with open('D:/Football Datasets/SoccermaticsForPython-master/Statsbomb/data/competitions.json') as f:
    competitions = json.load(f)
    
with open('D:/Football Datasets/SoccermaticsForPython-master/Statsbomb/data/matches/43/3.json') as f:
    matches = json.load(f)
    
df = pd.json_normalize(matches, sep = '_')

team_required = 'Belgium'

for match in matches:
    if match['home_team']['home_team_name'] == team_required or match['away_team']['away_team_name'] == team_required:
        match_id = str(match['match_id'])
        home_team = match['home_team']['home_team_name']
        away_team = match['away_team']['away_team_name']
        home_team_score = str(match['home_score'])
        away_team_score = str(match['away_score'])
        competition_stage = match['competition_stage']['name']
        result = competition_stage + ': ' + home_team + ' ' + home_team_score + ' - ' + away_team_score + ' ' + away_team + ', match id = ' + match_id
        print(result)
        
match_id = 8655 # France vs. Belgium (1-0)

with open('D:/Football Datasets/SoccermaticsForPython-master/Statsbomb/data/events/' + str(match_id) + '.json') as f:
    events = json.load(f)
    
df = pd.json_normalize(events, sep = '_')
df = df.assign(match_id = str(match_id))

