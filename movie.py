from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/movie', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_id = request.form.get('movie_id')
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d1df6f48b932dd8c70237849dc8ab349"
        r = requests.get(url)
        if r.status_code == 200:
            movie = json.loads(r.text)
            title = movie['original_title']
            info = movie['overview']
            tag = movie.get('tagline', 'No tagline available')
            backdrop_path = movie.get('backdrop_path')
            backdrop_url = f"https://image.tmdb.org/t/p/w1280{backdrop_path}" if backdrop_path else None
            return render_template('movie.html', title=title, info=info, tag=tag, backdrop_url=backdrop_url)
        else:
            error_message = "Movie not found. Please try another ID."
            return render_template('movie.html', error=error_message)

    return render_template('movie.html')

if __name__ == '__main__':
    app.run(debug=True)
