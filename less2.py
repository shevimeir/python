import json

def read_write(**kwargs):
    with open('file.json', 'a') as f:
       json.dump(kwargs,f)
    with open('file.json', 'r') as g:
        data=json.load(g)
        print(data)

my_dict = {
    "shevi": "meir",
    "miri": "bloch"
}

read_write(**my_dict)
