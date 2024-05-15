/*
Eduard Müller
Anton Ehrenfried-Straße 10
2020 Hollabrunn
*/

// Problem:
// Stringkonkatination mit + ist umständlich und fehleranfällig

// 1. Beispiel: Einrückung, Leerzeichen, Zeilenumbruche, usw.
const address = "Eduard Müller\n" +
    "Anton Ehrenfried-Straße 10\n" +
    "2020 Hollabrunn\n";

console.log(address);

// 2. Beispiel: Strings aus Konstanten/Variablen zusammenbauen
const firstName = "Eduard ";
const lastName = "Müller";
const street = "Anton Ehrenfried-Straße 10 ";
const houseNR = 10;
const zipCode = 2020;
const city = " Hollabrunn";

const line1 = firstName + lastName;
const line2 = street + houseNR;
const line3 = zipCode + city;
const address2 = line1 + "\n" + line2 + "\n" + line3;
console.log(address2);


