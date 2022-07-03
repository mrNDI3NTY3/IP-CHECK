import requests
def ip_geo(ip = "127.0.0.1"):
	try:
		response = requests.get(url = f'http://ip-api.com/json/{ip}').json()
		data = {
			'Айпи: ': response.get('query'),
			'Страна: ': response.get('country'),
			'Регион: ': response.get('regionName'),
			'Провайдер: ': response.get('isp'),
			'Город: ': response.get('city')
		}
		print("###########################")
		for k, v in data.items():
			print(f'{k} : {v}')
		print("###########################")
	except requests.exceptions.ConnectionError:
		print("Interneta Net")
while True:
	ip = input("IP: ")
	ip_geo(ip)
