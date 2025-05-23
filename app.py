from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, WeatherRecord
import requests, os
from utils import get_weather_by_location, validate_location

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

@app.before_request
def create_tables_once():
    if not getattr(app, '_tables_created', False):
        db.create_all()
        app._tables_created = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        date = request.form['date']
        if validate_location(location):
            weather = get_weather_by_location(location)
            if weather:
                record = WeatherRecord(
                    location=location,
                    date=date,
                    temperature=weather['temp'],
                    condition=weather['condition']
                )
                db.session.add(record)
                db.session.commit()
        return redirect(url_for('records'))
    return render_template('index.html')

@app.route('/records')
def records():
    data = WeatherRecord.query.all()
    return render_template('records.html', data=data)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    record = WeatherRecord.query.get_or_404(id)
    record.temperature = float(request.form['temperature'])
    db.session.commit()
    return redirect(url_for('records'))

@app.route('/delete/<int:id>')
def delete(id):
    record = WeatherRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('records'))

@app.route('/export/json')
def export_json():
    data = WeatherRecord.query.all()
    return jsonify([
        {"location": r.location, "date": r.date, "temperature": r.temperature, "condition": r.condition}
        for r in data
    ])

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
