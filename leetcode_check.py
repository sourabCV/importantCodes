import RPi.GPIO as GPIO
import requests
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
api_code_url = "https://alfa-leetcode-api.onrender.com/daily"
api_submission_check_url = "https://alfa-leetcode-api.onrender.com/maitysourab/acSubmission?limit=1"
headers = {
    "Content-Type": "application/json"
}


def red_color():
    GPIO.setup(2, GPIO.LOW)
    GPIO.setup(3, GPIO.LOW)
    GPIO.setup(4, GPIO.LOW)
    time.sleep(1)
    print("Red")
    GPIO.setup(2, GPIO.HIGH)
    GPIO.setup(3, GPIO.HIGH)
    GPIO.setup(4, GPIO.HIGH)


def green_color():
    GPIO.setup(2, GPIO.LOW)
    GPIO.setup(3, GPIO.LOW)
    GPIO.setup(4, GPIO.LOW)
    time.sleep(1)
    print("Green")
    #GPIO.setup(3, GPIO.HIGH)
    #GPIO.setup(4, GPIO.HIGH)
    GPIO.setup(2, GPIO.HIGH)

def blue_color():
    GPIO.setup(2, GPIO.LOW)
    GPIO.setup(3, GPIO.LOW)
    GPIO.setup(4, GPIO.LOW)
    time.sleep(1)
    print("Blue")
    GPIO.setup(4, GPIO.HIGH)
    GPIO.setup(2, GPIO.HIGH)


response = requests.get(api_code_url, headers=headers)

if response.status_code == 200:
    # Parse the JSON response
    daily_challenge = response.json()
    daily_challenge_code_title = daily_challenge["questionTitle"]
else:
    print(
        f"Failed to retrieve daily challenge. Status code: {response.status_code}")
    print(response.text)
    blue_color()

print(daily_challenge_code_title)
while True:
    response = requests.get(api_submission_check_url, headers=headers)
    if response.status_code == 200:
        # Parse the JSON response
        all_submission = response.json()
        last_submission = all_submission["submission"][0]["title"]
        if last_submission == daily_challenge_code_title:
            green_color()
            print("today task complete")
            break
        else:
            red_color()
    else:
        print(
            f"Failed to retrieve daily challenge. Status code: {response.status_code}")
        print(response.text)
        blue_color()
    time.sleep(60)
