import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://dolarhoje.com/')
except urllib.error.URLError:
    print('O site Dolar Hoje não está acessível no momento.')
else:
    print('Consegui acessar o site Dolar Hoje com sucesso!')
    print(site.read())