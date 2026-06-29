import requests
def test_get_user():
    response = requests.get("https://api.github.com/users/ltmq420")
    assert response.status_code == 200
    assert response.json()["login"] == "ltmq420"
    print("✅ Тест API пройден!")
if __name__ == "__main__":
    test_get_user()