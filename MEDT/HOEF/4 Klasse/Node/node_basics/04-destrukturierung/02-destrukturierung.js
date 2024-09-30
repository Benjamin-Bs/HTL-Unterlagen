const address = {
    firstname: 'Eduard',
    lastname: 'Müller',
    street: 'Anton Ehrenfried-Straße',
    houseNr: 20,
    zipCode: 2020,
    city: 'Hollabrunn'
};

// Destrukturierung ist die Zerlegung einer Objekteigenschaft
// in eine Variable/Konstante
//  -> funktioniert nur wenn variablen/konstantenname gleich dem eigenschftsnamen ist

const { firstname, lastname, zipCode } = address;

console.log(`${firstname} ${lastname} ${zipCode}`)

// Bei Arrays ist die Reihenfolge wichtig 
const list = [1, 2, 4]
const [one, two, three] = list;
