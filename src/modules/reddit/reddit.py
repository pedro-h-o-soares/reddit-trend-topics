import praw
import json
import numpy as np
from ...scripts.filters import filter_characters, filter_words

class Reddit:
    def __init__(self, config_file_path: str, subreddit_name: str='', limit: int=100):
        config = self.__get_config_file(config_file_path)

        reddit = praw.Reddit(
            client_id=config['client_id'],
            client_secret=config['client_secret'],
            password=config['password'],
            username=config['username'],
            user_agent=config['user_agent']
        )

        if subreddit_name:
            self.limit = limit
            self.subreddit = reddit.subreddit(subreddit_name)
            self.submissions = self.subreddit.new(limit=limit)

            self.__get_titles()

    def __get_config_file(self, config_file_path: str):
        f = open(config_file_path)
        config = json.load(f)
        f.close()

        return config
    
    def __get_titles(self):
        self.titles = np.array([])

        for submission in self.submissions:
            title = filter_characters(submission.title)

            self.titles = np.append(self.titles, title.split(' '))
        self.titles = filter_words(self.titles)

    def get_trend_topics(self, n) -> tuple[list[str], list[int]]:
        unique, count = np.unique(self.titles, return_counts=True)

        is_valid = [c > 1 for c in count]
        
        unique, count = unique[is_valid], count[is_valid]
        size = np.min([len(count), n])

        unique, count = unique[:size], count[:size]

        arg_sort_count = np.argsort(-count)

        return unique[arg_sort_count].tolist(), count[arg_sort_count].tolist()