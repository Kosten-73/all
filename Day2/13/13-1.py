# print(bin(120)[2:])
# print(bin(112)[2:])
# print(int("11110000",2))

from ipaddress import *

ip_net = ip_network("142.108.56.118/255.255.255.240", False)
# ip_net = ip_network("142.108.56.118/28")
cnt = 0
for ip in ip_net:
    print(ip)
    print(int(ip))
    print(bin(int(ip)))
    if bin(int(ip))[-16:].count("1") > bin(int(ip))[:-16].count("1"):
        cnt += 1
print(cnt)