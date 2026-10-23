import requests


def test_login():

    # Login API
    url = "https://devops.evolutionco.in/nextgen/api/v2/login"

    # Login data
    payload = {
        "email": "oliviadb@gmail.com",
        "password": "123456"
    }

    # Send POST request
    response = requests.post(
        url,
        json=payload
    )

    # Print response
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Verify status code
    assert response.status_code == 200

    # Get response data
    data = response.json()

    # Verify access token is present
    assert "accessToken" in data

    # Print token for checking
    print("Login successful")
    print("Access Token received:", bool(data["accessToken"]))