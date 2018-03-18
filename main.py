import requests

# examplePayload = {
#    'issue': {
#      'key': "BITE-1096"
#    },
#    'activity': 'gitCommit',
#    'feedback': [
#      {
#        'text': "Excessive backlog/Overloaded queue/Burnout potential",
#        'timeline': [
#          ["2017-04-21T14:54:00.000Z", "2017-04-25T14:54:00.000Z"],
#          ["2017-04-28T14:54:00.000Z"],
#        ]
#      }
#    ]
# }

url = 'https://sleepy-beach-90505.herokuapp.com/nudges'

def deliverNudge(payload):
  global url
  headers = {
    'Activity-Type': 'issuesDevstreamActivity'
  }
  r = requests.post(url, json=payload, headers=headers)
  print(r.status_code)
  return

# deliverNudge(examplePayload)