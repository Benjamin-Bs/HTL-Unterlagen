class Rechteck{
    [float]$length
    [float]$width

    Rechteck([int] $length, [int] $width){
        $this.length = $length
        $this.width = $width
    }

    [float]getArea(){
        return ($this.length * $this.width)
    }

}

$myObject = [Rechteck]::new(8,5)

"Area: "+ $myObject.getArea()