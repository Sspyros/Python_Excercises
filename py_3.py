with open('ShowIpRoute.txt', 'r') as file:
	read_data = file.readlines()
file.close()
import re

codes = []
codes_re = re.compile('(\w+\d?|\*|\+|\%)\s\-\s(.+?)(?:,|$)')
for line in read_data:
        route = codes_re.search(line)
        if route: codes.extend(re.findall('(\w+\d?|\*)\s\-\s(.+?)(?:,|$)', line))
codes=dict(codes)

for line in read_data:
    capt = re.compile('^(\w+)\s?(\w*\d*)?\s(\d+\.\d+\.\d+\.\d+).+?(?:(\d+\/\d+).+?(\d+\.\d+\.\d+\.\d+).+?(\d+:\d+:\d+).+?(\w+$)|((\w+$)))')
    route = capt.search(line)
    if route:
        if route.group(2): print('{0:20}{1:10}'.format('Protocol:',codes[route.group(2)]))
        else: print('{0:20}{1:10}'.format('Protocol:',codes[route.group(1)]))
        print('{0:20}{1:10}'.format('Prefix:',route.group(3)))
        if route.group(4): print('{0:20}{1:10}'.format('AD/Metric:',route.group(4)))
        if route.group(5): print('{0:20}{1:10}'.format('Next-Hop:',route.group(5)))
        if route.group(6):print('{0:20}{1:10}'.format('Last update:',route.group(6)))
        if route.group(7):print('{0:20}{1:10}\n'.format('Outbound interface:',route.group(7)))
        if route.group(8):print('{0:20}{1:10}\n'.format('Outbound interface:',route.group(8)))
        
        
        
        