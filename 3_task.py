import socket, sys
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
host = input('Введите адрес сайта или IP адрес: ')
p_range = input('Введите через пробел диапазон портов, или что угодно иное, для проверки стандартных портов: ').split()

for i in range(len(p_range)):  
    try:
        p_range[i] = int(p_range[i])
    except ValueError:
        break
else:
    ports = []
    for i in range(p_range[0],p_range[1]):
        ports.append(i)

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        pass
    else:
        s.close
        print (str(port) + ' порт активен')