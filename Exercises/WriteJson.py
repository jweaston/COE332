import json

data = {}
data['class'] = 'COE332'
data['title'] = 'Software ENgineering and Design'
data['subjects'] = []
data['subjects'].append( {'week': 1, 'topic': ['linux', 'python']} )
data['subjects'].append( {'week': 2, 'topic': ['json', 'unittest', 'git']} )

with open('class.json', 'w') as out:
    json.dump(data, out, indent=4)