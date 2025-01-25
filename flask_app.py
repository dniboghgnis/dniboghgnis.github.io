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
    return news_dataframe.drop(columns=["img"])

@app.route('/')
# def home():
#     title = 'Welcome to Our Website!'
#     python_version = sys.version
#     news_df = get_top_news()
#     news_html = news_df.to_html(classes='news-table', index=False)
#     return render_template('index.html', title=title, python_version=python_version, news_html=news_html)

def home():
    title = 'Welcome to Our Website!'
    python_version = sys.version
    news_df = get_top_news()
    news_data = news_df.to_dict(orient='records')
    
    return render_template('index.html', title=title, python_version=python_version, news_data=news_data)



@app.route('/about/')
def about():
    title = 'About Us'
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)