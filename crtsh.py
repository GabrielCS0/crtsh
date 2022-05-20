#!/usr/bin/env python3

import requests
import re
import cli

def domain_search(domain):
    request = requests.get(f'https://crt.sh/?q={domain}')

    if request.status_code != 200:
        print(f'Request failed with status code {request.status_code}.')
        quit()

    subdomains = re.findall(f'\w+\.{domain}', request.text)
    non_repeating_subdomains = list(set(subdomains))

    return non_repeating_subdomains

def print_subdomains(subdomains, domain):
    if len(subdomains) == 0:
        print(f'No subdomains were found for {domain}.')
        return

    print(f'[*] Found {len(subdomains)} unique subdomains of {domain}.\n')
    for subdomain in subdomains:
        print(subdomain)

def main(domain):
    print(f'[*] Searching crt.sh for subdomains of {domain}.')
    subdomains = domain_search(domain)
    return print_subdomains(subdomains, domain)

if __name__ == '__main__':
    args = cli.parser.parse_args()
    main(args.domain)
