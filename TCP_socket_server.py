from socket import *
from datetime import datetime
import sys

serverPort= 12000
# TCP server socket 생성
serverSocket = socket(AF_INET,SOCK_STREAM)
# 디폴트는 집 와이파이 주소이다.
serverSocket.bind(('192.168.219.100', serverPort))

# 서버 요청 받기 시작
serverSocket.listen()
print('The server is ready to receive')

while True:
    # 요청오면 connection 만들어주기
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # 수신
        message = connectionSocket.recv(65535).decode()
        request_headers = message.split()
        # print(int(request_headers)) # 500 에러 서버 띄우기
        '''
        request_headers[0] # 요청
        request_headers[1] # 요청 파일
        request_headers[2] # 프로토콜
        '''


        # 프토토콜이 맞을경우
        if request_headers[2] == 'HTTP/1.1' and request_headers[0] in ['GET', 'HEAD']:
            # 주소가 맞는 경우
            if request_headers[1] in ['/', '/index.html', './index.html']:
                
                # index.html 페이지 불러오기
                file_name = './index.html'
                f = open(file_name)
                response_data = f.read()

                # 헤더 만들어 주기
                response_header = 'HTTP/1.1 200 OK\r\n'
                response_header += 'Content-Type: text/html\r\n'
                response_header += 'Content-Length: {}\r\n'.format(str(len(response_data)))
                response_header += 'Date: {}\n\n'.format(datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
                
                # HEAD 요청일 경우
                if request_headers[0] == 'HEAD':
                    connectionSocket.send(response_header.encode('utf-8'))
                
                # GET 인경우
                elif request_headers[0] == 'GET':
                    response_message = response_header
                    response_message += response_data
                    connectionSocket.send(response_message.encode('utf-8'))
                    
            # 주소가 틀린 경우
            else:
                # 404error.html 페이지 불러오기
                file_name = './404error.html'
                f = open(file_name)
                response_data = f.read()
                response_header = 'HTTP/1.1 404 Not Found\r\n'
                response_header += 'Content-Type: text/html\r\n'
                response_header += 'Content-Length: {}\r\n'.format(str(len(response_data)))
                response_header += 'Date: {}\n\n'.format(datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
                response_message = response_header
                response_message += response_data
                connectionSocket.send(response_message.encode('utf-8'))
            
        # 프로토콜이나 요청이 틀릴 경우
        else:
            response_header = 'HTTP/1.1 400 Bad Request\n\n'
            connectionSocket.send(response_header.encode('utf-8'))


        connectionSocket.close()

    # 아예 서버에러 500
    # 로직이 잘못 되거나 통신이 잘못 됐을 경우
    except:
        response_header = 'HTTP/1.1 500 Internal Server Error\n\n'
        connectionSocket.send(response_header.encode('utf-8'))
        connectionSocket.close()
        sys.exit()