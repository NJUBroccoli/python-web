import socketsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)sock.connect(('127.0.0.1', 8080))data = '12'sock.send(data)receivedData = sock.recv(1024)print receivedDatasock.close()