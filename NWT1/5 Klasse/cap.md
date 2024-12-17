# CapsMan und Cap

```
/interface bridge
add name=bridge1 vlan-filtering=yes
/interface vlan
add interface=bridge1 name=VL10 vlan-id=10
add interface=bridge1 name=VL20 vlan-id=20
add interface=bridge1 name=VL30 vlan-id=30
add interface=bridge1 name=VL40 vlan-id=40
add interface=bridge1 name=VL50 vlan-id=50
add interface=bridge1 name=VL60 vlan-id=60
/interface wifi channel
add band=5ghz-ax name=5GHz80Mhz width=20/40/80mhz
add band=2ghz-ax name=2GHz20Mhz width=20mhz
/interface wifi datapath
add name=DPGaeste vlan-id=30
add name=DPMitarbeiter
/interface wifi security
add authentication-types=wpa2-psk disabled=no name=SecHTLIoT
add authentication-types=wpa2-eap name=wifisec
add authentication-types=wpa2-psk name=SecGaeste
add authentication-types=wpa2-psk name=SecMitarbeiter
/interface wifi
set [ find default-name=wifi1 ] configuration.country=Austria .manager=local \
    .mode=station-bridge .ssid=HTLIoT disabled=no security=SecHTLIoT
/interface wifi configuration
add channel=5GHz80Mhz country=Austria datapath=DPGaeste mode=ap name=Gaeste5GHz \
    security=SecGaeste
add channel=2GHz20Mhz country=Austria datapath=DPGaeste mode=ap name=Gaeste2GHz \
    security=SecGaeste
/ip pool
add name=deadpool10 ranges=192.168.10.10-192.168.10.250
add name=deadpool20 ranges=192.168.20.10-192.168.20.250
add name=deadpool30 ranges=192.168.30.10-192.168.30.250
add name=deadpool40 ranges=192.168.40.10-192.168.40.250
add name=deadpool50 ranges=192.168.50.10-192.168.50.250
add name=deadpool60 ranges=192.168.60.10-192.168.60.250
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
/interface bridge vlan
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=10
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=20
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=30
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=40
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=50
add bridge=bridge1 tagged=bridge1,ether1,ether2,ether3,ether4,ether5 vlan-ids=60
/interface wifi capsman
set enabled=yes interfaces=VL10,VL20,VL30,VL40,VL50,VL60 package-path="" \
    require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-enabled master-configuration=Gaeste5GHz name-format=%I-5GHz \
    supported-bands=5ghz-ax
/ip dhcp-client
add interface=wifi1
/ip dhcp-server
add address-pool=deadpool10 interface=VL10 name=dhcpServer10
add address-pool=deadpool20 interface=VL20 name=dhcpServer20
add address-pool=deadpool30 interface=VL30 name=dhcpServer30
add address-pool=deadpool40 interface=VL40 name=dhcpServer40
add address-pool=deadpool50 interface=VL50 name=dhcpServer50
add address-pool=deadpool60 interface=VL60 name=dhcpServer60
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
add address=192.168.30.0/24 gateway=192.168.30.1
add address=192.168.40.0/24 gateway=192.168.40.1
add address=192.168.50.0/24 gateway=192.168.50.1
add address=192.168.60.0/24 gateway=192.168.60.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8
/system clock
set time-zone-name=Europe/Vienna
/system identity
set name=Reiche2
/system note
set show-at-login=no
/system ntp client
set enabled=yes
[admin@Reiche2] > 
```





```
/interface bridge
add name=br
/interface vlan
add interface=br name=VLAN10 vlan-id=10
add interface=br name=VLAN20 vlan-id=20
add interface=br name=VLAN30 vlan-id=30
add interface=br name=VLAN40 vlan-id=40
add interface=br name=VLAN50 vlan-id=50
add interface=br name=VLAN60 vlan-id=60
/interface wifi security
add authentication-types=wpa2-psk disabled=no name=SecHTLIoT
/interface wifi
set [ find default-name=wifi1 ] configuration.country=Austria .manager=local \
    .mode=station-bridge .ssid=HTLIoT disabled=no security=SecHTLIoT
/interface bridge port
add bridge=br interface=ether1
add bridge=br interface=ether2
add bridge=br interface=ether3
add bridge=br interface=ether4
add bridge=br interface=ether5
/interface bridge vlan
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=10
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=20
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=30
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=40
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=50
add bridge=br tagged=br,ether1,ether2,ether3,ether4,ether5 vlan-ids=60
/interface wifi cap
set discovery-interfaces=VLAN10 enabled=yes
/ip dhcp-client
add interface=wifi1
/system clock
set time-zone-name=Europe/Vienna
/system identity
set name=Cap
/system note
set show-at-login=no
/system ntp client
set enabled=yes
[admin@Cap] > 

/interface/wifi/datapath/add bridge=br name=capdp
/interface/wifi/set configuration.manager=capsman .mode=ap datapath=capdb disabled=no
```
