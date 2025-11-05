import random
import string
from datetime import date, timedelta


def random_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_email():
    return random_name() + '@gmail.com'

def random_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(10))

def random_birth_date(start_year=1990, end_year=2005):
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)

    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d %b %Y")


SUBJECT_LIST = ["Maths", "Physics", "Chemistry", "Biology", "English", "History", "Economics"]

def random_subject():
    return random.choice(SUBJECT_LIST)

STATE_CITY = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Lucknow", "Agra"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}

def random_state_city():
    state = random.choice(list(STATE_CITY.keys()))
    city = random.choice(STATE_CITY[state])
    return state, city