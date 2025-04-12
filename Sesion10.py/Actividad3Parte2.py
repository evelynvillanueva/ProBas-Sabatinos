import requests 

def obtener_planetas(api_url="https://swapi.dev/api/planets/"):
    try: 

        poblaciones = []

        while api_url: 
            response = requests.get(api_url)

            if response.status_code == 200: 
                data = response.json()

                for planeta in data['results']: 

                    poblacion = planeta['population']
                    if poblacion == 'unknown':
                        poblaciones.append(0)
                    else:
                        try: 
                            poblaciones.append(int(poblacion))
                        except ValueError: 
                            print(f"Población no válida en el planeta {planeta['name']}. Valor: {poblacion}")

                api_url = data.get('next', None) 
            else: 
                print(f"No se logró obtener la información requerida. Código de error: {response.status_code}")    
                return 
        
        if poblaciones: 
            promedio_poblacion = sum(poblaciones) / len(poblaciones)
            print(f"El promedio de la población de los planetas es: {promedio_poblacion:.2f}")
        else: 
            print("No se encontraron planetas con datos sobre la población.")

    except requests.exceptions.RequestException as e: 
        print("No hay conexión.", e)

obtener_planetas()
