/*
Eduard Müller
Anton Ehrenfried-Straße 10
2020 Hollabrunn
*/

// template strings mit interpolation
// (template steht für schablone/vorlage)
// -> innerhalb eines template string mit ${ } kann javascript code ausgewertet werden

const firstName = "Eduard";
const lastName = "Müller";
const street = "Anton Ehrenfried-Straße";
const houseNR = 10;
const zipCode = 2020;
const city = "Hollabrunn";

const address = `${firstName} ${lastName}
${street} ${houseNR}
${zipCode} ${city}`;

console.log(address);
 