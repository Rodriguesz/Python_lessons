import requests
from datetime import datetime


#? Pegando os dados
API_KEY = "94cd00cb0cc5343764b0ae458ffc8f0f"
APP_ID = "d6f85936"

url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise = input("Tell me which exercises you did: ")


exercise_body = {
    "query":exercise,
    # "gender":"female",
    # "weight_kg":72.5,
    # "height_cm":167.64,
    # "age":30
}

response = requests.post(url=url_endpoint, json= exercise_body, headers=headers)
result = response.json()


#? FULTRANDO OS DADOS
exercises = [{"name": exercise["name"], "calories": exercise["nf_calories"], "duration": exercise["duration_min"]} for exercise in result["exercises"]]


#? ADICIONANDO OS DADOS NO GOOGLE SHEET
add_row_endpoint = "https://api.sheety.co/2e04e18fb2b43ec14bb474082dcf1bde/myWorkouts/workouts"

sheet_headers = {
    "Authorization": "Bearer mysecuritytoken"
}

date=datetime.now()
hour = date.strftime('%H:%M:%S')
today = date.strftime("%d/%m/%Y")

for exercise in exercises:
    add_exercise = {
        "workout":{
            "date": today,
            "time": hour,
            "exercise": exercise["name"].title(), 
            "duration": exercise["duration"],
            "calories": exercise["calories"]
        }
    }
    requests.post(url=add_row_endpoint, json=add_exercise, headers=sheet_headers)



