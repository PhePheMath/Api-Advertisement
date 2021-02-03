import requests

s = requests.Session()

r1 = s.get('http://localhost:8000/api-auth/login/')

csrf = r1.cookies['csrftoken']

context = {"username": 'phe', "password": 'django01',
           "csrfmiddlewaretoken": csrf}

r2 = s.post('http://localhost:8000/api-auth/login/', context, headers=context)

print(context)
