import random
import json
import sys
import collections

import requests

from settings import PROPOSER_URLS
    
    
failures = collections.defaultdict(int)


def sync(range):
    for i in range:
        url = random.choice(PROPOSER_URLS)
        response = requests.post(url + "/",
            data=json.dumps({
                "key": "foo", 
                "value": "Hello world!"
            }), headers={'Content-Type': 'application/json'})
        print(response.text)
        if response.status_code == 200:
            sys.stdout.write('.')
        else:
            failures[url] += 1
            sys.stdout.write('x')
        sys.stdout.flush()
    print("Failures", failures)

sync(range(20))
print("Failures", failures)

