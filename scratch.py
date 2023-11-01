from urllib.parse import urlparse
import tldextract
import dns.resolver
from dns.rdataclass import RdataClass
from dns.rdatatype import RdataType
import requests
from urllib.parse import quote

# url_string = 'http://www.bbc.co.uk'
# url_string = 'http://www.amazon.com'
# url_string = 'http://prime.amazon.com/cart'

# url = urlparse(url_string)
# if url.scheme == 'http' or url.scheme == 'https':
#     n = url.netloc.split(':')
#     query = n[0].split('.')[-2] + "." + n[0].split('.')[-1]
#     print(query)

# ext = tldextract.extract(url_string)
# print(ext)
# print(ext.registered_domain)


# request = 'yahoo.com'
# if request:
#     domain = request
#     print(domain)
#     try:
#         result = dns.resolver.query(domain, 'A')
#         print(result.__dict__)
#     except Exception as e:
#         print(e)
#         result = ''
#     for ipval in result:
#         a_record = ipval
#         print("maltego.IPv4Address", a_record)

# test_var = None
# test_var_2 = 'this works' if test_var == 'x' else 'this still works'
# print(test_var_2)
#
# test_dict = {'key': 'value'}
# test_val = test_dict.get('not_a_key')
# print(test_val)

# api_key = 'cdcc3997-6451-4b97-893f-66b35ab5fce6'
#
# domain1 = 'org.duckdns.org'
# domain2 = 'cnn.com'
#
# result1 = requests.get('https://api.hyas.com/dynamicdns/v1/ext/search?domain=' + quote(domain1),
#                        headers={'x-api-key': api_key})
# result2 = requests.get('https://api.hyas.com/dynamicdns/v1/ext/search?domain=' + quote(domain2),
#                        headers={'x-api-key': api_key})
#
# print(result1.text)
# print(result2.text)


class TestClass():
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        print(vars(self))

test = TestClass()

