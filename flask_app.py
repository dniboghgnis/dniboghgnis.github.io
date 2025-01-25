from flask import Flask, render_template
import sys
import pandas as pd

app = Flask(__name__)

def get_top_news(period="1h", search_term="India"):
    import pandas as pd
    from GoogleNews import GoogleNews

    news_object = GoogleNews(period=period)
    news_object.search(search_term)
    news = news_object.result(sort=True)
    news_object.clear()

    news_dataframe = pd.DataFrame.from_dict(news)
    return news_dataframe

@app.route('/')

def home():
    title = 'Welcome to Our Website!'
    python_version = sys.version
    news_df = get_top_news()
    news_data = news_df.to_dict(orient='records')
    return render_template('index.html', title=title, python_version=python_version, news_data=news_data)


@app.route('/about/')
def about():
    title = 'About Us'
    python_version = sys.version
    news_df = get_top_news()
    news_data = news_df.to_dict(orient='records')
    return render_template('index.html', title=title,  python_version=python_version, news_data=news_data)

if __name__ == '__main__':
    import os 
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
