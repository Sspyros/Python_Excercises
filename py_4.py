access_template = ['switchport mode access',

'switchport access vlan {}',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan {}']
import pprint

if_mode = input('Enter interface mode (access/trunk):')
if_type = input('Enter interface type and number:')
if if_mode in ['access']:
    option = input('Enter VLAN number: ')
    if_mode_template = access_template
elif if_mode in ['trunk']:
    option = input('Enter allowed VLANs: ')
    if_mode_template = trunk_template

print('Interface {}'.format(if_type))
for config in if_mode_template:
    print(config.format(option))