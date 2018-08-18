import requests, hashlib, os, random

h = hashlib.md5()
h.update(os.urandom(16))
user_id = h.hexdigest()

data = {
    'frequency' : {},
    'theme_start' : '#cafebabe',
    'theme_end' : '#deadbeef',
    'user_id' : user_id
}
for i in range(100):
    r = ''.join(random.sample([chr(i) for i in range(33, 127)], 10))
    if r not in data['frequency']:
        data['frequency'][r] = random.randint(1, 10)

print('[*] JSON : ' + str(data))
print(requests.get('http://localhost:5000/wordcloud', json=data).text)
