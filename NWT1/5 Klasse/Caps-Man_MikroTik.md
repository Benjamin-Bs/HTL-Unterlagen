# Caps-man

Wireless Lan



```
/interface/wifi/security/ add name=SecGaeste authentication-types=wpa2-psk passfprase=test
/interface/wifi/datapath/add name=DPGaeste vlan-id=30 
/interface/wifi/channel/add band=5ghz-ax width=20/40/80mhz name=5GHz80Mhz 
/interface/wifi/configuration/add name=Gaeste5GHz channel=5GHz80MHz country=Austria datapath=DPGaeste mode=ap security=SecGaeste ssid=Gaeste

/interface/wifi/capsman/set enabled=yes interface=VLAN10
/interface/wifi/provisioning/add supported-bands=5ghz-ax master-configuration=Gaeste5GHz name-format=%I-5GHz action=create-enabled

```


