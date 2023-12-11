import requests

api_url = 'http://127.0.0.1:5000/'
flat_data = {
    'name': 'lkhjkj Apartment',
    'price': 50000,
    'images': [
        'https://example.com/image1.jpg',
        'https://example.com/image2.jpg',
    ]
}

response = requests.post(api_url+"flat/1", json=flat_data)
# response = requests.get(api_url+"flats")

# print(f'Status Code: {response.status_code}')
# print('Headers:')
# print(response.headers)
# print('Content:')
print(response.text)
