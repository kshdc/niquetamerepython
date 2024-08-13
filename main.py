import requests
import threading
import time

proxy = {'https': ''}
vote_data = {
    "pv": "bb2d3b08-5920-11ef-9780-4d9a9e717338",
    "v": {"pollVotes": [{"id": "PbZqjJJMByN", "value": 1}], "voteType": "add", "token": ""},
    "h": False, "ht": False, "st": None, "token": None
}
def send_vote():
    try:
        response = requests.post('https://api.strawpoll.com/v3/polls/xVg71jGR6yr/vote', json=vote_data, proxies=proxy)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(e)
def worker():
    while True:
        send_vote()
        time.sleep(1)  
num_threads = 5
threads = [threading.Thread(target=worker) for _ in range(num_threads)]
for t in threads: t.start()
for t in threads: t.join()
