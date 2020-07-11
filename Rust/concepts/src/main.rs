

// Common programming concepts

fn main() {
    // Variables are immutable by default.
    let x = 1;
    println!("The value of x is: {}", x);

    // We can make them mutable with "mut":
    let mut y = 1;
    println!("The value of y is: {}", y);
    y = 3;
    println!("The value of y is: {}, y");

    /* Constants are like always-immutable variables, plus
    we must always specify their type on assignment.
    They are usually written in all caps */

    const MAX_POINTS: u32 = 100_000;

    // We can "let" multiple times the same variable, shadowing the older ones:
    let x = 2;
    let x = 13;
    let x = 0;
    println!("The value of x is: {}", x)
    /* This way, we can reuse the variable name multiple times.
    This can also be sued to change the variable's type, which is not allowed
    if the variable is a simple "mut" */

    let spaces = "     ";
    let spaces = spaces.len()  // This changes from str to int

    /* ~~~~~~~~~~~~~~~
        Data Types
    ~~~~~~~~~~~~~  */

    /* 1: Scalar
    Scalar types are integers, floating points, bools and chars. 
    They contain a single value */

    /* ints

    A number without a fractional part. They are either signed (i) or unsigned (u).
    Can have various sizes, and the size is explicit - 8, 16, 32, 64 or 128 bits are supported
    The possible sizes of a signed int are from -(2^n-1) to +(2^n-1) -1, both inclusive, and for
    an unsigned int are from 0 to 2^n -1, both inclusive.

    Instead of giving a size we can give "isize" and "usize", so that the program uses
    the machine's own system type, either 32 or 64 bits.

    We can write them as many forms. For decimal, we needn't specify their form. We can
    also write them in hexadecimal (0x), octal (0o), binary (0b) and byte (only for u8, b'-').

    Ints can overflow and wrap. It is considered a bug when cargo compiles with --debug, but
    are ignored otherwise. So, be careful.

    The default int type is u32.
    */

    let x: u32 = 100_000_231
    // 4294967295 is the max value 

    /* floats
    Floating points are similar to integers, but can have a decimal part. The notation is
    "f<size>". Default is f64, which is as fast as f32, but has more precision. */

    let x: f32 = 3.21
    let y: f64 = 12.33

    // Operations
    let sum = 5 + 10;
    let difference = 95.5 - 4.3;
    let product = 4 * 30;
    let quotient = 56.7 / 32.2;
    let remainder = 43 % 5;

    /* Bools
    Are big one byte. */
    let t = true;
    let f: bool = false;

    /* Char
    a single bit of text, as represented in the Unicode (so it includes emojis).
    It spans 4 bytes. */

    let c = 'z'; // Notice the single quote, instead of double quotes

    /* Compound types
    Tuples: several types but with fixed length.*/

    let tup: (i32, f64, u8) = (500, 6.4, 1); // The type declarations are optional
    let tup: (33, 6.4, 'a');

    // We can unpack the tuples in single variables ("destructuring")
    let (x, y, z) = tup;
    println!("The value of y is: {}", y);

    // Or access it with the dot notation (zero-indexed)
    let tup = (1, 2, 3);

    println!("The first item is: {}", tup.0);
    println!("The second item is: {}", tup.1);

    // Arrays: Single types and fixed length
    let arr: [i32; 3] = [3, 12, 22]; // The type is type; nr. of items
    let arr = [5; 3]; // This is equal to:
    let arr = [5, 5, 5];

    // Can access using indexing:
    let first = arr[0];
    let second = arr[1];

    /* Trying to access an element in a position which is higher than the
    array lenght will panic *at runtime*, but not at compile time. */
}

/* Functions

Defined with "fn", brackets and curly brackets with the function body.
You **must** declare the types of the parameters (arguments) of the function
at the function definition. 

Function names use snake_case */

fn my_function(x: i32) {
    println!("The value of x is {}:", x)
}

/* Functions contain STATEMENTS and EXPRESSIONS.

A statement is an instruction that does something and doesn't return anything.
An expression is an instruction that does something and then returns something else. */

fn this_name() {
    let x = 5; // This is a statement
    // "let" doesn't return a variable, so you can't assign a let to another let

    let x = 3;

    let y = {
        let x = 3;
        x + 1  // This is an expression, as it returns a value. Expressions don't have an ending ;
    }; // This {} is a *block* that evaluates to 4. 

    // A function, by default, returns the value of its last expression.

} // Defining a function is also a statement

fn five() -> i32 { // The return type of this function is specified.
    5
}

// The above function returns 5, as the 5 is an expression that returns itself.

fn plus_one(x: i32) -> i32 {
    x + 1 // Remember: no semicolon
    // If we write x + 1;, the function wouldn't return anything.
}

fn should_be_main() {
    let x = plus_one(5);

    println!("The value of x is {}", x); // Is 6. It's 6
}

// Control flow tools

fn should_be_main2() {
    let x = 3;

    if number < 5 { // This accepts anything that evaluates to a bool.
        println!("The condition is true")
    } else {  // The else is optional.
        println!("The condition is false")
    }

    // Can also use elseif

    if number % 4 == 0 {
        println!("The value was divisible by 4");
    } else if number % 3 == 0 {
        println!("The value was divisible by 3");
    } else {
        println!("The value was not divisible by 3 or 4");
    }

    // If you get in a situation where you need many elseif, considering using a match expression.

    // if is an expression, sow e can sue it as any other expression, like "5":

    let x = if true {
        5
    } else {
        6
    }; // This will place 5 inside of x, and is prefectly valid.

    // Note that for something like this to work, the two arms must return the same type
    // This is beacuse Rust needs to know the type of each variable to make sure we use it
    // preperly everywhere.

    // Loops
    // Rust has 3 loops:

    // loop runs forever, until something breaks out if it.
    loop {
        println!("I'll do it again!")
    }

    let mut counter = 1;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter *2;
        }
    }
    // In this case, result = 20

    // while runs until the condition stops being true:

    let mut number = 3;
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }

    // This prints 3!, 2!, 1!

    // for loop

    let a = [10, 20, 30, 40, 50 , 60]

    for element in a.iter() {
        println!("The value is: {}", element);
    }

    // When you use a loop, you most always end up using a for loop, together
    // with a range construct, which is a concised way to make a tuple of values.

    for number in (1..4).rev() {
        println!("{}!", number);
    }
    // This prints 4!, 3!, 2!, 1!

}