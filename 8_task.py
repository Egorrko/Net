import requests
import json
import re
import time

key = "&access_token="
v = "&v=5.103"
link = "https://api.vk.com/method/"
friends_list = "friends.get?count=10000&user_id="
url_to_id = "utils.resolveScreenName?screen_name="
users_get = "users.get?fields=sex,bdate,city,country&user_ids="
count_lines = 300

def get_id(url):
    url = re.search(r"vk\.com\/(\w+)",url)
    if(not url):
        return False
    user = url.group(1)
    response = requests.get(link + url_to_id + user + key + v)
    j = json.loads(response.text)
    if("response" in j):
        if("object_id" in j["response"]):
            return j["response"]["object_id"]
        else:
            return False
    else:
        return False

def get_friends(uid):
    response = requests.get(link + friends_list + str(uid) + key + v)
    j = json.loads(response.text)
    if("response" in j):
        if("items" in j["response"]):
            return j["response"]["items"]

def print_info(friends):
    friends = [str(i) for i in friends]
    friends = [friends[i:i + count_lines] for i in range(0, len(friends), count_lines)]
    for part in friends:
        l = ",".join(part)
        response = requests.get(link+users_get+l+key+v) 
        j = json.loads(response.text)
        if("response" in j):
            for i in j["response"]:
                first = i["first_name"]
                last = i["last_name"]
                u_id = i["id"]
                bdate = ""
                country = ""
                city = ""
                if ("bdate" in i):
                    bdate = i["bdate"]
                if ("country" in i):
                    country = i["country"]["title"]
                if ("city" in i):
                    city = i["city"]["title"]
                result = "{0:15} {1:20} {2:15} {3:15} {4:20} vk.com/{5}".format(first, last, bdate, country, city, u_id)
                print(result)


if __name__ == "__main__":
    key += input("Введите сервисный ключ: ")
    url = input("Введите ссылку на пользователя: ")
    user_id = get_id(url)
    if(not user_id):
        print("Неверная ссылка на пользователя")
        exit(0)
    friends = get_friends(user_id)
    print_info(friends)