# Documentation
This is the documentation for this repo. We based our intial structure and notation off of the [standard convention for the Rubik's Cube](http://www.rubiksplace.com/move-notations/).
## Rubik's Cube Representation
The class definition for the Rubik's Cube can be found in the template_class.py file. Member functions can be found in the cube.py file. 
### Cube Dimension
Stored in the "dim" variable is the dimensions of the cube. Currently the only supported dimension is 2x2x2, but we have considered extendind our model to 3x3x3 (the standard size).
### Orientation
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
                  +-----------------+
                  | u[0][0] u[0][1] | 
                  | u[1][0] u[1][1] |
+-----------------+-----------------+-----------------+-----------------+
| l[0][0] l[0][1] | f[0][0] f[0][1] | r[0][0] r[0][1] | b[0][0] b[0][1] |
| l[1][0] l[1][1] | f[1][0] f[1][1] | r[1][0] r[1][1] | b[1][0] b[1][1] | 
+-----------------+-----------------+-----------------+-----------------+
                  | d[0][0] d[0][1] | 
                  | d[1][0] d[1][1] |
                  +-----------------+
```

### Color codes:

| Char | Color |
| ---- | ----- |
| r | Red|
| o | Orange |
| w | White |
| y | Yellow |
| g | Green |
| b | Blue |
### Faces Represented as 2D Arrays
These are the initial values of each face as intialized in the constructor in [template_class.py](https://github.com/owencqueen/302_final_project/blob/master/template_class.py). </br>
Here is the initial state and orientation of each face. This is based off of our standard convention for the setup of the cube found above under the "Documentation" heading. </br>
#### Front face
```
f = [ ['r', 'r'],
    ['r', 'r'] ]
```
#### Back face
```
b = [ ['o', 'o'],
    ['o', 'o'] ]
```
#### Up face
```
u = [ ['w', 'w'],
    ['w', 'w'] ]
```
#### Down face
```
d = [ ['y', 'y'],
    ['y', 'y'] ]
```
#### Left face
```
l = [ ['g', 'g'],
    ['g', 'g'] ]
```
#### Right face
```
r = [ ['b', 'b'],
    ['b', 'b'] ]
```
## Move Functions
All move functions are implemented in [cube.py](https://github.com/owencqueen/302_final_project/blob/master/cube.py) (see under "Backend Cube Implementation" below). </br>
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
 - Each function, when called as a member funcion on a declared rubiks_cube object, takes no argument. </br>
    - Example:
    ```
    rc = rubiks_cube() # Declaring the object
    rc.front()         # Calling the function to perform F move
    ```
 - All functions are formatted in the the standard Rubik's Cube notation, which can be found in the link under the "Documentation" header. </br>
## Solvers
### Recursive Solver
### Machine Learning Solver
#### Data 
##### Storage
The data for this project was stored in .csv files (written using Python csv module). The csv files are of the following general format: 
```
state, moves
rrwb....byy, F
rryb....gyy, f
```
Which is outputted in csv format as: </br>
![Example of data in csv file](https://github.com/owencqueen/302_final_project/blob/master/data_pic.png)
</br>
###### Notes on storage
- The column named "state" is the starting state of the cube after shuffle. </br>
- The column named "moves" is the code for the moves made by the solver to achieve a solution. </br>
- If a move is capitalized, it is not a prime move. </br>
- If a move is lowercase, it is a prime move.
##### Data Compression
To compress the data to fit easily in the .csv file, there is:
1. flatten_faces ([solver_helpers.py](https://github.com/owencqueen/302_final_project/blob/master/solver_helpers.py)): this function takes all the data in the faces within the Rubik's Cube and outputs them into a single string.
2. <function to 
 
## Backend Cube Implementation
All backend implementation of the Rubik's Cube workings is in cube.py. </br>
All of the rotation functions came down to two main functions: rotate and check_cube. Each move function calls rotate which then calls check_cube.
### Rotate
Rotate simply moves all of the colors on one face in either a clockwise or counterclockwise direction. Given a face, this function performs the rotation of each color on that face in the specified direction
### Check_cube
This function is called after the rotation of colors on one face. After the main rotation, this function decides which faces are adjacent to the previously rotated face, and then it rotates the colors on those adjacent faces in the same manner as the previous face was rotated.
## User Interaction
