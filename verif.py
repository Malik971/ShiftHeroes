import asyncio
import requests

async def get_plannings(api_token):
    url = "https://shiftheroes.fr/api/v1/plannings"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    def get_plannings_sync():
        response = requests.get(url, headers=headers)
        return response.json()
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, get_plannings_sync)

async def get_shifts(api_token, planning_id):
    url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    def get_shifts_sync():
        response = requests.get(url, headers=headers)
        return response.json()
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, get_shifts_sync)

async def create_reservation(api_token, planning_id, shift_id):
    url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts/{shift_id}/reservations"
    headers = {"Authorization": f"Bearer {api_token}"}
    reservation_data = {"seats": 1}
    
    def create_reservation_sync():
        response = requests.post(url, json=reservation_data, headers=headers)
        return response.status_code == 201
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, create_reservation_sync)

async def main():
    api_token = "e0c10c33f320f9a12fe93f8ffa40f52d"
    planning_id = "zPfMvk"
    
    plannings = await get_plannings(api_token)
    shifts = await get_shifts(api_token, planning_id)
    
    if shifts:
        shift_id = shifts[0]["id"]
        success = await create_reservation(api_token, planning_id, shift_id)
        if success:
            print("Créneau réservé avec succès.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
