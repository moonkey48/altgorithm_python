from  requests

url = 'https://www.safety.go.kr/openApi/'
dataName = '행정안전부_날씨정보'
apiKey = '5Z04AZAX18J0JB0R'
payloads = {'serviceKey': apiKey, 'returnType': 'JSON', 'pageNum': 1, 'numRowsPerPage': 5}
response = requests.get(url+dataName, params=payloads)