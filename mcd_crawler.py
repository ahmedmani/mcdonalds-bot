import requests, os, json, code, string, random



class Mcd_crawler:

	def __init__(self):
		self.fetch_sensor_tokens()
		self.header = {'x-acf-sensor-data': self.tokens[0], 'mcd-clientid': '8cGckR5wPgQnFBc9deVhJ2vT94WhMBRL', 'authorization': 'Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIiwia2lkIjoiMjAxNi0wOS0xOSJ9.JoZdna5Vmb6TPYK2Xh0hJ5NXUggTvTbuv7eMZh8k00bsKw-opgiOeQ.RlxEhuIesUDDYjtzOQ3k4g.zdtL5Y4A_YQylonHImlXRhCg5CpbSiptRicGhYLhbOzmWUZbUKqjZvAs0BxqFNRLqpKw803-ZUQ-oXqSywFUlVhjCTQwqM5VuaA5-vkNMehZtz4RhpaRURthylJr-4MtDVy1bIyXxZ8OM0AxVwlV8m3-IGVUNlumLdFkVRFtNiQ_orplN59FnjK4EKobWwr5xNEO48bcatdFWIW3nh2bWyANlTGOSgqcvwrv4VCR8-CjTdNNREh_9CfFabRV1wx5jDdWpw688A2Rw4lWn67Fq47jPMyQPESUeDJ8ObV8Y5yKY3q7RpUX0Z4dY3tHgbvZbAvN50UYK7fx7eMFlJTr3kBAz5hXUD6U7gK2rJosbTTKBeU6GmJu717nKF4sPaFJrYDNyUVN2z5B9drv_3jEdjTeQRthIyiypgawQKrKlKALLs5fKtXxazI1nKWlWuV-_UO636XZNPXjPXBntwHoPWuFZ12W8dn-YSsGDWg-DDPDl5EO7GSfbvHQvv0-AcjZ0QRddEYF8_c95IzBCp16ED-7u74k0yXKlozNPpOiWSskbCQUtcSan4G-2TiGZ4z2j7rVCIQtORJMVF77oJ-RotMGSyshcOjvnhCrEFyiXzbwhKYSDwHqXC0ut_DMa0RDBYQeG7N77l8IGdzz1NroWO4zuzW1ocSqsL21gnoCucum0XGqvaGRYn-RjTl8DcVXNbo1k7Fac1xVpfl8a-if4JNnO9qXeKxHi5PkoKwLPlM.YyKcpOU2SiW1tBO59oHsog', 'cache-control': 'true', 'accept-charset': 'UTF-8', 'user-agent': 'MCDSDK/23.0.15 (Android; 30; en-US) GMA/7.5.0', 'accept-language': 'en-US', 'mcd-sourceapp': 'GMA', 'mcd-uuid': '0bae1f6a-d383-45f4-8041-f8ea9ef3dbac', 'mcd-marketid': 'US', 'tracestate': '@nr=0-2-734056-436998460-8a9b1fd2396d4753----1659277394920', 'traceparent': '00-aa0782f185f94c21b2f4b7f68fb7b9b9-8a9b1fd2396d4753-00', 'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjczNDA1NiIsImQuYXAiOiI0MzY5OTg0NjAiLCJkLnRyIjoiYWEwNzgyZjE4NWY5NGMyMWIyZjRiN2Y2OGZiN2I5YjkiLCJkLmlkIjoiOGE5YjFmZDIzOTZkNDc1MyIsImQudGkiOjE2NTkyNzczOTQ5MjB9fQ==', 'accept-encoding': 'gzip', 'x-newrelic-id': 'UwUDUVNVGwcDUlhbDwUBVg=='}
		# holds Latitude and Longitude coordinates of various Us states
		self.cords =  [{"lat": "42.856842", "log":	"-70.963440"}, {"lat": "38.981544", "log":	"-77.010674"}, {"lat": "38.363350", "log":	"-75.605919"}, {"lat": "38.186886", "log":	"-76.434166"}, {"lat": "39.086437", "log":	"-77.161263"}, {"lat": "39.407833", "log":	"-79.409386"}, {"lat": "39.644207", "log":	"-77.731430"}, {"lat": "38.998318", "log":	"-76.896332"}, {"lat": "39.703602", "log":	"-77.328995"}, {"lat": "39.609505", "log":	"-75.839920"}, {"lat": "38.776402", "log":	"-76.082825"}, {"lat": "39.649109", "log":	"-78.769714"}, {"lat": "38.563461", "log":	"-76.085251"}, {"lat": "39.514877", "log":	"-76.174110"}, {"lat": "43.159996", "log":	"-70.662003"}, {"lat": "43.595406", "log":	"-70.352226"}, {"lat": "44.553761", "log":	"-70.568275"}, {"lat": "46.680672", "log":	"-68.023521"}, {"lat": "43.680031", "log":	"-70.310425"}, {"lat": "44.713200", "log":	"-67.469025"}, {"lat": "44.858288", "log":	"-66.988403"}, {"lat": "44.101902", "log":	"-70.217110"}, {"lat": "46.126865", "log":	"-67.849777"}, {"lat": "44.230553", "log":	"-69.779633"}, {"lat": "47.255791", "log":	"-68.594620"}, {"lat": "44.670052", "log":	"-70.159668"}, {"lat": "44.906910", "log":	"-66.996201"}, {"lat": "44.389732", "log":	"-68.804054"}, {"lat": "45.188042", "log":	"-67.282753"}, {"lat": "43.909313", "log":	"-69.987274"}]
		# holds the restaurant ids
		self.rest_ids = []
		try:
			fp = open(os.path.join(os.path.expanduser('~')) + "/Onedrive/Bureau/mcd_data/restaurant_ids.txt", "r")
			self.rest_ids = json.loads(fp.read())
		except:
			self.fetch_restaurants()
	
		self.fetch_rest_data()

	def fetch_sensor_tokens(self):
		fp = open(os.path.join(os.path.expanduser('~')) + "/Onedrive/Bureau/akamai_tokens.txt", "r")
		self.tokens = fp.read().split('\n')


	def fetch_auth_token(self):
		x = requests.post("https://us-prod.api.mcd.com/v1/security/auth/token", headers={'mcd-clientid': ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)), 'authorization': 'Basic OGNHY2tSNXdQZ1FuRkJjOWRlVmhKMnZUOTRXaE1CUkw6WW00clZ5cXBxTnBDcG1yZFBHSmF0UnJCTUhoSmdyMjY=', 'mcd-clientsecret': 'Ym4rVyqpqNpCpmrdPGJatRrBMHhJgr26', 'cache-control': 'true', 'accept-charset': 'UTF-8', 'user-agent': 'MCDSDK/23.0.15 (Android; 30; en-US) GMA/7.5.0', 'accept-language': 'en-US', 'mcd-sourceapp': 'GMA', 'mcd-uuid': '15ba0e18-599b-481d-a27d-cbe67f94c633', 'mcd-marketid': 'US', 'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjczNDA1NiIsImQuYXAiOiIl1zY5OTg0NjAiLCJkLnRyIjoiOTZiOTMyYzg2MjdlNGU4ZWIyZThkZTMzMzI3NzZlZTUiLCJkLmlkIjoiOTgwZGVmMzJiYWU3NDNiZSIsImQudGkiOjE2NTkyMTM2NzA2NjR9fQ==', 'traceparent': '00-96b932c8627e4e8eb2e8de3332776ee5-980def32bae743be-00', 'tracestate': '@nr=0-2-734056-436998460-980def32bae743be----1659213670664', 'accept-encoding': 'gzip', 'x-newrelic-id': 'UwUDUVNVGwcDUlhbDwUBVg=='}, data={"grantType": "client_credentials"})
		try:
			token = json.loads(x.text)["response"]["token"]
		except:
			print("error fetching auth token")
			code.interact(local=locals())
		else:
			return token
	
	def fetch_restaurants(self):
		total_rests = 0
		for i in self.cords:

			try:
				x = requests.get(f"https://us-prod.api.mcd.com/exp/v1/restaurant/location?distance=27&filter=summary&latitude={i['lat']}&longitude={i['log']}&pageSize=1000", headers=self.header)
				try:
					data = json.loads(x.text)
					total_rests += len(data["response"]["restaurants"])
					for j in data["response"]["restaurants"]:
						self.rest_ids.append({"name": j["name"], "id": j["nationalStoreNumber"]})
					print(f"total restaurants found : {total_rests}")
				except:
					if 'message' in data["status"].keys():
						if data["status"]["message"] == "JWT Token is expired":
							self.header["authorization"] = "Bearer " + str(self.fetch_auth_token())
			except:
				code.interact(local=locals())
		
		fp = open(os.path.join(os.path.expanduser('~')) + "/Onedrive/Bureau/mcd_data/restaurant_ids.txt", "w+")
		fp.write(json.dumps(self.rest_ids))
		fp.close()

	def fetch_rest_data(self):
		print("scraping data")
		j = 0
		try:
			for i in self.rest_ids:
				if os.path.isfile(os.path.join(os.path.expanduser('~')) + f"/Onedrive/Bureau/mcd_data/{i['id']}.txt"):
					print("file already exists moving on")
					continue

				try:
					x = requests.get(f"https://us-prod.api.mcd.com/exp/v1/menu/catalog/US/{i['id']}?filter=summary", headers=self.header, timeout=10)
				except Exception as ex:
					print(ex)
					j += 1
					print("timeout occured changing token: n" + str(j))
					if j >= len(self.tokens):
						print("tokens ran out")
						code.interact(local=locals())
					self.header['x-acf-sensor-data'] = self.tokens[j]
					# self.header["authorization"] = "Bearer " + str(self.fetch_auth_token())

				else:
					print("request finished")	

					data = json.loads(x.text)
					# code.interact(local=locals())

					if x.status_code == 401:
						print("error fetching data")
						print(x.text)
						if 'message' in data["status"].keys():
								if data["status"]["message"] == "JWT Token is expired":
									print("auth token no longer valid")
									self.header["authorization"] = "Bearer " + str(self.fetch_auth_token())
								if data["status"]["message"] == " Access Denied for Current Region.":
									print("ip blocked")
					else:
						print(f"file created with restaurant id: {i['id']}")
						fp = open(os.path.join(os.path.expanduser('~')) + f"/Onedrive/Bureau/mcd_data/{i['id']}.txt", "w+")
						fp.write(x.text)
						fp.close()

		except Exception as ex:
			print(ex)
			code.interact(local=locals())

		print("scraping finished")
		code.interact(local=locals())




Mcd_crawler()