import requests

# Assurez-vous d'avoir les informations nécessaires pour la requête
planning_id = "zPfMvk"
shift_id = "KnFBZbe"
api_token = "e0c10c33f320f9a12fe93f8ffa40f52d"

# Créez les données de réservation
reservation_data = {
    "seats": 1  # Nombre de places à réserver
}

# Construisez l'URL de l'API
url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts/{shift_id}/reservations"

# Ajoutez les en-têtes
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Créez trois réservations en utilisant une boucle
for _ in range(3):
    response = requests.post(url, json=reservation_data, headers=headers)

    if response.status_code == 201:
        print("Réservation créée avec succès.")
    else:
        print("Échec de la création de la réservation.")