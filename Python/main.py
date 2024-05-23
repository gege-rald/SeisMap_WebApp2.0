from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(
        location=[13.044031000000002, 123.45465545767141],
        zoom_start=13
    )
    return map._repr_html_()

@app.route("/open-street-map")
def open_street_map():
    map = folium.Map(
        location=[13.044031000000002, 123.45465545767141],
        tiles='Stamen Toner',
        zoom_start=13,
        attr='Map tiles by <a href="https://stamen.com">Stamen Design</a>, under <a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, under <a href="https://www.openstreetmap.org/copyright">ODbL</a>.'
    )
    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
