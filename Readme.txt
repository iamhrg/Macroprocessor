                                                                             << WELCOME TO *OUR* MACRO PROCESSOR >>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


=> This macro pre-processor has been designed to be as user-friendly as possible. It has the capability to process multiple nested macros with multiple parameters for different high-level
 languages such as C and Python.



 THE SALIENT FEATURES OF *OUR* MACRO PRE-PROCESSOR INCLUDES:

->  Implementation of line macro definitions.

->  Nested Macro application.      

->  Passing of multiple parameters in pre-defined functions and expanding its operation.

->  Implementation of conditional statements in macros.       

->  Removal of comments entered by users without affecting the actual code.

->  Multiple language code can be pre-processed within the same text-file at the same time.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                                                                          << INSTRUCTIONS TO USE *OUR* MACRO PROCESSOR >>



**The language being used to write the code has to be specified before the start of the code itself.
 
  For C Language: /C

  For Python Language: /P

- The macro processor will detect the end of the code itself.

- Code segments of different languages can be written in the same file and macro processed simultaneously using the above instruction.

  For example--
  /C
  
							(enter code here)
  


  /P            					(signifies end of c code and start of py code)




  

				  (if it detects no other language string, it will automatically end the process and process the code above it)

 ***Every word in the code shall be followed by a white space for better readability of the code.

=> LINE MACRO DEFINITIONS: 


	1. For macros which do not take any parameters.

        -> #define to start the macro, followed by a space (this is for the pre-processor to recognize that a definition is being made)

        -> A space followed by macro name (can be any variable)

        -> A space followed by v followed by the value you want to assign to the particular macro.

        **for example- definition to assign the macro "int" a value of "20" will be as follows: #define int v 20

        -> The user can call the macro by just using the macro name such as : int , this will expand as : 20.


	2. For macros which take parameters.

        -> As we are defining a macro so it starts with #define followed by a space.

        -> Now we define the name of the macro followed by a space and then the parameters taken by it in enclosed curved brackets.

        -> Followed by a space is the operation that is to be performed using the parameters.

        **for example- definition to assign the macro "int" parameters (a,b,c) and performing the operation a*b+c : #define int (a,b,c) a*b+c

        -> For the above example, the user can call the macro using the name "int" and defining its parameters as any value suitable to the user.
        
        **for example- the user can call the macro as : int (x,y,z) which results to : x*y+z as the output


=> NESTED MACRO:


        -> Define a macro as you did for line macro definition.

        -> Use the same macro you defined earlier inside another macro. 

        **for example- if you want to enter the macro "int" defined earlier in another macro "xyz" then: #define int v 20
													 #define xyz v int

        
        -> Here the macro "int" is nested under the macro "xyz".

        -> The user can call the macro as : xyz , this in the first pass will result as : int , and since "int" is again a macro
           a second pass will take place and result as : 20 , since 20 is not a macro so the processor will terminate here.

        -> This was an example of single level nested macro, in a similar manner n levels can also be defined.


=> CONDITIONAL MACRO STATEMENTS:


         -> This macro processor evaluates two conditional statements : #ifdef and #ifndef
         
         -> #ifdef is the keyword used to perform a certain operation (here , a print statement) if the given macro is defined.

         **for example- #ifdef int Defined , this will check whether the macro int is defined , if yes then it prints "Defined".   

         -> In a similar manner, #ifndef is the keyword used to perform a certain operation (here , a print statement) if the given macro is not defined.
     
         **for example- #ifndef int Not Defined , this will check whether the macro int is not defined , if yes then it prints "Not Defined".

=> REMOVAL OF USER INPUT COMMENTS:


         -> Keeping it user friendly , *OUR* macro processor can understand the comments in the same way as in C or Python.

         -> Like in C , we define comments by starting it with '//' character and by '#' in Python.

	 -> *OUR* macro processor removes the user input comment without affecting the program necessary code. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                          << SAMPLE INPUT FOR C AND PYTHON >>


=> SAMPLE INPUT IN C:
       
/C
#include <stdio.h>
#define max v 100
#define min v max 
#define avg v min
#define lst v avg
#define qwe v lst
#define mdf (a,b,c,d,e) a*b+c/d-e
int main()
{
int i1 = max ;
int j1 = min ;       //Comment1
int k1 = avg ;          //Comment2
int l1 = lst ;
int m1 = qwe ;
mdf (v,w,x,y,z)
#ifdef max Defined!
#ifndef rty Undefined!
printf ("%d" , t) ;
}


=> SAMPLE OUTPUT IN C AFTER EXPANSION:
       
/C
#include <stdio.h>
int main()
{
int i1 = 100 ;
int j1 = 100 ;       
int k1 = 100 ;          
int l1 = 100 ;
int m1 = 100 ;
v*w+x/y-z
Defined!
Undefined!
printf ("%d" , t) ;
}


___________________________________________________________________________________________________________________________________________________________________________________________


=> SAMPLE INPUT IN PYTHON:
       
/P
#define sum v 50
#define dif v sum 
#define quo v dif
#define dfe (a,b,c,d) a*b+c/d
i1 = sum
j1 = dif      #Comment1
k1 = quo          #Comment2
dfe (v,w,x,y)
#ifdef sum Defined!
#ifndef uiop Undefined!
print "Hello"


=> SAMPLE OUTPUT IN PYTHON AFTER EXPANSION:
       
/P
i1 = 50
j1 = 50      
k1 = 50          
v*w+x/y
Defined!
Undefined!
print "Hello"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This Macro Processor has been designed in Python Language. 

Made By:
1) HARSH GANDHI (2015UCP1011)
                                                                                         THANK YOU!
----------------------------------------------------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxx-------------------------------------------------------------------------------------

























































            



