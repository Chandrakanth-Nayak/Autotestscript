
from typing import ItemsView
import requests
import json

#first time editing using nano command
# Define the URL and headers
url = "https://develop.snipeitapp.com/api/v1/hardware?limit=2&offset=0&sort=created_at&order=desc"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTU2MDc0MjVmYjM5YTEwYjFjNTZlZTAxMTBmZDk4ZjQ0ZjVjODMzYjcxZWVhYjZlNDk1NGMwOThlY2YzMzU2MDY4Mzg4MmFhMDMzOTAzNzciLCJpYXQiOjE2MzI4NjU5MTgsIm5iZiI6MTYzMjg2NTkxOCwiZXhwIjoyMjY0MDIxNTE4LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.LgGVzyH67IRhXvccHd4j2Dn6TDuIuQTBoo30_wD9jPehy8v_h0xBmE1-dOUBRJyeJOI8B4gwPeALsWaudpGj9Lb5qWAtKV7eYtH9IYQKoLF_iHgOGXnAUcNwID6zBU_YyLNSI6gp8zjutLJias33CBLsHy5ZRNpxVibVrZouJ_HjYuIYbtZyLus-KFFeibtZoPiTWOeHhQFD37MR6ifx4dBqT37fN-xDS99mONtrkAplEIou5aSO1oZ4IlJIPCUyA1lixPgpn1YU7PxiBDZp1teeugD0WEmrAqxRS2I0bH4qPsuTsrVXS_lo87Sf5LBGLW7lGHKqyYH6J47OZOM0K-SrxLKtE1ww8jyLBgnnxH0lJHRLCBiwUnL5ZGTUmiOysUA-wSJ6s78o8Pc-ec6bpBvAlelHdiQ-wslE7gzEJDptbejFg-75b_CEwgJYh7J2D18ul6Qu5EFCUEgt033mm04dgVk0isWTDt6EW5ZvTo5Qhr1LY0YnEIXCTqIRN-BSQjL55sZaCrtwR_21bnBGgniyI5MRDYblFawVmFKroeClCpSjBo9vi66akdD5hjpvx67RL3r33BZQhEXmPifUPNH5wP_U-IHGFUD99TJk2c1awF0RASveZRLSunbJb1x6hGAVUaIvQV4r2quWzXqYyKLph9kGTyJYrb6iJtH5smE"
}

# Make the request
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    # Load JSON data
    data = response.json()
    print(data)
    
#     total_count = data['total']
# print("Total count:", total_count)

# asset_tags = [item['asset_tag'] for item in data['rows']]
# print("Asset Tags:", asset_tags)

# model_names = [item['model']['name'] for item in data['rows']]
# print("Model Names:", model_names)

# purchase_costs = [item['purchase_cost'] for item in data['rows']]
# print("Purchase Costs:", purchase_costs)

# id_location_pairs = [(item['id'], item['location']['name']) for item in data['rows']]
# print("ID and Locations:", id_location_pairs)

# status_labels = [(item['id'], item['status_label']['name']) for item in data['rows']]
# print("Status Labels:", status_labels)

requestable_items = [item for item in data['rows'] if item['requestable']]
print("Requestable Items:", requestable_items)










    
    
