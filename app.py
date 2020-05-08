from flask import Flask, render_template, request
#from flask_debugtoolbar import DebugToolbarExtension
import data

app = Flask(__name__)


@app.route('/')
def render_main():
    """
    Представление главной страницы
    :return: 'Здесь будет Главная страница'
    """
    #    return render_template('about.html', hour= 13)
    if __name__ == '__main__':
        # for tour in data.tours.values():
        #    print(tour['title'])
        print(request.path)
        short_list_tours = {num: tour for num, tour in data.tours.items() if tour['stars'] in ['4', '5']}
        return render_template('index.html', title_gen=data.title, directions_menu=data.departures,
                               tours=short_list_tours)


@app.route('/about/')
def render_about():
    """
    Представление страницы "О сервисе"
    :return: Описание сервиса
    """
    short_list_tours = {num: tour for num, tour in data.tours.items() if tour['stars'] in ['4', '5']}
    return render_template('about.html', title_gen=data.title, directions_menu=data.departures,
                           tours=short_list_tours)


@app.route('/departures/<departure>/')
def render_departures(departure):
    """
    Представление страницы с направлениями для путешествий
    :return: 'Здесь будет список направлений для путешествий'
    """
    # print(request.path)
    direct = request.path.split('/')[-2]
    direction = {key: depart for key, depart in data.departures.items() if key == direct}
    short_list_tours = {num: tour for num, tour in data.tours.items() if tour['departure'] == direct}
    price_list = []
    for key, val in short_list_tours.items():
        price_list.append(val['price'])
    night_list = []
    for key, val in short_list_tours.items():
        night_list.append(val['nights'])
    print(price_list)
    return render_template('departure.html', title_gen=data.title, directions_menu=data.departures,
                           departure=direction, tours=short_list_tours, prices=price_list, nights=night_list)


@app.route('/tours/<tour_id>/')
def render_tours(tour_id):
    """
    Представление страницы с турами путешествий
    :return: 'Здесь будет список туров ' + tour_id'
    """
    print(request.path)
    #    direct = request.path.split('/')[-4]
    tour_id = request.path.split('/')[-2]
    print(tour_id)
    tour = data.tours[int(tour_id)]
    direct = data.tours[int(tour_id)]['departure']
    direction = {key: depart for key, depart in data.departures.items() if key == direct}
    short_list_tours = {num: tour for num, tour in data.tours.items() if tour['departure'] == direct}
    stars = '★' * int(data.tours[int(tour_id)]['stars'])
    return render_template('tour.html', title_gen=data.title, directions_menu=data.departures,
                           departure=direction, tours=short_list_tours, tour_info=tour, star_count=stars)


if __name__ == '__main__':
    #    app.run('127.0.0.1', 7777, debug=False)
    app.run()  # for gunicorn server

# toolbar = DebugToolbarExtension(app)
