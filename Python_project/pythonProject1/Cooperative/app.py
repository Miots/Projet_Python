from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

reservations = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        nom = request.form['nom']
        depart = request.form['depart']
        destination = request.form['destination']
        date = request.form['date']
        reservations.append({'nom': nom, 'depart': depart, 'destination': destination, 'date': date})
        return "Réservation effectuée avec succès !"
        return redirect('/reservations')
    else:
        return render_template('reservation.html')

@app.route('/reservations')
def list_reservations():
    return render_template('reservations.html', reservations=reservations)


if __name__ == '__main__':
    app.run(debug=True)
