from wordcloud import WordCloud
import numpy as np
from .scripts import parser
from .modules.reddit import Reddit
import matplotlib.pyplot as plt
import pandas as pd

class Main:
    def __init__(self) -> None:
        args = parser.configure_parser()

        self.n = parser.cast_arg(args.n, int)
        self.limit = parser.cast_arg(args.limit, int)
        self.subreddit_name = args.subreddit

        reddit = Reddit(config_file_path='reddit_config.json', subreddit_name=self.subreddit_name, limit=self.limit)

        unique, count = reddit.get_trend_topics(self.n)
        if not unique:
            print('No trend topic found')
            return

        print(f'{len(unique)} trend topics found')
        for word, number in zip(unique, count):
            print(f'{word}({number})')

        wordcloud = WordCloud().generate(' '.join(unique))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    