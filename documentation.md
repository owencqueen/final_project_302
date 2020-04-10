# Documentation
This is the documentation for this repo. We based our intial structure and notation off of the [standard convention for the Rubik's Cube](http://www.rubiksplace.com/move-notations/).
## Rubik's Cube Representation
The class definition for the Rubik's Cube can be found in the template_class.py file. Member functions can be found in the cube.py file. 
### 1. Face representations
Here is the initial state and orientation of each face. This is based off of our standard convention for the setup of the cube found above under the "Documentation" heading. </br>
#### Orientation
Orientation in space based off of conventional 2D representation of the cube [found here](https://www.codewars.com/kata/5b3bec086be5d8893000002e):
```
      +-----+
      |  u  | 
      |     |
+-----+-----+-----+-----+
|  l  |  f  |  r  |  b  |
|     |     |     |     | 
+-----+-----+-----+-----+
      |  d  |
      |     |
      +-----+
```
If you want to access the individual blocks in the cube, you can use the below map for the indices. This map corresponds to the above codes for each face.
```
                +---------------+
                | [0][0] [0][1] | 
                | [1][0] [1][1] |
+---------------+---------------+---------------+---------------+
| [0][0] [0][1] | [0][0] [0][1] | [0][0] [0][1] | [0][0] [0][1] |
| [1][0] [1][1] | [1][0] [1][1] | [1][0] [1][1] | [1][0] [1][1] | 
+---------------+---------------+---------------+---------------+
                | [0][0] [0][1] | 
                | [1][0] [1][1] |
                +---------------+
```

#### Color codes:

| Char | Color |
| ---- | ----- |
| r | Red|
| o | Orange |
| w | White |
| y | Yellow |
| g | Green |
| b | Blue |
#### Initial values of each face
These are the initial values of each face as intialized in the constructor.
##### Front
- f in template_class.py
```
[ ['r', 'r'],
  ['r', 'r'] ]
```
##### Back
- b in template_class.py
```
[ ['o', 'o'],
  ['o', 'o'] ]
```
##### Up
- u in template_class.py
```
[ ['w', 'w'],
  ['w', 'w'] ]
```
##### Down
- d in template_class.py
```
[ ['y', 'y'],
  ['y', 'y'] ]
```
##### Left
- l in template_class.py
```
[ ['g', 'g'],
  ['g', 'g'] ]
```
##### Right
- r in template_class.py
```
[ ['b', 'b'],
  ['b', 'b'] ]
```
### 2. Move Functions

  | Class Syntax | Standard Notation |
  |---------------| ------------------|
  | front()       | F                 |
  | front_prime() | F'                |
  | back()        | B                 |
  | back_prime()  | B'                |
  | up()          | U                 |
  | up_prime()    | U'                |
  | down()        | D                 |
  | down_prime()  | D'                |
  | left()        | L                 |
  | left_prime()  | L'                |
  | right()       | R                 |
  | right_prime() | R'                |
 - Each function, when called as a member funcion on a declared object, takes no argument. </br>
    - Example:
    ```
    rc = rubiks_cube() # Declaring the object
    rc.front()         # Calling the function to perform F move
    ```
 - The standard Rubik's Cube notation can be found in the link under the "Documentation" header. </br>
 
3. 

### Interacting with the cube
## Solvers
1. 
### Recursive Solver
## User Interaction
