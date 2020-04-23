import subprocess
import requests
import json
import socket
import sys

jump_count = "20"
timeout = "200"
last_addr = ""
hlp = "Сероев Егор Игоревич МО-201 МЕН-282201\nИспользование: python " +sys.argv[0][:-3] + ".py [ip/address]"


def valid_addr(addr):
    try:
        ip = socket.gethostbyname(addr)
        return ip
    except socket.error:
        return False


def clean_ip(ip):
    if(ip[0] == "[" and ip[len(ip)-1] == "]"):
        return ip[1:len(ip)-1]
    return ip


def print_info(res):
    if(len(res) != 0 and res[0].isdigit() and res[1] != "*"):
            ip = clean_ip(res[len(res) - 1])
            response = requests.get("http://ip-api.com/json/" + ip)
            j = json.loads(response.text)
            if (j["status"] == "success"):
                print(res[0] + "   " + ip + "   " + j["as"][2:].split()[0] + "   " + j["isp"] + "   " + j["country"])
            else:
                print(res[0] + "  " + ip + "  " + "Неизвестный адрес")
            global last_addr
            last_addr = ip

if (len(sys.argv) == 2):
    addr = sys.argv[1]
    if(valid_addr(addr)):
        process = subprocess.Popen(["tracert", "-w", timeout, "-h", jump_count, addr], stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                res = output.strip().decode('cp866').split()
                print_info(res)
        if(valid_addr(last_addr) == valid_addr(addr)):
            print("Трассировка завершена. Последний адрес совпадает с запросом")
        else:
            print("Трассировка не завершена. Последий адрес не совпадает с запросом")
    else:
        print("Неверный адрес")
        print(hlp)
else:
    print(hlp)