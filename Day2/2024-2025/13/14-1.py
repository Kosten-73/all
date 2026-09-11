from ipaddress import *

# print(bin(252).count("1"))

ip_net = ip_network("252.67.33.87/255.252.0.0", False)
# ip_net = ip_network("142.108.56.118/28")
cnt = 0
for ip in ip_net:
    # print(ip)
    # print(int(ip))
    # print(bin(int(ip)))
    if bin(int(ip))[-16:].count("1") > 2 * bin(int(ip))[:-16].count("1"):
        cnt += 1
print(cnt)