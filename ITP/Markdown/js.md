# 1.Block-Scope, let und const
##### Es gibt mehrere Scopes grob unterteilt in
Global Scope (alles außerhalb von Funktions)
Local Scope  (alles innerhalb von Funktions)

```js
//global scope
function foo1(){
    //local scope 1
    function foo2(){
        //local scope 2
    }
}

//global scope
function foo3(){
    //local scope 3
}

//global scope
```


##### Local scopes können noch weiter aufgeteilt werden in
Funktion Scope (innerhalb von Funktion aber nicht in Schleifen oder einem if)
Block Scope (innerhalb von Funktion und in Schleifen oder einem if)

```js

function foo(){
    //funktion scope
    if(true){
        //block scope
        var fruit1 = 'apple';        //exist in function scope
        const fruit2 = 'banana';     //exist in block scope
        let fruit3 = 'strawberry';   //exist in block scope

    }
    //funktion scope
    console.log(fruit1);
    console.log(fruit2);
    console.log(fruit3);
}
```


### const
const is used when you don't want to reassign the variable. It stays constant once it's declared. As a result, const is always a default option for me if I don't need to reassign the variable. In this way, we can also avoid the case when we occasionally declare the same variable name in other files.

### let
When it comes to the situation I need to reassign a variable, let is more welcome than var after ES6. The reason is that let is in block scope which means it only exists within its own scope. For Example,

```js

let foo='outside';
if(true){
    let foo = 'inside'
    console.log(foo);            //print inside

}
console.log(foo);                //print outside
```

After if condition, foo is equal to 'outside' rather than the value we have inside the if statement ('inside').

# 2. Template Strings

In JavaScript ermöglichen Template Strings die einfache und übersichtliche Verarbeitung von Zeichenketten (Strings) in einer flexiblen Art und Weise. 

## Was sind Template Strings?

