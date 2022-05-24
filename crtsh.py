#!/usr/bin/env python3

import requests
import re
import cli

def domain_search(domain: str) -> list:
    print(f'[*] Searching crt.sh for subdomains of {domain}.')
    request = requests.get(f'https://crt.sh/?q={domain}')

    if request.status_code != 200:
        print(f'Request failed with status code {request.status_code}.')
        quit()

    subdomains = re.findall(f'\w+\.{domain}', request.text)
    non_repeating_subdomains = list(set(subdomains))

    return non_repeating_subdomains

def print_subdomains(subdomains: list, domain: str):
    if len(subdomains) == 0:
        print(f'No subdomains were found for {domain}.')
        return

    print(f'[*] Found {len(subdomains)} unique subdomains of {domain}.\n')
    for subdomain in subdomains:
        print(subdomain)

def save_subdomains_to_file(output_file: str, subdomains: list):
    if output_file is None or len(subdomains) == 0:
        return

    with open(str(output_file), 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')
    print(f'\n[*] Results saved in {output_file} file.')

def main(domain: str, output_file: str):
    subdomains = domain_search(domain)
    print_subdomains(subdomains, domain)
    save_subdomains_to_file(output_file, subdomains)

if __name__ == '__main__':
    args = cli.parser.parse_args()
    main(args.domain, args.output_file)
