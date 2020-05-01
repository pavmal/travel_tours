from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)


@app.route('/')
def render_main():
    """
    Представление главной страницы
    :return: 'Здесь будет Главная страница'
    """
    return render_template('index.html')


@app.route('/about/')
def render_about():
    """
    Представление страницы "О сервисе"
    :return: Описание сервиса
    """
    return render_template('about.html')


@app.route('/departures/<departure>/')
def render_departures(departure):
    """
    Представление страницы с направлениями для путешествий
    :return: 'Здесь будет список направлений для путешествий'
    """
    return render_template('departure.html')


@app.route('/tours/<tour_id>/')
def render_tours(tour_id):
    """
    Представление страницы с турами путешествий
    :return: 'Здесь будет список туров ' + tour_id'
    """
    return render_template('tour.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 7777, debug=True)
#    app.run()  # for gunicorn server

toolbar = DebugToolbarExtension(app)
