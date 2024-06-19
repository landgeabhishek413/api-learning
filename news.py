from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_KEY = '055a3a64c5754f92a010230a134bfd37'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        url = f'https://newsapi.org/v2/everything?q={query}&from=2024-06-15&to=2024-06-15&sortBy=popularity&apiKey={API_KEY}'
        
        r = requests.get(url)
        if r.status_code == 200:
            news = json.loads(r.text)
            articles = news['articles']
            return render_template('news.html', articles=articles, query=query)
        else:
            error_message = "Failed to fetch news. Please try again later."
            return render_template('news.html', error=error_message)

    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
