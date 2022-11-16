from Generic_functions_modules import *

# import requests
# from requests.structures import CaseInsensitiveDict
#
# url = "https://www.w3schools.com/xml/tempconvert.asmx"
#
# headers = CaseInsensitiveDict()
# headers["Content-Type"] = "application/soap+xml"
#
# data = """
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
#       <Fahrenheit>75</Fahrenheit>
#     </FahrenheitToCelsius>
#   </soap12:Body>
# </soap12:Envelope>
# """
#
#
# resp = requests.post(url, headers=headers, data=data)
# print(resp.status_code)
#
# # SOAP request URL
# url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
#
# # POST request
# response = requests.request("POST", url, headers=headers, data=data)
#
# # prints the response
# print(response.text)
# print(response)


url = "https://www.w3schools.com/xml/tempconvert.asmx"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "text/xml; charset=utf-8"

data = """
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>75</Fahrenheit>
    </FahrenheitToCelsius>
  </soap12:Body>
</soap12:Envelope>
"""

resp = requests.post(url, headers=headers, data=data)
print(resp.text)



















