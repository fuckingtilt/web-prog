from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    if start_date and end_date:
        url = "https://earthquake.usgs.gov/fdsnws/event/1/count"
        params = {
            "starttime": start_date,
            "endtime": end_date
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            count = response.text
            return f"<h3>Кількість землетрусів з {start_date} по {end_date}: {count}</h3>"
        else:
            return "Помилка при запиті до API"

    return '''
        <h2>Отримати кількість землетрусів</h2>
        <form method="get">
            Початкова дата: <input type="date" name="start"><br><br>
            Кінцева дата: <input type="date" name="end"><br><br>
            <input type="submit" value="Отримати">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)