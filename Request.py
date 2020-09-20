# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://run.mocky.io/v3/9a266a44-dd8c-4b3d-987c-ee4b1205b4f0"
  
# location given here 
location = "delhi technological university"
  
# sending get request and saving the response as response object 
response = requests.get(url = URL) 

print(response)
print(response.text)
# extracting data in json format 
#data = r.json() 