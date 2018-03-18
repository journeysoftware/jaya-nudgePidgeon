import requests

url = 'https://sleepy-beach-90505.herokuapp.com/nudges'

headers = {
    'Activity-Type': 'issuesDevstreamActivity'
}

# Example payload

payload = {
   'issue': {
     'key': "BITE-1096"
   },
   'activity': 'gitCommit',
   'feedback': [
     {
       'text': "Excessive backlog/Overloaded queue/Burnout potential",
       'timeline': [
         ["2017-04-21T14:54:00.000Z", "2017-04-25T14:54:00.000Z"],
         ["2017-04-28T14:54:00.000Z"],
       ]
     }
   ]
}

r = requests.post(url, json=payload, headers=headers)

print(r.status_code)