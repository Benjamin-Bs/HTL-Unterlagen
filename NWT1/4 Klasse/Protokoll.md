# Protokoll

#### Openssh-server installieren:

```bash
apt install openssh-server
```



##### Netcat installieren:

```bash
sudo apt install netcat
```

Server mit dem richtigen Port einstellen:

```bash
nc -l 25565
```

![67224176-403e-4018-82ad-4dc8a4769728](file:///C:/Users/bsulj/Pictures/Typedown/67224176-403e-4018-82ad-4dc8a4769728.png)

Sich mit ssh verbinden

```bash
ssh root@172.18.10.12
```

![747c0520-3037-48f2-b9c2-1dc0ed25e361](file:///C:/Users/bsulj/Pictures/Typedown/747c0520-3037-48f2-b9c2-1dc0ed25e361.png)

### Firwall einstellen mittels iptables

###### Iptables installieren:

```bash
sudo apt install iptables
```

###### Die Regeln für die Firewall konfiguriren

```bash
sudo iptables -A INPUT -p tcp --dport 2222 -j ACCEPT # SSH-Port anpassen
```

```bash
sudo iptables -A INPUT -p tcp --dport 25565 -j ACCEPT # TCP-Server-Port anpassen
```

![c306f173-1695-42e8-83a9-d2d2e43b01e0](file:///C:/Users/bsulj/Pictures/Typedown/c306f173-1695-42e8-83a9-d2d2e43b01e0.png)

###### Die Regeln speichern

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
sudo netfilter-persistent reload
```



![d2b8162d-4c57-4e2a-aec4-2937ef8f89a0](file:///C:/Users/bsulj/Pictures/Typedown/d2b8162d-4c57-4e2a-aec4-2937ef8f89a0.png)

#### Mit Nmap testen:

###### Nmap installieren:

```bash
apt install nmap

nmap localhost
```

![4023daf8-9993-43fa-a62d-21409b666051](file:///C:/Users/bsulj/Pictures/Typedown/4023daf8-9993-43fa-a62d-21409b666051.png)



###### Den SSh Zugang dem root entnehmen:

```bash
nano /etc/ssh/sshd_config
```

Den **PermitRootLogin** auf **no** und **PasswordAuthentication** ebenfalls auf **no** setzen

![60611b31-b3ea-4b85-87ff-979e0996a9f0](file:///C:/Users/bsulj/Pictures/Typedown/60611b31-b3ea-4b85-87ff-979e0996a9f0.png)

![8a275f9c-3596-49b1-931d-aab54692cfa4](file:///C:/Users/bsulj/Pictures/Typedown/8a275f9c-3596-49b1-931d-aab54692cfa4.png)



Danach den SSH Server neustarten:

```bash
sudo service ssh restart
```



#### SSH Port ändern:

```bash
sudo nano /etc/ssh/sshd_config
```

![4f3d606f-e90f-497f-b9a5-db6da2c30385](file:///C:/Users/bsulj/Pictures/Typedown/4f3d606f-e90f-497f-b9a5-db6da2c30385.png)

Der Port wurde von 22 auf 2222



### Benutzer erstellen:

```bash
sudo adduser mincraft_user

sudo usermod -aG sudo mincraft_user    #Admin Rechte geben
```


