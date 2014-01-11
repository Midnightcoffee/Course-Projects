"""
       File : happiest_state.py
     Author : Drew Verlee
       Date : 11.05.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : finds the happiest_state using data from twitter!
"""
import json
import sys
from pprint import pprint


def get_US_and_EN_tweets(tweet_file):
    US_tweets = {} # state: [tweet, tweet ...]
    for line in tweet_file:
        jline = json.loads(line)
        if 'text' in jline and 'place' in jline: # and 'lang' in jline:
            # if jline['lang'] == 'en':
            jplace = jline['place']
            if jplace:
                if 'full_name' in jplace and \
                ('country' in jplace and jplace['country'] == 
                        'United States') or \
                ('country_code' in jplace and jplace['country_code'] == 'US'):
                    state = jplace['full_name'].split(',')[1].strip().lower().\
                    encode('utf-8')
                    if len(state) == 2:
                        if state not in US_tweets:
                            US_tweets[state] = [jline['text']]
                        else:
                            US_tweets[state].append(jline['text'])
    return US_tweets


def create_affin_dict(affin_file):
    """ create are dictionary so we can easily look up words and assign scores"""
    affin_dict = {}
    for line in affin_file:
        line_split = line.split('\t')
        word, score = line_split[0], int(line_split[1])
        affin_dict[word] = score
    return affin_dict


def create_score_states(st_tweets, affin_dict):
    """returns a dict of states with there tweet scores"""
    scored_states = {} # state : [score,count tweets]
    for st, tweets in st_tweets.items():
        if st not in scored_states:
            scored_states[st] = [0.0, 0]
        for tweet in tweets:
            for word in tweet.split():
                if word in affin_dict:
                    scored_states[st][0] += float(affin_dict[word])
                    scored_states[st][1] += 1
    return scored_states

def create_ranked_states(scored_state_dict):
    """ returns happiest state """
    ranked_states = {}
    for state, scores in scored_state_dict.items():
        if state not in ranked_states:
            ranked_states[state] = 0
        total_score, total_count = scores[0], scores[1]
        try:
            average_score = total_score/ total_count
        except ZeroDivisionError:
            average_score = 0
        ranked_states[state] += average_score
    return ranked_states

def find_happiest_state(ranked_states):
    high_score = 0
    highest_state = None
    for state, score in ranked_states.items():
        if high_score < score:
            high_score = score
            highest_state = state
    return highest_state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    affin_dict = create_affin_dict(sent_file)
    tweets_by_state = get_US_and_EN_tweets(tweet_file)
    scored_tweets = create_score_states(tweets_by_state, affin_dict)
    ranked_states = create_ranked_states(scored_tweets)
    happiest_state = find_happiest_state(ranked_states)
    print happiest_state


if __name__ == '__main__':
    main()

# Outdated options
# aff = open('AFINN-111.txt')
# print affin_score(example, create_affin_dict(aff))


