from socket import *

serverName= '192.168.219.100'
serverPort= 12000

def create_socket_and_send_message(request_message):
    # 클라이언트 소켓 만들기
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(request_message.encode('utf-8'))

    # 응답 확인
    recieve_message= clientSocket.recv(65535)
    print("######### From Server ###########")
    print(recieve_message.decode())

    clientSocket.close()

# 1. 정상적인 head 요청
request_message  = 'HEAD / HTTP/1.1\r\n'
request_message += 'Host: 192.168.219.100:12000\r\n'
request_message += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)



# 2. 정상적인 get 요청
request_message  = 'GET / HTTP/1.1\r\n'
request_message += 'Host: 192.168.219.100:12000\r\n'
request_message += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)


# 3. 잘못된 페이지 get 요청
request_message  = 'GET /random HTTP/1.1\r\n' # 없는 페이지 요청
request_message += 'Host: 192.168.219.100:12000\r\n'
request_message += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)


# 4. 프로토콜이나 요청 메소드 잘못 요청
request_message  = 'POST / HTTTTP/1.1\r\n'
request_message += 'Host: 192.168.219.100:12000\r\n'
request_message += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)


# 5. internal server error
# 해당 요청은 서버에서 에러가 나야하므로 서버에 있는 에러 띄우는 코드를 주석해제 해야한다.
'''
request_message  = 'HEAD / HTTP/1.1\r\n'
request_message += 'Host: 192.168.219.100:12000\r\n'
request_message += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)
'''

