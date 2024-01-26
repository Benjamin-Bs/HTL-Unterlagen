# VPN

###### = Virtual Private Network



## VPN - Tunnel

- Road Warrior VPN

- Site-to-Site VPN

![9440544c-977a-44c8-b9e9-beca36462132](file:///C:/Users/bsulj/Pictures/Typedown/9440544c-977a-44c8-b9e9-beca36462132.png)



##### Road Warrior VPN

a) Dst: 192.168.10.0/24 -> Tunnel        => split Tunnel
                0.0.0.0/0 -> direkt                    => split Tunnel

b) 0.0.0.0/0 -> Direkt

![Routing Road Warrior&#39;s clients through a Site-To-Site VPN with pfSense 2.0  RC1 and OpenVPN - Stefcho&#39;s Tech Blog](https://blog.stefcho.eu/wp-content/uploads/2011/06/OpenVPN-site-to-site-and-Road-Warrior-routing.png)

##### Site-to-Site VPN

![What Is a Site-to-Site VPN? - Palo Alto Networks](https://www.paloaltonetworks.com/content/dam/pan/en_US/images/cyberpedia/site-to-site-vpn.png?imwidth=480)



### ❌ PPtp❌

PPtp nicht verwenden da die Verschlüssel nicht sicher ist

![Understanding Point-to-Point Tunneling Protocol (PPTP)](https://wwwdisc.chimica.unipd.it/luigino.feltre/pubblica/unix/winnt_doc/pppt/understandingpptp6.gif)

### IPESC over L2TP

![L2TP over IPsec PC - Teltonika Networks Wiki](https://wiki.teltonika-networks.com/images/d/df/Finaltopology.jpg)

### Open VPN

![What is OpenVPN, and how does it work? - Surfshark](https://surfshark.com/wp-content/uploads/2020/11/OpenVPN-protocol-as-VPN-1024x501.png)

[OpenVPN - RouterOS - MikroTik Documentation](https://help.mikrotik.com/docs/display/ROS/OpenVPN#OpenVPN-Overview)

Server Config:

```
/ip pool add name=ovpn-pool range=192.168.77.2-192.168.77.254
 
/ppp profile add name=ovpn local-address=192.168.77.1 remote-address=ovpn-pool
/ppp secret
add name=client1 password=123 profile=ovpn
add name=client2 password=234 profile=ovpn<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
```

```
/interface ovpn-server server set enabled=yes certificate=server<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
```

###### Client Config:

```RouterOS
/interface ovpn-client
add name=ovpn-client1 connect-to=2.2.2.2 user=client1 password=123 disabled=no
/ip route
add dst-address=10.5.8.20 gateway=ovpn-client1
add dst-address=192.168.55.0/24 gateway=ovpn-client1
/ip firewall nat add chain=srcnat action=masquerade out-interface=ovpn-client1<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
```



### Wiregurad

![How to Install WireGuard on FreeBSD? - zenarmor.com](https://www.zenarmor.com/docs/assets/images/1-f429b46a671cf6531fc5c99dd6fe302c.png)


