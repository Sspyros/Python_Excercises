with open('commands.txt', 'r') as file:
	read_data = file.readlines()
file.close()

import re
command_re = re.compile('(?<=^switchport trunk allowed vlan\s)(.+)')

vlans, vlans_list, unique_vlans = [],[], []
for line in read_data:
    command = command_re.search(line)
    if command:
        vlans.append(command.group(1))

for line in vlans:
    vlans_list.append(line.replace(" ", "").split(','))
flat_list = [item for sublist in vlans_list for item in sublist]
for vlan in flat_list:
    if flat_list.count(vlan) == 1: unique_vlans.append(vlan)
for vset in vlans_list:
    common_vlans = list(set(common_vlans).intersection(vset))

print('List_1 =',sorted(common_vlans, key=int))
print('List_2 =',sorted(unique_vlans, key=int))
