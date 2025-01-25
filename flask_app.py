from flask import Flask, render_template
import sys
from src.news_utils import get_top_news
app = Flask(__name__)

@app.route('/')

def home():
    title = 'Welcome to Our Website!'
    python_version = sys.version
    news_df = get_top_news()
    news_data = news_df.to_dict(orient='records')
    print(news_data)
    cricket_news = get_top_news(search_term="Cricket")
    cricket_data = cricket_news.to_dict(orient='records')
    print(cricket_data)
    return render_template('index.html', title=title, python_version=python_version, news_data=news_data, cricket_data=cricket_data)


@app.route('/about/')
def about():
    title = 'About Us'
    python_version = sys.version
    news_df = get_top_news()
    news_data = news_df.to_dict(orient='records')
    return render_template('index.html', title=title,  python_version=python_version, news_data=news_data)

if __name__ == '__main__':
    import os 
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
