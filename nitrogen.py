import requests
import concurrent.futures
import json
import hashlib
import uuid

def generate_id():
    return hashlib.sha256(uuid.uuid4().bytes).hexdigest()

generated = []

class Discord:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'})

    def jwtToken(self):
        try:
            r = self.session.post('https://api.discord.gx.games/v1/direct-fulfillment', json={"partnerUserId":generate_id()})
            return r.json()['token']
        except:
            pass

    def nitro(self):
        token = self.jwtToken()
        return f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'

if __name__ == '__main__':
    dc = Discord()

    howmuch = int(input('How many codes do you want to generate? '))

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for _ in range(howmuch):
            future = executor.submit(dc.nitro)
            generated.append(future.result())

    with open('generated.json', 'w') as f:
        json.dump(generated, f, indent=4)
