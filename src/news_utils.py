# Description: This file contains utility functions to fetch news from Google News API.
def get_top_news(period="1h", search_term="India"):
    import pandas as pd
    from GoogleNews import GoogleNews

    news_object = GoogleNews(period=period)
    news_object.search(search_term)
    news = news_object.result(sort=True)
    news_object.clear()

    news_dataframe = pd.DataFrame.from_dict(news)
    news_dataframe['link'] = news_dataframe['link'].map(lambda x: x.split('&ved')[0])
    return news_dataframe

print(get_top_news().columns)