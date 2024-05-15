const address = {
    firstname : 'Eduard', 
    lastname : 'Müller',
    street : 'Anton Ehrenfried-Straße',
    houseNr : 20,
    zipCode: 2020,
    city: 'Hollabrunn',
    print: () => console.log(`${firstname} ${lastname}
    ${street} ${houseNr}
    ${zipCode} ${city}`)
}; 

// zugriff auf objekteigenschaften
const firstName = address.firstname;
const lastName = address.lastname;
const street = address.street;
const houseNr = address.houseNr;
const zipCode = address.zipCode;
const city = address.city;

// zugriff auf print-funktion
address.print();