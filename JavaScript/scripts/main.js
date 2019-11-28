console.log("Hello from JavaScript");
// Inline comment
/* This is a
multiline
comment
*/

/* 1- Data Types:
Undefined, null, boolean, string, number and object
*/

// variable declaration
var myName = "Luca"; // Used by the whole program
myName = 9;

let python = "A bean!"; // Used by the portion that uses it

const pi = 3.14; // Cannot be changed

/* Variables
Normal is camelcase myVariableIsBeautiful
 */
var a; // Declare the variable, but no initialization
var b = 2; // Declare and initialize the variable immediately
a = 4 // No need to further declare when reassigning.
a = b

console.log(a);

var string = "This is a ";
a = string + "string."; // String concatenation
console.log(a);

/* Operators */

var why = 5 + 3; //Sum
var why = 5 - 3; //Substraction
var why = 5 * 3; //Multiplication
var why = 5 / 3; //Division
var why = 1;
why++; //Increment by 1, same as why = why + 1
why += 10 //Increment the variable by 10
why--; //Decrement by 1, same as why = why - 1
why -= 2; //Decrement the variable by 2
why *= 10 //Multiply why by 10 and set it to why
why /= 3 // Same, but division

var aDecimal = 5.6; //A float

var product = aDecimal * 2.5;
var division = aDecimal / 1.3;
var remainder = 5 % 2;

/* Strings */
var myFirstName = "Luca";
var quoteInIt = "This needs to use a \"quote\" and it breaks if not escaped.";
// Escape marks using backslashes. We need to escape only the surrounding
// quotes:
quoteInIt = 'I dont need to escape "this" quotes.'
quoteInIt = "I don't need to escape 'these' quotes"

/* We can escape:
\'
\"
\\
\n (newline)
\r (carriage return)
\t (tab)
\b (backspace)
\f (form feed)
*/

// Concantenation
var longerString = "First part of " + "this sentence.";
console.log(longerString);
// We can also use +=
longerString += " Another bit!";
console.log(longerString);

var myName = "Luca";
var status = "all good.";
var what = "My name is " + myName + ", and I am " + status;
console.log(what);
what = "My name is ";
what += myName;
what += "."
console.log(what)

// Find length

var thisBanana = "Loveme";
var length = thisBanana.length;
console.log(length);

// Using bracket notation to index strings. JavaScript has 0-indexing.
var myName = "Javascript";
myName[0] // "J"
myName[1] // "a"
// Strings are immutable.
// To find the last character of the list is using length
myName[myName.length - 1]; //"t"
myName[myName.length - 3]; //"i"

// Function declaration unsing "function":
function game(noun, adj, verb, adverb){
    var result = "";
    result += "The " + adj + " " + noun + " " + verb + " to my home " + adverb;

    return result;
};

console.log(game("Sapu", "sexy", "came ", "pragmatically."));

// Arrays

var myArray = ["Banana", 23]; // Can contain any data type
myArray = [["Multi", "dimensionality"], ["is very", "very,"], ["awesome!", 12]];

// Access the variables using brackets
myArray = [10,20,30];
myArray[2]; // 30
myArray[1] = 12; // Arrays are mutable
myArray = [[1,2], [3, 4], [5, 6], [1, ["so deep", 2], 3]];
var extracted = myArray[3][1][1]; // 2 (After the "so deep")
console.log(extracted);

// Append to the end of array, push()
myArray = [1, 2, 3];
myArray.push(4, 5, 6);
console.log(myArray);

// Remove and return from the end, pop()
var removed = myArray.pop(); //Pops "6" and removes it from the array.
console.log(myArray);

// Remove and return from the beginning, shift():
myArray = [["A", "B"], ["C", "D"]];
removed = myArray.shift();
console.log(removed)

// Add to the beginning of the array, unshift();
myArray = [6, 2, 3, 4, 5];
myArray.shift()
myArray.unshift(1) // 1, 2, 3, 4, 5

// An example shopping list.
var shoppingList = [["Juice", 2], ["Cereal", 4], ["Eggs", 12], ["Chocolate", 2]];

// Functions

function reusableHello() {
    console.log("Hello World!");
};

// This will say "Hello World" twice.
reusableHello();
reusableHello();
