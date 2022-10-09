from mitmproxy import http






class HTTPEvents:
	def request(self, flow):
		url_request = str(flow.request.url)
		if "us-prod.api.mcd.com/exp/v1/restaurant" in url_request:
			flow.response = http.HTTPResponse.make(401,
						{
						  "status": {
						    "code": 40000,
						    "type": "ValidationException",
						    "message": "JWT Token is expired",
						    "errors": [
						      {
						        "code": 40006,
						        "type": "JWTTokenExpired",
						        "message": "User authentication failed",
						        "property": "Authentication",
						        "path": "GET/restaurant/location",
						        "service": "LambdaAuthorizerService"
						      }
						    ]
						  }
						},
						{'Content-Type': 'application/json', 'Content-Length': '385', 'x-amzn-RequestId': 'a334fafc-3bdd-4649-880f-a91152aad29e', 'x-amzn-Remapped-x-amzn-RequestId': '01b698dd-b190-40bd-a9ed-210abff82f35', 'x-amzn-Remapped-Content-Length': '385', 'x-amzn-ErrorType': 'AccessDeniedException', 'x-amzn-Remapped-Connection': 'keep-alive', 'x-amz-apigw-id': 'WGSGEE62IAMFoPQ=', 'x-amzn-Remapped-Date': 'Sat, 30 Jul 2022 20:39:15 GMT', 'Date': 'Sat, 30 Jul 2022 20:39:15 GMT', 'Connection': 'keep-alive'}
						)