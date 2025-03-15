#Ejercicio 3: Para las siguientes preguntas, toma como referencia el diccionario siguiente y escribe el código necesario para que imprimas lo que se solicita en cada pregunta: 

datosClima = {'lat': 28.5421, 

              'lon': -81.379, 

              'timezone': 'America/New_York', 

              'timezone_offset': -18000, 

              'daily':  

[{'dt': '09/Sep/24', 'temp': 26.33,'pressure': 1020, 'humidity': 58}, 

                   {'dt': '10/Sep/24', 'temp': 28.03, 'pressure': 1018, 'humidity': 47}, 

                   {'dt': '11/Sep/24', 'temp': 28.93, 'pressure': 1018, 'humidity': 56}, 

                   {'dt': '12/Sep/24', 'temp': 30.8, 'pressure': 1018, 'humidity': 46}, 

                   {'dt': '13/Sep/24', 'temp': 27.17, 'pressure': 1019, 'humidity': 61}, 

                   {'dt': '14/Sep/24', 'temp': 24.02, 'pressure': 1020, 'humidity': 67}, 

                   {'dt': '17/Sep/24', 'temp': 23.73, 'pressure': 1023, 'humidity': 40}, 

                   {'dt': '18/Sep/24', 'temp': 24.7, 'pressure': 1024, 'humidity': 39}]} 

#1. ¿Cómo puedo obtener la latitud y longitud del lugar registrado en datosClima? 

latitud = datosClima.get('lat')
longitud = datosClima.get('lon')
print(f"Latitud: {latitud}, Longitud: {longitud}")

#2. ¿Imprimir el valor de la presión atmosférica el 11 de septiembre? 

for dia in datosClima['daily']:
    if dia['dt'] == '11/Sep/24':
        presion_11_sep = dia['pressure']
        print(f"Presión el 11 de Septiembre: {presion_11_sep} hPa")
        break

#3. ¿Cuál es la humedad relativa el 13 de septiembre? 

for dia in datosClima['daily']:
    if dia['dt'] == '13/Sep/24':
        humedad_13_sep = dia['humidity']
        print(f"Humedad el 13 de Septiembre: {humedad_13_sep}%")
        break


#4. ¿Cómo accedo a la lista completa de datos diarios (claves 'daily')? 

for dia in datosClima['daily']:
    print(dia)

#5. ¿Cómo obtengo la temperatura registrada el 14 de septiembre? 

for dia in datosClima['daily']:
    if dia['dt'] == '14/Sep/24':
        temperatura_14_sep = dia['temp']
        print(f"La temperatura el 14 de Septimebre: {temperatura_14_sep}°C")
        break

#6. ¿Cuántos elementos hay en la lista 'daily'?  

contador = 0
for dia in datosClima['daily']:
    contador += 1
print(f"Número de elementos en 'daily': {contador}")

