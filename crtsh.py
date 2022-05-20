#!/usr/bin/env python3

import requests
import re

domain = 'hackerone.com'
request = requests.get(f'https://crt.sh/?q={domain}')

if request.status_code != 200:
    print(f'Request failed with status code {request.status_code}.')
    quit()

subdomains = re.findall(f'\w+\.{domain}', request.text)
non_repeating_subdomains = list(set(subdomains))

if len(non_repeating_subdomains) == 0:
    print(f'No subdomains were found for {domain}.')
    quit()

print(f'[*] Found {len(non_repeating_subdomains)} unique subdomains of {domain}.\n')
for subdomain in non_repeating_subdomains:
    print(subdomain)
