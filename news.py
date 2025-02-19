# -*- coding:utf-8 -*-

import requests
import textwrap

class News:
    def __init__(self):
        pass

    def update(self, api_id):
        self.news_list = requests.get(
            f"https://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey={9c7dea03fa2b48158f90a0b9dd21fa55}").json()
        return self.news_list

    def selected_title(self):
        list_news = []
        if self.news_list["status"] == "ok":
            for i in range(len(self.news_list["articles"])):
                line = self.news_list["articles"][i]["title"]
                line = textwrap.wrap(line, width=30)
                list_news.append(line)
        else:
            list_news = ["Problem loading news"]
        return list_news
