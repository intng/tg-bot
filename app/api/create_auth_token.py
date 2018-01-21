import requests, os
domain = os.getenv('domain.accounts')

def create(tg_id):
    r = requests.post(f'http://{domain}/api/v1/logins/create_auth_token', json={'tg_id': tg_id})
    r = r.json()
    return r