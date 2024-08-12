import subprocess
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import ssl
import time
import logging
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from requests.exceptions import SSLError, HTTPError, Timeout, ConnectionError

class TLSAdapter(HTTPAdapter):
    def __init__(self, tls_version=None, cert_file=None, key_file=None, ca_certs=None, *args, **kwargs):
        self.tls_version = tls_version
        self.cert_file = cert_file
        self.key_file = key_file
        self.ca_certs = ca_certs
        super(TLSAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = self._create_ssl_context()
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = self._create_ssl_context()
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).proxy_manager_for(*args, **kwargs)

    def _create_ssl_context(self):
        context = ssl.create_default_context(cafile=self.ca_certs)
        if self.cert_file and self.key_file:
            context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
        if self.tls_version:
            if self.tls_version == 'TLSv1.2':
                context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
            elif self.tls_version == 'TLSv1.3':
                context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
        context.set_ciphers('DEFAULT:@SECLEVEL=1')
        logging.debug(f"SSL context created with TLS version: {self.tls_version}, CA certs: {self.ca_certs}, Cert file: {self.cert_file}")
        return context

def validate_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])

def generate_self_signed_cert(cert_file='selfsigned.crt', key_file='selfsigned.key', password=None):
    key_command = ['openssl', 'genpkey', '-algorithm', 'RSA', '-out', key_file]
    
    if password:
        key_command += ['-aes256', '-pass', f'pass:{password}']
    
    cert_command = [
        'openssl', 'req', '-x509', '-new',
        '-key', key_file,
        '-out', cert_file,
        '-days', '365',
        '-subj', '/C=US/ST=State/L=City/O=Organization/OU=Department/CN=localhost'
    ]
    
    subprocess.run(key_command)
    subprocess.run(cert_command)

def fetch_webpage(url, headers=None, proxies=None, tls_versions=None, cert_file=None, key_file=None, ca_certs=None):
    session = requests.Session()
    for tls_version in tls_versions:
        session.mount('https://', TLSAdapter(tls_version=tls_version, cert_file=cert_file, key_file=key_file, ca_certs=ca_certs))
        try:
            response = session.get(url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            return response.text
        except SSLError as e:
            print(f"SSL Error with TLS {tls_version}: {e}")
        except HTTPError as e:
            if e.response.status_code == 403:
                print("Error 403: Forbidden. Access to the webpage is denied.")
            elif e.response.status_code == 404:
                print("Error 404: Not Found. The requested webpage could not be found.")
            elif e.response.status_code == 500:
                print("Error 500: Internal Server Error. The server encountered an error.")
            else:
                print(f"HTTP Error: {e.response.status_code}")
            return None
        except Timeout as e:
            print(f"Error: The request timed out. {e}")
            return None
        except ConnectionError as e:
            print(f"Error: Connection error occurred. {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return None
    print("Failed to connect using all TLS versions.")
    return None

def sanitize_keywords(keywords):
    sanitized = [keyword.strip().lower() for keyword in keywords if keyword.strip()]
    return list(set(sanitized))

def search_tags_by_keyword(soup, keywords):
    results = {}
    keyword_pattern = re.compile('|'.join(re.escape(keyword) for keyword in keywords), re.IGNORECASE)
    for element in soup.find_all(text=keyword_pattern):
        tag = element.parent.name
        if tag in results:
            results[tag].append(element)
        else:
            results[tag] = [element]
    return results

def print_results(results):
    for tag, elements in results.items():
        print(f"\nTag: <{tag}>")
        for element in elements:
            print(f" - {element}")

def main():
    url = input("Enter the URL of the webpage: ").strip()
    if not validate_url(url):
        print("Invalid URL. Please enter a properly formatted URL.")
        return
    
    keywords = input("Enter the keywords (comma-separated): ").split(',')
    sanitized_keywords = sanitize_keywords(keywords)
    
    if not sanitized_keywords:
        print("No valid keywords entered. Please provide at least one valid keyword.")
        return
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    proxies = {
        'http': 'http://3.136.29.104:3128',
        'https': 'https://3.136.29.104:3128',
    }
    
    tls_versions = ['TLSv1.3', 'TLSv1.2']
    
    # Automatically generate self-signed certificate and key if they don't exist
    cert_file = 'selfsigned.crt'
    key_file = 'selfsigned.key'
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        print("Generating self-signed certificate and key...")
        generate_self_signed_cert(cert_file=cert_file, key_file=key_file)

    ca_certs = None  # Path to your custom CA bundle, if needed
    
    html_content = fetch_webpage(url, headers=headers, proxies=proxies, tls_versions=tls_versions, cert_file=cert_file, key_file=key_file, ca_certs=ca_certs)

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        results = search_tags_by_keyword(soup, sanitized_keywords)
        
        if results:
            print_results(results)
        else:
            print("No matching elements found for the specified keywords.")

if __name__ == "__main__":
    main()
