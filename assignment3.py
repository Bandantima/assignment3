#Qu1.what are function advantageous to have in your program?
#Ans: Advantages to have function in progran are following:
      1. It reduces chances of error.
      2. Increases progran readability.
      3.This makes program shorter.
      4.It divides a complex program into simpler one.
      5. Avoid repetition of code .

#Qu2.When does the code in a function run.When its specified or when its called?
Ans: When a function is called, the program control jumps to the function definition and executes the code inside the
     function body.After executing the body of the function ,the program control jumps back to the part of the program
     which called the function ,and resumes execution at that point.

#Qu3.What statement creates a function?
Ans: A function is called with the def keyword .The statements is the block of the function must be intended .The def
     keyword is followed by the function name with round brackets and a colon.

#Qu4.What is the difference between a function and a functional call?
Ans:                  Function                                           Function call
    1.A function is a block of code that does a      1. A function cell is the code used to pass control to a
     particular operation and returns a result         function.
    2.e.g Function add(a,b)                          2. b=add(5,6)
             return a+b
    3.A function should have is name and             3.In a function call,there will be a semicolon too.
      paranthesis bracket.

#Qu5. How many global scopes are there in a Python program? How many local scopes?
Ans: There is one global scope,and a local scope is created whenever a function is called.

#Qu6. What happens to variables in a local scope when the function call returns?
Ans: When a function returns ,the local scope is destroyed and all the variables in it are forgotten.

#Qu7. What is the concept od return value?Is it possible to have a return value of a call to that function?
Ans: A return value is the value that a function call evaluates to .like any value,a return value can be used as part
     of an expression .

#Qu8. If a function does not have a return statement ,what is the return value of a call to that function?
Ans: If there is no return statement for a function ,its return value is None.

#Qu9. How do you make a function variable refer to the global variable ?
Ans: A global statement will force a variable in a function to refer to the global variable.

#Qu10:What is the data type of None?
Ans: The data type of None is NoneType.

#Qu11:What does the sentence import areallyourpetsnamederic do?
Ans:That import statement imports a module named areallyourpetsnamederic.

#Qu12:If had a bacon() feature in aspam module,what would you call it after importing spam?
Ans:This function can be called with spam.bacon()

#Qu13:What can you do to save a programme from crashing if it encounters an error?
Ans: Place the line of code that might cause an error in a try clause.

#Qu14:What is the purpose of the try clause? What is the purpose ofthe except clause?
Ans:The code that could potentially cause an error goes in the try clause.
    The code that executes if an error happens goes in the except clause.  