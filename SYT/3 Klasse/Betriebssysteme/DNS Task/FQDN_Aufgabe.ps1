$address = "www.amazon.de"

nslookup $address 8.8.8.8 

nslookup.exe -type=NS . 8.8.8.8
nslookup.exe -type=A b.root-servers.net 8.8.8.8

#Damit man die Ip-Adresse in eine Variable speichert
$firstOutput = nslookup.exe -type=A b.root-servers.net 8.8.8.8 | Select-String -Pattern "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" | Select-Object -Last 1
$ip_address = $firstOutput -replace ".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*", '$1'

nslookup.exe -type=NS de. $ip_address

$output = nslookup.exe -type=A c.gtld-servers.net 8.8.8.8 | Select-String -Pattern "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" | Select-Object -Last 1
$ipAddress = $output -replace ".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*", '$1'

nslookup.exe -type=NS amazon.de. $ipAddress

$Secondoutput = nslookup.exe -type=A ns4.p31.dynect.net 8.8.8.8 | Select-String -Pattern "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" | Select-Object -Last 1
$ip_Address = $Secondoutput -replace ".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*", '$1'

nslookup.exe -type=A www.amazon.de. $ip_Address
