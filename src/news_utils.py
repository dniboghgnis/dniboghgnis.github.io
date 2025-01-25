# Description: This file contains utility functions to fetch news from Google News API.
def get_top_news(period="1h", search_term="India"):
    import pandas as pd
    from GoogleNews import GoogleNews
    from datetime import datetime

    news_object = GoogleNews(period=period)
    news_object.search(search_term)
    news = news_object.result(sort=True)
    news_object.clear()

    news_dataframe = pd.DataFrame.from_dict(news)
    print(news_dataframe.columns)
    news_dataframe['sanitized_link'] = news_dataframe['link'].map(lambda x: x.split('&ved')[0])
    
    # Convert datetime column to the desired format
    news_dataframe['sanitized_datetime'] = news_dataframe['datetime'].astype(str).apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f').strftime('%A, %d %B %Y, %I:%M %p')
    )
    
    return news_dataframe
