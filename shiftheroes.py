import requests

# Get the planning of the current week
headers = {
    'Authorization': 'Bearer e0c10c33f320f9a12fe93f8ffa40f52d',
}

response = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)

# print(response.json()[2]['id'])
planning_id = response.json()[2]['id']

# Récupérer les créneaux du planning
response = requests.get('https://shiftheroes.fr/api/v1/plannings/' + planning_id + '/shifts', headers=headers)
shifts = response.json()

# Réserver tous les créneaux
for shift in shifts:
    # Vérifier s'il y a des places disponibles dans le créneau
    if shift['seats_taken'] < shift['seats']:
        # Réserver le créneau en envoyant une requête POST
        reservation_data = {
            'shift_id': shift['id'],
            'seats': shift['seats'] - shift['seats_taken']  # Réserver toutes les places disponibles
        }
        
        reservation_response = requests.post('https://shiftheroes.fr/api/v1/reservations', json=reservation_data, headers=headers)
        
        if reservation_response.status_code == 201:
            print(f"Créneau réservé : {shift['id']}")
        else:
            print(f"Échec de la réservation pour le créneau {shift['id']}")
    else:
        print(f"Aucune place disponible dans le créneau {shift['id']}")


# print(response.json())