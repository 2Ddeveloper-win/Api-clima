import requests 
import json
import cache
import funciones

from datetime import date, datetime

def api(city):
	ciudad = city



	Api_key = cache.os.getenv('WEATHER_API_KEY')
	tiempo = date.today()
	tiempo = tiempo.strftime("%Y-%m-%d")


	obtener_ciudad = cache.r.get("ciudad")#1.consulta en el cache si existe la ciudad

	if ciudad != obtener_ciudad:
		#3. la ciudad no existe en cache, se hace la consulta a la API
		url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{ciudad}/{tiempo}?key={Api_key}&contentType=json"
		response = requests.get(url)
		if response.status_code == 200:#4. la API responde correctamente
			busqueda = json.loads(response.text)
			cache.r.set("busqueda", json.dumps(busqueda))#5. se guarda la busqueda en cache
			cache.r.set("ciudad",ciudad)
			

		else:
			code = response.status_code
			busqueda = None
	else:#2.el cache responde 

		obtener_busqueda = cache.r.get("busqueda")
		busqueda = json.loads(obtener_busqueda)
		

	if busqueda:
		
		condicion = busqueda['days'][0]['conditions']
		temp = funciones.convertion_celcius(busqueda['days'][0]['temp'])
		hume = busqueda['days'][0]['humidity']
		viento = funciones.convertion_kmPorHora(busqueda['days'][0]['windspeed'])
		pres = busqueda['days'][0]['pressure']
		tiempo = datetime.strptime(tiempo, "%Y-%m-%d")
		tiempo = tiempo.strftime("%d-%m-%Y")
		
		return temp, hume, viento, pres, condicion, tiempo
	else:
		return None,code
		
