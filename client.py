import socket
import random
import time

SERVER_IP = '127.0.0.1' # endereço IP do servidor (localhost nesse caso)
SERVER_PORT = 1234 # número da porta do servidor ao qual se conectar

# loop para manter o cliente rodando indefinidamente
while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um objeto socket TCP
    client_socket.connect((SERVER_IP, SERVER_PORT)) # conecta ao servidor usando o endereço IP e número da porta

    numero_casas = random.randint(1, 30) # gera um número inteiro aleatório entre 1 e 30, que é o número de casas que queremos gerar
    numero = ''.join(random.choices('0123456789', k=numero_casas)) # é escolhido k digitos (onde k é o número de casas) entre 0 e 9 e concatenamos esses dígitos
    client_socket.send(numero.encode()) # envia o número gerado ao servidor

    resposta = client_socket.recv(1024).decode() + ' FIM' # recebe a resposta do servidor e adiciona "FIM" no final
    print('Numero: ',numero,' Recebido: {}'.format(resposta)) # imprime o número gerado e a resposta recebida do servidor

    client_socket.close()  # encerra a conexão do socket com o servidor
    time.sleep(10) # pausa o programa por 10 segundos antes de repetir o loop e gerar um novo número para enviar ao servidor
