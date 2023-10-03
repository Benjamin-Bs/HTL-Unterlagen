$list = Import-CSV -Path "C:\Users\bsulj\Desktop\SYT\CSV_File_Parsing\score_sample.csv" -Delimiter "," -Encoding UTF8

$myTable=@{}


foreach($csv in $list){


    $name = $csv.Vorname ,$csv.Nachname
    $score = [int] $csv.Scores

    if(!$myTable.ContainsKey($name)){

        $myTable[$name] = @($score, 1)         

    }else{

      $myTable[$name][0] += ($score) // Es wird an der Stelle [0] scoure gespeichert
	
    }
}

foreach($person in $myTable.Values){
    
    $summe = 0
    $count = 0

    foreach($s in $person){
    
        $summe +=$s
        $count++

    }

$result = $summe/$count    
    echo $result
}

    
    