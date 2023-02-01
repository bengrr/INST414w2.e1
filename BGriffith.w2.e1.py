"""
import pandas as pd

with pd.read_json('imdb_movies_1985to2022.json', 'r') as f:
    hugh_movies = []
    for row in f:
        for col in row:
            if "Hugh Jackman" in col:
                hugh_movies.append('test')
    print(hugh_movies)
    
    
"""
import json

counter = 0

with open('imdb_movies_1985to2022.json', 'r') as in_file:
    for line in in_file:
        this_movie = json.loads(line)
        
        actors = this_movie["actors"]
        actor_list = []
        for actor in actors:
            actor_name = actor[1]
            actor_list.append(actor_name)
            if 'Hugh Jackman' in actor_list:
                
#very unfinished
