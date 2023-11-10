import requests
import datetime
import time
import random

# Get the current time
start_time = datetime.datetime.now()

# Calculate the end time by adding 3 hours to the current time
end_time = start_time + datetime.timedelta(hours=3)

# Define the API endpoint
url = "https://cricket.k2games.online/api/players/handle" 

while datetime.datetime.now() < end_time:
    # Sample data with 'timeCreated' field to be updated
    #   "score": "18020",
    #     "xorScore": "8112",
    # 20
    #  "score": "15872",
    #     "xorScore": "3744",
    data = {
        "phoneNumber": "0784478771",
        "score": "15872",
        "xorScore": "3744",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQ2h1dHRlIiwicGhvbmVOdW1iZXIiOiIwNzg0NDc4NzcxIiwiaWF0IjoxNjk5NDQ5ODIyLCJleHAiOjE2OTk0NTA0MjJ9.waRFgaCtJq6jUHGbZdBUyTgwF5xxMynUh0xrdTH94M4",       
        "win": "1",
        "sixWin": "0",
        "sixCount": "2",
        "fourCount": "2",
        "timeCreated": datetime.datetime.now().strftime("%H:%M:%S")
    }


    # Make a POST request to update the 'timeCreated' field
    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 200:
        #print("POST request successful. 'timeCreated' updated to current time.")
        #print("Response content:", response.text)
        # Parse the JSON response
        data = response.json()
        
        # Extract and print totalScore and totalPlayCount
        total_score = data.get('totalScore', 'N/A')
        total_play_count = data.get('totalPlayCount', 'N/A')
        
        print("Total Score:", total_score, "| Total Play Count:", total_play_count)
    else:
        print(f"POST request failed with status code: {response.status_code}")
        print("Response content:", response.text)

    # Wait for 50 seconds before making the next request
    time.sleep(30)


print("Script has finished running for 3 hours.")