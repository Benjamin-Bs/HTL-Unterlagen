// array mit zahlen
const list = [4, 25, 46];


// arrow fuction ohne parameter
// wird gespeichert aud eine konstante
const exampleFunction = () => {
    const result = 'array =>';
    return result;
};

console.log(exampleFunction());


// arrow function 
// geschwungene klammern können weggelassen werden
//      -> return keyword nicht notwenig
//      -> wert des nächsten commands entspricht dem rückgabewert
// () sind notwendig bei 0 oder 2 bzw. mehr paramter
// bei genau einem parameter können die runden klammern weggelassen werden
const listDoubled = list.map((value) => value * 2);

console.log(listDoubled);
