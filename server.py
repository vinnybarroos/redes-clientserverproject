import socket

# define o endereço IP e número de porta do servidor
SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234

# cria um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincula o socket a um endereço IP e número de porta específico
server_socket.bind((SERVER_IP, SERVER_PORT))

# esperando por conexões
server_socket.listen()

# loop para manter aceitando novas conexões
while True:
    print('Aguardando por uma conexão ...')

    # aceita a conexão de um cliente
    client_socket, client_address = server_socket.accept()

    # imprime uma mensagem para indicar que a conexão foi aceita
    print('Conexão aceita de {}:{}'.format(client_address[0], client_address[1]))

    # loop para manter recebendo dados do cliente
    while True:
        # try para receber dado do cliente
        try:
            numero = client_socket.recv(1024).decode()
        except ConnectionResetError:
            # se a conexão for redefinida pelo cliente, imprime uma mensagem e quebra o loop
            print('Conexão redefinida pelo ponto')
            break
         # se não existe dados recebidos do cliente, imprime mensagem e quebra o loop
        if not numero:
            print('Cliente desconectado')
            break
         # se o número recebido tiver mais de 10 casas, gera uma string com o mesmo tamanho do número
        if len(numero) > 10:
            string = 'A' * len(numero)
            client_socket.send(string.encode())
        else:
            # se o número recebido tiver menos de 10 casas, checa se é impar ou par
            if int(numero) % 2 == 0:
                client_socket.send('PAR'.encode())
            else:
                client_socket.send('IMPAR'.encode())
    # fecha o socket do cliente
    client_socket.close()
# fecha o socket do servidor
server_socket.close()
