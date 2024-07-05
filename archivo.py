import requests
import json

# URL y encabezados para la solicitud a la API
uri = "https://api.football-data.org/v4/competitions/PD/standings?season=2023"
headers = {'X-Auth-Token': 'dfcbb960ead6444dbb44fb6b46cced84'}

# Realizar la solicitud GET a la API
response = requests.get(uri, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear la respuesta JSON
    data = response.json()
    print(data)
    
    # Acceder a la lista de equipos
    teams = data.get('teams', [])
    standings = data.get('standings', [])

    for standing in standings:
        for team in standing['table']:
            print(f"Posición: {team['position']}")
            print(f"Equipo: {team['team']['name']}")
            print(f"Puntos: {team['points']}")
            print(f"Partidos jugados: {team['playedGames']}")
            print(f"Partidos ganados: {team['won']}")
            print(f"Partidos empatados: {team['draw']}")
            print(f"Partidos perdidos: {team['lost']}")
            print(f"Goles a favor: {team['goalsFor']}")
            print(f"Goles en contra: {team['goalsAgainst']}")
            print(f"Diferencia de goles: {team['goalDifference']}")
            print('-' * 40)

    # Imprimir información relevante de cada equipo
    for team in teams:
        print(f"ID: {team['id']}")
        print(f"Nombre: {team['name']}")
        print(f"Colores del club: {team['clubColors']}")
        print(f"Estadio: {team['venue']}")
        print(f"Sitio web: {team['website']}")
        print('-' * 40)
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
