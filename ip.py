import requests
def ip_geo(ip = "127.0.0.1"):
	try:
		response = requests.get(url = f'http://ip-api.com/json/{ip}').json()

		if response.get('status') != "fail":
			data = {
				'Айпи: ': response.get('query'),
				'Страна: ': response.get('country'),
				'Регион: ': response.get('regionName'),
				'Провайдер: ': response.get('isp'),
				'Город: ': response.get('city'),
				'Язык: ': response.get('countryCode'),
				'Широта: ': response.get('lat'),
				'Долгота: ': response.get('lon'),
				'Почт. Индекс: ': response.get('zip')
			}
			print("###########################")
			for k, v in data.items():
				print(f'{k} : {v}')
			print("###########################")
		else:
			return False

	except requests.exceptions.ConnectionError:
		print("Interneta Net")

while True:
	ip = input("IP: ")
	ip_geo(ip)
