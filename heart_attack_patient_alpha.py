import requests

url = 'http://127.0.0.1:9696/heart_attack_verifier'

patient = {
    "sex": "male",
    "diet": "healty",
    "country": "brazil",
    "continent": "south_america",
    "hemisphere": "southern_hemisphere",
    "age":73,
    "cholesterol":390,
    "heart_rate":48,
    "diabetes":1,
    "family_history":0,
    "smoking":1,
    "obesity":0,
    "alcohol_consumption":1,
    "exercise_hours_per_week":15,
    "previous_heart_problems":0,
    "medication_use":1,
    "stress_level":2,
    "sedentary_hours_per_day":9,
    "bmi":19,
    "triglycerides":390,
    "physical_activity_days_per_week":4,
    "sleep_hours_per_day":6,
    "blood_pressure_min": 83,
    "blood_pressure_max": 100,
    "income_30k": 8
}

response = requests.post(url, json=patient).json() 
print(response)

if response['heart_attack : ']== True:
    print("Send the patient to the doctor")
