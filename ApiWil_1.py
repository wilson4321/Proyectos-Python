#Api usando framework flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular-distancia', methods=['POST'])
def calcular_distancia():
    try:
        #Aqui recivo la informacion de la distancia en km
        data = request.get_json()
        distancia_km = data['distancia_km']
        
        # Conversion 1km=1000m
        distancia_metros = distancia_km * 1000
        
        # Respuesta que enviara mi servicio
        response = {
            'distancia_metros': distancia_metros
        }
        return jsonify(response)
    #Mensaje por si se llega a presentar un error en la solicitud
    except Exception as e:
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud'}), 400
        

if __name__ == '__main__':
    app.run(debug=True)