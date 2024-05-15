const list = [4, 23, 53];

// erstelle ein neues array mit doppelten zahlen aus list
// verwendet die map funktion des arrays (map -> Abbildung)
// callback-function    -> wird für jedes element des arrays aufgerufen
//                      -> parameter dafür sind wert, index und gesamtes array
//                      -> verpflichteter parameter ist der wert


// variante mit inline function (lange schreibweise)
const listDoubled = list.map(function double(value, index, array) {
    const result = value * 2;
    return result;
});

// variante mit inline und anonymous function (callbackfunktion ohne überflüssige parameter)
const listDoubled2 = list.map(function (value) {
    const result = value * 2;
    return result;
});

console.log(listDoubled2);
// Arrow function
const listDoubled3 = list.map((value) => value * 2);
