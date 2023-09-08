$list = Import-CSV -Path "C:\dns_records.csv" -Delimiter ";"


foreach($csv in $list){
    
    $name = $csv.name
    $ipv4 = $csv.ipv4
    $type = $csv.type

  if($type -eq "A"){
    Add-DnsServerResourceRecordA -Name $name -ZoneName "suljevic.at" -AllowUpdateAny -IPv4Address $ipv4 -TimeToLive 01:00:00
  }

  if($type -eq "MX"){
    Add-DnsServerResourceRecordMX -Preference 10 -Name $name -TimeToLive 01:00:00 -MailExchange $ipv4 -ZoneName "suljevic.at"
  }

  if($type -eq "NS"){
	Add-DnsServerResourceRecordA -IPv4Address $ipv4 -Name $name -ZoneName "suljevic.at";    
	Add-DnsServerResourceRecord -NS -ZoneName suljevic.at -Name suljevic.at -NameServer $($name + ".suljevic.at.");
  }

}