from winreg import *

def regbin_to_mac(val):
    address = ''
    for char in val:
        address += "%02x "% ord(char)
    address = address.strip(' ').replace('',':')[0:17]
    return address

def print_nets():
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print('\n[*] Wireless Access Point History\n')
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            net_key = OpenKey(key, str(guid), reserved=0, access=KEY_READ) 
            #registry key indexes the network name 
            (n, addr, t) = EnumValue(net_key, 1)
            (n, name, t) = EnumValue(net_key, 4)
            mac_addr = regbin_to_mac(addr) 
            net_name = str(name)
            print('[+]' + net_name + ' ' + mac_addr)
            CloseKey(net_key)
        except:
            break

def main():
    print_nets()

if __name__ == '__main__':
    main()
