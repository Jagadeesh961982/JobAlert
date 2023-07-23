import os
from flask import Flask, request, Response
import requests

app = Flask(__name__)


def gettingjoblist(data):
    jobs_wanted = {
        "Software Engineer", "Software Developer", "Go Full Stack Engineer",
        "Front End Engineer", "Full stack Developer", "Web Developer",
        "Junior Frontend Developer", "Backend Software Engineer"
    }
    required_details = {
        "company", "position", "location", "salary_min", "salary_max", "url"
    }
    res = []
    const = 0
    for i in data:
        const += 1
        if const == 1:
            continue
        else:
            if i["position"] in jobs_wanted:
                temp = {}
                for j in i:
                    if j in required_details:
                        temp[j] = i[j]
                res.append(temp)
    return res


@app.get("/")
def index():
    response = requests.get(
        'https://remoteok.com/api')
    if response.status_code == 200:
        data = response.json()
        list = gettingjoblist(data)
        for i in list:
            requests.get("https://api.telegram.org/bot" +
                         os.environ['Telegram_Token'] +
                         "/sendMessage?chat_id=" + str(os.environ['Chat_id']) +
                         "&text=" + str(i))
    return "ok"


app.run('0.0.0.0', 8080)
