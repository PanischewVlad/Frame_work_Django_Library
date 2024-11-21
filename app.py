from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

tours = [
    {"країна": "Туреччина", "туроператор": "ТурКом", "ціна": 500, "число днів": 7},
    {"країна": "Єгипет", "туроператор": "СонцеТур", "ціна": 400, "число днів": 10},
    {"країна": "Греція", "туроператор": "МореТревел", "ціна": 600, "число днів": 5},
    {"країна": "Туреччина", "туроператор": "ТурКом", "ціна": 700, "число днів": 14},
    {"країна": "Італія", "туроператор": "СонцеТур", "ціна": 1000, "число днів": 8},
    {"країна": "Іспанія", "туроператор": "ТурКом", "ціна": 900, "число днів": 7},
    {"країна": "Франція", "туроператор": "МореТревел", "ціна": 850, "число днів": 6},
    {"країна": "Туреччина", "туроператор": "ТурКом", "ціна": 1200, "число днів": 10},
    {"країна": "Хорватія", "туроператор": "СонцеТур", "ціна": 750, "число днів": 12},
    {"країна": "Чехія", "туроператор": "МореТревел", "ціна": 500, "число днів": 5},
    {"країна": "Австрія", "туроператор": "РозумнийВибір", "ціна": 500, "число днів": 5},

]

operators = list(set(tour["туроператор"] for tour in tours)) 

@app.route('/')
def all_tours():
    return render_template('tours.html', tours=tours)
@app.route('/filter_tours', methods=["GET", "POST"])
def filter_tours():
    if request.method == "POST":
        operator = request.form.get('operator')
        price_order = request.form.get('price_order')

        if not price_order:
            return render_template('filter_tours.html', operators=operators, error_message="Будь ласка, виберіть порядок сортування за ціною.")

        filtered_tours = [tour for tour in tours if (tour["туроператор"] == operator or not operator)]

        if price_order == 'asc':
            filtered_tours = sorted(filtered_tours, key=lambda x: x['ціна'])
        elif price_order == 'desc':
            filtered_tours = sorted(filtered_tours, key=lambda x: x['ціна'], reverse=True)

        return render_template('filter_tours.html', operators=operators, filtered_tours=filtered_tours)

    return render_template('filter_tours.html', operators=operators)

if __name__ == "__main__":
    app.run(debug=True)