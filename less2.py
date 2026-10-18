import json
def count_words(file):
    with open(file,'r') as f:
     data=f.read()
    words=data.split()
    return len(words)


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
print(count_words('new.txt'))
read_write(**my_dict)
