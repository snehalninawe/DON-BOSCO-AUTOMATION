
import os
import pytest
import requests
from dotenv import load_dotenv

# Read .env from the main automation folder
automation_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

env_path = os.path.join(automation_path, ".env")
load_dotenv(env_path)

BASE_URL = "https://devops.evolutionco.in/nextgen/api"


@pytest.fixture
def get_auth_token():

    def login(staff_number):
        staff_users = {
            1: ("STAFF_A_EMAIL", "STAFF_A_PASSWORD"),
            2: ("STAFF_B_EMAIL", "STAFF_B_PASSWORD"),
            # 3: ("STAFF_C_EMAIL", "STAFF_C_PASSWORD"),
        }

        if staff_number not in staff_users:
            raise ValueError(f"Staff {staff_number} is not configured")

        email_key, password_key = staff_users[staff_number]

        email = os.getenv(email_key)
        password = os.getenv(password_key)

        if not email or not password:
            raise ValueError(
                f"Credentials for Staff {staff_number} are missing from .env"
            )

        url = f"{BASE_URL}/v2/login"

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(url, json=payload, timeout=30)

        assert response.status_code == 200, (
            f"Login failed for Staff {staff_number}. "
            f"Status: {response.status_code}"
        )

        data = response.json()
        token = data["data"]["accessToken"]

        assert token, "Access token was not received"

        return token


    return login





def test_staff_credentials_loaded():
    assert os.getenv("STAFF_A_EMAIL"), "Staff A email missing from .env"
    assert os.getenv("STAFF_A_PASSWORD"), "Staff A password missing from .env"

    assert os.getenv("STAFF_B_EMAIL"), "Staff B email missing from .env"
    assert os.getenv("STAFF_B_PASSWORD"), "Staff B password missing from .env"

    print("Both staff credentials loaded successfully.")


def test_staff_a_login(get_auth_token):
    token = get_auth_token(1)
    assert token, "Staff A login token was not received"
    print("Staff A login successful")


def test_staff_b_login(get_auth_token):
    token = get_auth_token(2)
    assert token, "Staff B login token was not received"
    print("Staff B login successful")
