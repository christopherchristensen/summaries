# WEBLAB Notizen

## Javascript

<img src="img/historyjs.png" style="width:300px"/>

### Strict Mode

* `"use strict";` zuoberst im JS-File.
* Verlangt dass man,
	* Variablen deklariert (`var`)
	* Objekte deklariert
	* und vieles mehr ...

### Objekte, Object Literals

* Deklaration:

```javascript
var bachelorModule = {title: "WebApplication Development", instructor: "Thomas Koller"};
```

* Properties hinzufügen	

```javascript
bachelorModule.credits = 3;
```

* Properties löschen

```javascript
delete bachelorModule.credits;
```

* Getters / Setters ES5

```javascript
var otherModule = {course: "WebApp",semester: "F15",get title() {return this.course + this.semester},set title(value) {}};
```

* Objekt mit `new` erzeugen

```javascript
var masterModule = new Object();
```

* Objekt mit `create` erzeugen

```javascript
var doctoralModule = Object.create(Object.prototype);
```

* Objekt mit anderem Objekt als Prototype

```javascript
var doctoralModule2 = Object.create(bachelorModule);
```

### Arrays

* Sparse Array

```javascript
let a = [];
a[1000] = "thousand";
```

* Array Reduce Beispiel

```javascript
let sum = a.reduce((x, y) => { return x + y; };
```

### Functions

* Function Literal (anonym)

```javascript
let add = (a, b) => { return a + b; };
```

* Function Literal (mit Name)

```javascript
let subtract = function subtract(a, b)  { return a - b; };
```

* Function Declaration Statement

```javascript
function mult(a, b) { return a * b; };
```

### Hoisting

Variablen haben Block Scope und nach oben auf die ersten Linien in ihrem Scope gehoisted.

```javascript
function log () {
	console.log(a); // funktioniert
	let a;
	console.log(b); // funktioniert nicht
}

function declare () {
	let b = 5;
}
```

### Immediate Function Invocation

```javascript
let fiveToThePowerOfTwo = function (x) { return x * x; }(5);
```

### Constructors

```javascript
function Name(vorname, nachname) { 
	this.vorname = vorname; 
	this.nachname = nachname;}

let name = new Name("John", "Doe");
```

### Prototype

*  (Jedes) Objekt enthält (implizit) ein `prototype` Objekt
*  Wird ein Property nicht im Objekt selber gefunden, so wird es (rekursiv) im `prototype` Objekt gesucht
*  Das letzte Objekt (i.e. Object) in der Kette hat den Prototyp `null`
*  Mit Hilfe der Methode Object.getPrototypeOf() (ES5) kann explizit auf den Prototype zugegriffen werden

* Einem Circle-Prototype eine neue Methode zuweisen

```javascript
function Circle() { 
	this.radius = 1; 
	this.center = {x:0, y:0}}

Circle.prototype.draw = function () { 
	console.log("Radius: " + this.radius);};

let circle = new Circle();
c.draw();
```


### The Awful Parts of JS

* Global Variables
* Scope
* Semicolon Insertion
* typeof
* Eval
* Falsy values


### Embedding JS

* Inline `<script></script>`* External File `<script src="something.js"/>`
* HTML event handler* URL mit javascript: protocol

### Verarbeitung von JS

#### Phase 1

1. Dokument wird geladen
2. Code `<script>` wird ausgeführt (synchron, asynchron oder defered)

<img src="img/loadingjs.png" style="width:300px">

#### Phase 2

3. Asynchrone Ausführung durch Event Handler

### Event Handlers

```javascript
window.addEventListener("load", function () => { ... }, false);
```

### Server Requests

#### Example

```javascript
var request = new XMLHttpRequest();
request.open("GET", "data.json" /* url */);
request.setRequestHeader("Content-Type", "text/plain"); 
request.send(null /* body */);
request.onreadystatechange = function() { 
	if (request.readyState === 4 && request.status === 200) {		var type = request.getResponseHeader("Content-Type"); 
		if (type.match(/^text/)) {			// do something with request.responseText()		} 
	}}
```

#### XMLHttpRequest readyState

<img src="img/xmlhttprequestreadystate.png" style="width:300px">

## LAMP

<img src="img/lamp.png" style="width:300px">

### Wie funktioniert PHP?

* Apache (Webserver) leitet http-Requests  für PHP Files an PHP Interpreter weiter
* Seite wird nach Verarbeitung durch Interpreter wieder an Apache geschickt (als HTML Seite)
* Browser sieht PHP nie!

### MySQLi Object Interface

```javascript$db = new mysqli(host, user, password, databaseName);$sql = "SELECT * FROM ... WHERE ..";$result = $db->query($sql);$row = $result->fetch_assoc();echo $row["id"];
```

## HTML

### DOM-Klassenhierarchie

<img src="img/domklassenhierarchie.png" style="width:300px">

## CSS

### Embedding CSS

* Inline Style
* Inline Style Sheets
* External Style Sheets