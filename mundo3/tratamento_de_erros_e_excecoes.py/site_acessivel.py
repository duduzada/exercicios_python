import urllib.request

try:
    site = urllib.request.urlopen('https://g1.com.br')
except urllib.error.URLError:
    print('O site G1 não está acessível no momento.')
else:
    print('Consegui acessar o site G1 com sucesso!')


""" import socket  ### MEU CÓDIGO ###

HOST = 'g1.com.br'
PORT = 443

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
except socket.error as erro:
    print(f"O site G1 não está acessível no momento\n {erro}")
else:
    print("Consegui acessar o site G1 com sucesso!")
    client_socket.close()
 """