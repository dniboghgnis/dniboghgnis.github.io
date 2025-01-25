# Description: This file contains utility functions to fetch news from Google News API.
def get_top_news(period="1h", search_term="India"):
    import pandas as pd
    from GoogleNews import GoogleNews
    from datetime import datetime

    news_object = GoogleNews(period=period)
    news_object.search(search_term)
    news = news_object.result(sort=True)
    news_object.clear()

    # Convert datetime in the dict itself
    for item in news:
        if 'datetime' in item:
            item['sanitized_datetime'] = datetime.strptime(str(item['datetime']), '%Y-%m-%d %H:%M:%S.%f').strftime('%A, %d %B %Y, %I:%M %p')
        if 'link' in item:
            item['sanitized_link'] = item['link'].split('&ved')[0]
    
    return news
