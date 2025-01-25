from flask import Flask, render_template
import sys
from src.news_utils import get_top_news
from src.gpt_utils import call_gemini_api
app = Flask(__name__)

@app.route('/')
def home():
    title = 'Welcome to Our Website!'
    python_version = sys.version
    general_news = get_top_news()
    cricket_news = get_top_news(search_term="Cricket")
    poem = call_gemini_api(query="give a classical poem, any 2-4 lines would do. add new lines whereever required.\
                            end it with a new line and - name of author, and year of publication. \
                           avoid copyright material and anonymous, and always prefer famous poets")
    return render_template('index.html', 
                           title=title, 
                           python_version=python_version, 
                           news_data=general_news, 
                           cricket_data=cricket_news, 
                           poem = poem)


@app.route('/about/')
def about():
    title = 'About Us'
    python_version = sys.version
    general_news = get_top_news()
    print("General News: ", general_news)
    cricket_news = get_top_news(search_term="Cricket")
    print("Cricket News: ", cricket_news)
    poem = call_gemini_api(query="give a classical poem, any 2-4 lines would do. add new lines whereever required.\
                            end it with a new line and - name of author, and year of publication. \
                           avoid copyright material and anonymous, and always prefer famous poets")
    print("Poem: ", poem)
    return render_template('index.html', 
                           title=title, 
                           python_version=python_version, 
                           news_data=general_news, 
                           cricket_data=cricket_news, 
                           poem = poem)



if __name__ == '__main__':
    import os 
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
