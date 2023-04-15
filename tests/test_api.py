import requests


def test_make_summary_api(check_openai_tests):
    response = requests.post(
        "http://localhost:8080/api?video_url=https://www.youtube.com/watch?v=x7KedT6uvus",
    )
    assert "shields" in response.text.lower()


def test_make_summary_api_video_that_needs_2_api_calls(check_openai_tests):
    url = "https://www.youtube.com/watch?v=FrMRyXtiJkc"
    response = requests.post(f"http://localhost:8080/api?video_url={url}")
    assert "vim" in response.text.lower()


def test_make_summary_api_video_that_needs_tldr(check_openai_tests):
    url = "https://www.youtube.com/watch?v=pKpnAX612k0"
    response = requests.post(f"http://localhost:8080/api?video_url={url}")
    assert "database" in response.text.lower()
