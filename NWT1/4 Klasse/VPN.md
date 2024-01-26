# VPN

###### = Virtual Private Network



## VPM - Tunnel

- Road Warrior VPN

- Site-to-Site VPN



![20240109_105833](https://cdn.discordapp.com/attachments/801382612639285248/1194221897076973638/20240109_105833.jpg)



##### Road Warrior VPN

a) Dst: 192.168.10.0/24 -> Tunnel          => split Tunnel
                0.0.0.0/0 -> direkt                     => split Tunnel

b) 0.0.0.0/0 -> Direkt

![Routing Road Warrior&#39;s clients through a Site-To-Site VPN with pfSense 2.0  RC1 and OpenVPN - Stefcho&#39;s Tech Blog](https://blog.stefcho.eu/wp-content/uploads/2011/06/OpenVPN-site-to-site-and-Road-Warrior-routing.png)

##### Site-to-Site VPN

![What Is a Site-to-Site VPN? - Palo Alto Networks](https://www.paloaltonetworks.com/content/dam/pan/en_US/images/cyberpedia/site-to-site-vpn.png?imwidth=480)



#### ❌ PPtP ❌

PPtP nicht mehr verwenden da es eine sehr schlechte Verschlüsselung hat

![What Is PPTP VPN and Should You Use It? | VeePN Blog](https://veepn.com/blog/wp-content/uploads/2023/07/PPTP-VPN.png)





### IPSEC over L2TP

![L2TP over IPsec PC - Teltonika Networks Wiki](https://wiki.teltonika-networks.com/images/d/df/Finaltopology.jpg)

### OpenVPN

![What is OpenVPN, and how does it work? - Surfshark](https://surfshark.com/wp-content/uploads/2020/11/OpenVPN-protocol-as-VPN-1024x501.png)

##### MikroTik Anwendung

[OpenVPN - RouterOS - MikroTik Documentation](https://help.mikrotik.com/docs/display/ROS/OpenVPN)[OpenVPN - RouterOS - MikroTik Documentation](https://help.mikrotik.com/docs/display/ROS/OpenVPN)

###### Server Config:

```

```

###### Client Config:

```

```

```

```

### Wireguard

![How to Install WireGuard on FreeBSD? - zenarmor.com](https://www.zenarmor.com/docs/assets/images/1-f429b46a671cf6531fc5c99dd6fe302c.png)