Template Strings sind eine erweiterte Möglichkeit, Zeichenketten in JavaScript zu erstellen. Sie ermöglichen es, Variablen oder Ausdrücke in Zeichenketten einzufügen. Sie werden durch Backticks (`` ` ``) anstelle von einfachen Anführungszeichen oder doppelten Anführungszeichen definiert.

## 2.1 Funktionalität

Die Hauptfunktionalitäten von Template Strings umfassen:

1. **Einfügen von Variablen:** Mit Hilfe von Platzhaltern `${}` können Variablen oder Ausdrücke direkt in die Zeichenkette eingefügt werden.

2. **Mehrzeilige Zeichenketten:** Mehrzeilige Zeichenketten können problemlos erstellt werden, ohne Zeilenumbrüche manuell hinzufügen zu müssen.


## 2.2 Anwendungen

### 2.2.1 Einfaches Zusammenfügen von Zeichenketten

```javascript
const name = "Max";
const greeting = `Hallo, ${name}!`;
console.log(greeting); 
// Ausgabe: Hallo, Max!
```

### 2.2.2 Mehrzeilige Zeichenketten

Template Strings machen es einfach, mehrzeilige Zeichenketten zu erstellen:

javascript
```javascript
const multiLine = `Dies ist eine
mehrzeilige Zeichenkette
erstellt mit Template Strings. `;

console.log(multiLine); 
// Ausgabe:
// Dies ist eine 
// mehrzeilige Zeichenkette 
// erstellt mit Template Strings.
```

### 2.2.3 Verwendung in Funktionen

Template Strings sind besonders nützlich, um formatierte Ausgaben erzeugen:

```javascript
function begrüßung(name) {
	return `Hallo, ${name}!`;
}

console.log(begrüßung("Anna")); 
// Ausgabe: Hallo, Anna!
```

### 2.2.4 Mathematische Berechnungen

Template Strings können auch zur Darstellung von Ergebnissen mathematischer Berechnungen verwendet werden:

javascript
```javascript
const a = 5;
const b = 3;
const summe = `Die Summe von ${a} und ${b} ist ${a + b}.`;

console.log(summe); 
// Ausgabe: Die Summe von 5 und 3 ist 8.
```

# 3. Destructing von Objekten und Arrays
## 3.1 Objekte

Objekte sind in JavaScript Assoziative Arrays, wobei Methoden als Funktionen in Properties abgespeichert werden. Aus diesem Grund ist "JavaScript Object Notation" (JSON) so beliebt.

### Syntax
```JavaScript 
// Array
const numbers = [1, 2, 3];
const numbers2 = [
	1, 
	2, 
	3
];

// Object
const person = {
	firstname: 'Max',
	lastName: 'Mustermann',
	age: 35,
	speak: function(text) {
		console.log(`${this.firstname} ${this.lastname} says: ${text}`);
	}
}; 
```

## 3.2 Destructuring

Destrucuring von Arrays und Objekten funktioniert so, dass man die einzelnen Properties/ArrayeintrÃ¤ge schnell in Variablen speichern kann.

### 3.2.1 Syntax
```JavaScript
// Array
const [first, ,third] = numbers;
console.log(first);
console.log(third);

// Object
const {firstname: fname, lastname: lname, age} = person;
console.log(fname);
console.log(lname);
console.log(age);
```

### 3.2.1 Alternative
```JavaScript
// Array
const first = numbers[0];
const third = numbers[2];

// Object
const fname = person.firstname;
const lname = person["lname"];
const age = person.age;
```

## 3.3 Vorteile

- Lesbarkeit
- Kompakter Code
- Fehlervermeidung


# 4.  Klassen
## 4.1 Constructor

### 4.1.1 Syntax
```JavaScript
class Person {
	constructor(firstname, lastname, age) {
		this.firstname = firstname;
		this.lastname = lastname;
		this.age = age;
	}
}
const person1 = new Person("Max", "Mustermann", 35);
```

### 4.1.2 Alternative
```JavaScript
function Person(firstname, lastname, age) {
	this.firstname = firstname; 
	this.lastname = lastname;
	this.age = age; 
}
const person1 = new Person("Max", "Mustermann", 35);
```

## 4.2 ReadOnly-Properties

Eine ReadOnly-Property ist eine Property, die man nicht bearbeiten kann. 

### 4.2.1 Syntax
```JavaScript
// Klasse "Person"
Object.defineProperty(Person.prototype, 'lastname', { 
	writable: false, 
	enumerable: true,
	configurable: true
});

// Object "person1"
Object.defineProperty(person1, 'lastname', { 
	writable: false, 
	enumerable: true,
	configurable: true
});

```

## 4.3 Getter

### 4.3.1 Syntax
```JavaScript
class MyClass { 
	constructor() { 
		this._myProperty = 42; 
	} 
	get myProperty() { 
		return this._myProperty; 
	} 
} 
const myInstance = new MyClass(); 
console.log(myInstance.myProperty);
```
# 5. Export & Import 

Dienen dazu den Code in **wiederverwendbare** und **wartbare** Teile zu organisieren

## 5.1 Export
Es gibt zwei Hauptmethoden zum Exportieren:
- Mit dem Schlüsselwort "**export**" kann man bestimmte Funktionen, Variablen oder Klassen nach Module exportieren

```javascript
// Man befindet sich gerade in math.js 
export const add = (a,b) => a + b;

export function (a , b) {
	return a + b;
}

export const sub = (a,b) => a - b;
```

- Du kannst die Syntax "**export default**" verwenden, um eine einzelne Entität als Standardexport aus einem Modul zu exportieren. Pro Modul kannst du nur einen Standardexport haben.
```javascript
// Man befindet sich gerade in utils.js 
const capitalize = (str) => str.toUpperCase();
export default capitalize;
```
## 5.2 Import

Das Importieren ist der Vorgang, durch den exportierte Entitäten aus anderen Modulen in das aktuelle Modul gebracht werden, um sie zu verwenden. 
Das Schlüsselwort ist "**import**"

- Um **benannte Exporte** zu importieren, gibst du die Namen in geschweiften Klammern "**{}**" an und gibst den relativen Pfad zum Modul an.
- Um einen **Standardexport** zu importieren, verwendest du den Namen, den du dafür festgelegt hast.

``` javascript
// Man befindet sich auf der Hauptseite: main.js
import { add, subtract } from './math.js'; // Benannte Exporte 
import capitalize from './utils.js'; // Standardexport 

console.log(add(5, 3)); // 8 
console.log(subtract(8, 3)); // 5 
console.log(capitalize('hello')); // "HELLO"
```


# 6. Arrow Funktionen

Ist eine kompakte und praktische Möglichkeit, Funktionen in JavaScript zu definieren
## 6.1 Syntax

Reguläre Funktion:
```javascript
const multi = function(x,y){
	return x * y; 
}
```
	
Arrow Funktion:
```javascript
multi = (x,y) => {
	return x * y;
}

//Die kurze Schreibweise kann verwendet werden, wenn ein Ausdruck zurück gegeben wird
const multi = (x,y) => x * y;
```

## 6.2 this

- In **regulären Funktionen** stellte das Schlüsselwort **this** das Objekt dar, das die Funktion aufruft. Dabei kann es sich um das Fenster, das Dokument oder was auch immer handeln.
- Bei **Arrow Funktionen** stellt das Schlüsselwort **this** immer das Objekt dar, das die Arrow Funktion definiert hat.

```javascript
// Regular Function:  
hello = function() {  
  document.getElementById("demo").innerHTML += this;  
}  
  
// The window object calls the function:  
window.addEventListener("load", hello);  
  
// A button object calls the function:  
document.getElementById("btn").addEventListener("click", hello);
```

```javascript
// Arrow Function:  
hello = () => {  
  document.getElementById("demo").innerHTML += this;  
}  
  
// The window object calls the function:  
window.addEventListener("load", hello);  
  
// A button object calls the function:  
document.getElementById("btn").addEventListener("click", hello);
```

Das Ergebnis zeigt, dass das erste Beispiel zwei verschiedene Objekte (Window und Button) zurückgibt und das zweite Beispiel das Window Objekt zweimal zurückgibt, da das Window Objekt der „Owner“ der Funktion ist.
# 7. Default-parameter und Restparameter
## 7.1 Default-parameter

Wenn der Parameter nicht angegeben wird, wird standartmäßig der Default-Wert genommen.
### 7.1.1 Syntax
```JavaScript
function greet(name = "Anonymous") {
	console.log(`Hello, ${name}!`);
}

greet(); // Output: Hello, Anonymous!
greet("Alice"); // Output: Hello, Alice!
```

## 7.2 Restparameter

Der Restparameter fasst alle restlichen Parameter zusammen zu einem Array.

### 7.2.1 Syntax
```JavaScript
function sum(...numbers) { 
	let total = 0;
	numbers.forEach((num) => {
		total += num; 
	});
	return total;
}

console.log(sum(1, 2, 3)); // Output: 6 
console.log(sum(4, 5, 6, 7, 8)); // Output: 30
```
# 8. SPREAD Operator(...)

In JavaScript gibt es den Spread Operator, der eine wichtige Rolle bei der Arbeit mit Arrays und Objekten spielt. Der Spread Operator ermöglicht es, Elemente eines Arrays oder Eigenschaften eines Objekts in eine neue Datenstruktur zu kopieren oder zu kombinieren.

## 8.1 Was ist der Spread Operator?

Der Spread Operator, der durch drei Punkte `...` dargestellt wird, ermöglicht das Ausbreiten von Elementen aus einer Datenstruktur wie einem Array oder einem Objekt. Dies kann nützlich sein, um neue Arrays oder Objekte zu erstellen, bestehende zu kopieren oder Elemente zusammenzuführen.

Hier sieht man eine einfache function welche mit 3 Parametern aufgerufen wird, welche danach zusammenaddiert werden:

```javascript
function sum(a, b, c){
	return a + b + c; 
}

console.log(sum(1, 2, 3));
```

Wenn man nun jedoch diese function nun mit einem array aufrufen will,

```javascript
function sum(a, b, c){
	return a + b + c; 
}

let numbers = [1, 2, 3];

console.log(sum(numbers));
```

sieht es dann so aus:

![[Pasted_image_20230913163132.png]]

Grund dafür ist, dass js hier versucht das array in `a` hineinzuschreiben.
Um dieses Problem nun zu lösen gibt es eben den spread operator. Dieser bewirkt, dass hier das array auf die einzelnen Aufrufparameter verteilt (spread) wird. Verwenden kann man ihn, indem man einfach `...` vor den Arrayaufruf schreibt.

```javascript
function sum(a, b, c){
	return a + b + c; 
}

let numbers = [1, 2, 3];

console.log(sum(...numbers));
```

![[Pasted_image_20230913163549.png]]

Somit wurde das gewünschte Ergebnis erfolgreich erreicht.


# 9. Array-Funkrionen(min. foreach(), map(), filter(), ...)

## 9.1 foreach()
Die foreach() Funktion führt für jedes Element im Array eine vorgegebene Funktion aus

```js

let numbers = [1, 3, 4, 9, 8];

// function to compute square of each number
function computeSquare(element) {
  console.log(element * element);
}

// compute square root of each element
numbers.forEach(computeSquare);

/* Output:
1
9 
16
81
64
*/
```

## 9.2 map()
Die map() Funktion erstellt ein neues Array mit den Ergebnissen des Funktionsaufrufs für jedes Array-Element

```js

let numbers = [2, 4, 6, 8, 10];

// function to return the square of a number
function square(number) {
  return number * number;
}

// apply square() function to each item of the numbers list
let square_numbers = numbers.map(square);
console.log(square_numbers);

// Output: [ 4, 16, 36, 64, 100 ]
```

## 9.3 filter()
Die filter() Funktion  gibt ein neues Array zurück, dass alle Elemente enthält, die eine angegeben Filterfunktion bestehen.

```js

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// function to check even numbers
function checkEven(number) {
  if (number % 2 == 0)
    return true;
  else
    return false;
}

// create a new array by filter even numbers from the numbers array
let evenNumbers = numbers.filter(checkEven);
console.log(evenNumbers);

// Output: [ 2, 4, 6, 8, 10 ]
```

für noch mehr auf den Link klicken
https://www.programiz.com/javascript/library/array


