$list = Import-Csv -Path "C:\Users\bsulj\Desktop\SYT\CSV_File_Parsing\score_sample.csv" -Delimiter "," -Encoding UTF8

$myTable = @{}

$myMethode = @{
    MemberType = "ScriptMethod" 
    Name = "getAverage"
	Value = {
	return ( this.sum / this.count)
	}
}

foreach($csv in $list){
    $score = [int] $csv.Scores
    $name = $csv.Vorname +","+ $csv.Nachname


    if(!$myTable.ContainsKey($name)){
        $myObject = [PSCustomObject]@{
                sum = [int] $score
                count = 1
        }
        
        Add-Member -InputObject $myObject @myMethode
        $myTable.Add($name,$myObject)
        
    }else{

        $myTable[$name].sum += $score
        $myTable[$name].count ++
    
    }

    "Durchscnitt " + $myObject.getAverage()


}



