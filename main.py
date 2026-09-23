from __future__ import annotations
import cache
import Back_end
from flask import Flask
from flask import render_template, request


from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


localhost = cache.os.getenv('REDIS_HOST')
puerto = cache.os.getenv('REDIS_PORT')
username = cache.os.getenv('REDIS_USERNAME')
password = cache.os.getenv('REDIS_PASSWORD')




app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri=f"redis://{username}:{password}@{localhost}:{puerto}",
    storage_options={"socket_connect_timeout": 30},
    strategy="fixed-window", # or "moving-window" or "sliding-window-counter"
)



@app.route("/")
@limiter.exempt
def Index():
    return render_template('Index.html')

@app.route("/pedir")
@limiter.limit("4 per day")
def pedir():
    return render_template('pedir.html')

@app.route("/clima")
@limiter.exempt
def clima():
    nombre_ciudad = request.args.get('ciudad')

    resultado = Back_end.api(nombre_ciudad)

    if resultado[0] != None:
        temp, hume, viento, pres, condicion,f = resultado
        return render_template('clima.html',ciudad = nombre_ciudad, tempu = temp, humedad = hume, presion = pres, vientos = viento, codition = condicion,Fecha = f )
    else:
        
        return resultado[1]
    
    

if __name__ == '__main__':
    app.run(debug=True)