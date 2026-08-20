--- String indexing (part 1) ---

name = "OMKAR"
python sees:
character : O M K A R
Index     : 0 1 2 3 4

print(name[0])
O
print(name[3])
A


--- Negative indexing (part 2) ---


word = "PYTHON"

The indexes are:

 P   Y   T   H   O   N 
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1

print(word[-1])
N
print(word[-5])
Y


--- String slicing (part 3) ---


word = "PYTHON"
print(word[0:3])

Think of
P Y T H O N
0 1 2 3 4 5 

word[0:3] means:
start at index 0, stop before index 3.
so it takes
P Y T    ( IMPORTENT RULE )  -> The start is included, but the stop is excluded.


--- String Slicing with a step ---


word = "PYTHON"
print(word[0:6:2])     -> REmember [start : stop : step]

[0:6:2] means:
*start at 0 -> P
*jump by 2  -> T
*jump by 2  -> O
*stop before 6

so output would be -> PTO


--- Reverse string ---

  word = "ROBOTICS"
PRINT(WORD[::-1])

S C I T O B O R

Reversed

R O B O T I C S
S C I T O B O R



--- I HAVE LEARNED TODAY ---


POSITIVE INDEXING  -> word[0]
NEGATIVE INDEXING  -> word[-1]
SLICING            -> word[start:stop]
SLICING WITH STEP
WORD[start:stop:step]
REVERSE            -> word[::-1]




