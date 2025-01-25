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
    
    # Debugging: Print the columns of the DataFrame
    print("Columns in news_dataframe:", news_dataframe.columns)
    
    # Check if 'link' column exists
    if 'link' in news_dataframe.columns:
        news_dataframe['sanitized_link'] = news_dataframe['link'].map(lambda x: x.split('&ved')[0])
    else:
        print("Error: 'link' column not found in the DataFrame")
    
    # Convert datetime column to the desired format
    if 'datetime' in news_dataframe.columns:
        news_dataframe['sanitized_datetime'] = news_dataframe['datetime'].astype(str).apply(
            lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f').strftime('%A, %d %B %Y, %I:%M %p')
        )
    else:
        print("Error: 'datetime' column not found in the DataFrame")
    
    return news_dataframe

print(get_top_news().columns)
