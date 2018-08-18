import requests
data = {
    'image_url' : 'http://www.jnjl.kr/data/file/s1_1/thumb_view/763816310_5n37Lmwa_C1A6B8F1_BEF8C0BD.png'
}
print('[*] JSON : ' + str(data))
print(requests.get('http://localhost:5000', json=data).text)
