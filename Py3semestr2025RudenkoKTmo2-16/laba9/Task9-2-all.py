import requests
from datetime import datetime

# https://oauth.vk.com/blank.html#access_token=vk1.a.O-di9bA4_xeXd7lm1MNwbnID1t-Iy7QSL5sCg_iZ75jtQZrWxx_6QoMeX1q3WE4j8IzDN2sgQAPJJ8JN2MI53J90IAYT-Bv_YAsUYeLhmXANl4axVDbdU_9QmdL5dVe0H9Abm6ES7GfNLxI4lWVn0Cpp5DgmaevgyNbhoR3elb9HRYMXe0iwATRw0xHDROrg6iQ8xySz7_AajddD9rQNiA&expires_in=0&user_id=122299142&email=kos.rudenko2014@yandex.ru
TOKEN = "vk1.a.O-di9bA4_xeXd7lm1MNwbnID1t-Iy7QSL5sCg_iZ75jtQZrWxx_6QoMeX1q3WE4j8IzDN2sgQAPJJ8JN2MI53J90IAYT-Bv_YAsUYeLhmXANl4axVDbdU_9QmdL5dVe0H9Abm6ES7GfNLxI4lWVn0Cpp5DgmaevgyNbhoR3elb9HRYMXe0iwATRw0xHDROrg6iQ8xySz7_AajddD9rQNiA"  # user token или service token
API_VERSION = "5.199"

# Пост: vk.com/wall122299142_1675
# https://vk.com/wall122299142_1675
OWNER_ID = 122299142
POST_ID = 1675


def get_likers(owner_id, post_id):
    users = []
    offset = 0

    while True:
        params = {
            "type": "post",
            "owner_id": owner_id,
            "item_id": post_id,
            "access_token": TOKEN,
            "v": API_VERSION,
            "count": 1000,
            "offset": offset
        }
        r = requests.get("https://api.vk.com/method/likes.getList", params=params).json()

        items = r.get("response", {}).get("items", [])
        users.extend(items)

        if len(items) < 1000:
            break

        offset += 1000

    return users


def get_users_info(user_ids):
    info = {}
    ids = ",".join(map(str, user_ids))

    params = {
        "user_ids": ids,
        "fields": "bdate,sex",
        "access_token": TOKEN,
        "v": API_VERSION
    }

    r = requests.get("https://api.vk.com/method/users.get", params=params).json()

    for user in r.get("response", []):
        info[user["id"]] = {
            "sex": user.get("sex", 0),
            "bdate": user.get("bdate", None)
        }
    return info


def calc_age(bdate):
    if not bdate:
        return None

    parts = bdate.split(".")
    if len(parts) != 3:
        return None  # нет года → возраст определить нельзя

    day, month, year = map(int, parts)
    today = datetime.now()

    age = today.year - year - (
            (today.month, today.day) < (month, day)
    )
    return age


def get_age_group(age):
    if age is None:
        return "unknown"
    if age <= 18:
        return "0-18"
    if 19 <= age <= 35:
        return "19-35"
    if 36 <= age <= 50:
        return "36-50"
    return "> 50"


def get_sex_group(code):
    """VK sex: 1 — female (женский), 2 — male (мужской), 0 — unknown (неизвестный)"""
    if code == 1:
        return "female"
    if code == 2:
        return "male"
    return "unknown"


likers = get_likers(OWNER_ID, POST_ID)
users_info = get_users_info(likers)

stats = {
    "post_id": POST_ID,
    "age": {"0-18": 0, "19-35": 0, "36-50": 0, ">50": 0, "unknown": 0},
    "sex": {"male": 0, "female": 0, "unknown": 0}
}

for user_id, data in users_info.items():
    sex = get_sex_group(data["sex"])
    stats["sex"][sex] += 1

    age = calc_age(data["bdate"])
    age_group = get_age_group(age)
    stats["age"][age_group] += 1

print(stats)


# C:\Users\korudenko\AppData\Local\Programs\Python\Python312\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba9\Task9-2-all.py
# {'post_id': 1675, 'age': {'0-18': 0, '19-35': 5, '36-50': 1, '>50': 0, 'unknown': 4}, 'sex': {'male': 7, 'female': 3, 'unknown': 0}}
#
# Process finished with exit code 0
