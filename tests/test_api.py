import requests


def test_make_summary_api():
    response = requests.get(
        "http://localhost:8080/api?video_url=https://www.youtube.com/watch?v=x7KedT6uvus",
    )
    assert "software" in response.text and "Germany" in response.text


def test_make_summary_api_2():
    response = requests.post(
        "http://localhost:8080/api2?video_url=https://www.youtube.com/watch?v=x7KedT6uvus",
    )
    assert response.text == "x7KedT6uvus"
