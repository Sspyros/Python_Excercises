import re

match_ip, match_sub = 0, 0
ip_bin, broadcast_bin ='', ''
ip_addr_re = re.compile('^(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[0-9][0-9]|[0-9])$')
subnet_mask_re = re.compile('([89]|[12]\d{1}|30)')

while not match_ip:
    ip_addr = input('Enter ip address:')
    match_ip = ip_addr_re.search(ip_addr).group(0)
    if not match_ip:
        print('Invalid IP address format')

while not match_sub:
        subnet_mask = input('Enter subnet mask: /')
        match_sub = subnet_mask_re.search(subnet_mask).group(0)
        if not match_sub:
            print('Subnet mask is invalid')

for i in match_ip.split('.'):
    ip_bin+=bin(int(i))[2:].zfill(8)

match_ip = match_ip.split('.')
print('{0:>8}  {1:>8}  {2:>8}  {3:>8}'.format(match_ip[0],match_ip[1],match_ip[2],match_ip[3]))
print('{0:10}{1:10}{2:10}{3:10}'.format(ip_bin[0:8],ip_bin[8:16],ip_bin[16:24],ip_bin[24:32]))

broadcast_bin = ip_bin[:int(match_sub)] + '1' * (32 - int(match_sub))
ip_bin = ip_bin[:int(match_sub)] + '0' * (32 - int(match_sub))

print('network address is: {}.{}.{}.{}/{}'.format(int(ip_bin[0:8], 2),int(ip_bin[8:16], 2),int(ip_bin[16:24], 2),int(ip_bin[24:32], 2),subnet_mask))
print('broadcast address is: {}.{}.{}.{}/{}'.format(int(broadcast_bin[0:8], 2),int(broadcast_bin[8:16], 2),int(broadcast_bin[16:24], 2),int(broadcast_bin[24:32], 2),subnet_mask))