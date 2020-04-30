from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["GET","POST"])
def hello():
	api_key = "6bb245afb7309bafd35ae4b0226c676a"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	city_name = request.form.get("name")
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name  
	response = requests.get(complete_url)
	x = response.json()
	y = x["main"]
	current_temperature = y["temp"]-273  
	current_pressure = y["pressure"] 
	current_humidity = y["humidity"] 
	z = x["weather"] 
	weather_description = z[0]["description"] 
	return render_template("index.html", y=y, current_temperature=current_temperature, current_pressure=current_pressure, current_humidity=current_humidity, z=z, weather_description=weather_description, city_name=city_name)

if __name__=="__main__":
	main()