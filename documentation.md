# Documentation
This is the documentation for this repo. We based our intial structure and notation off of the [standard convention for the Rubik's Cube](http://www.rubiksplace.com/move-notations/).

## Rubik's Cube Representation
All of the modules involved in the representation of the cube are in the [r_cube](https://github.com/owencqueen/final_project_302/tree/master/r_cube) directory.
- The class definition for the Rubik's Cube can be found in the [template_class.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/template_class.py) file. 
- Member functions can be found in the [cube.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/cube.py) file. 
- Functions to help with our solvers, as well as other programs, are contained in the [solver_helpers.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/solver_helpers.py) file. 
### Cube Dimension
![2x2x2 Rubik's Cube](https://www.grubiks.com/images/puzzles/17/small.png) </br>
Stored in the "dim" variable is the dimensions of the cube. Currently the only supported dimension is 2x2x2, but, if we had more time, we considered extending our model to 3x3x3.
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

### Color codes

| Char | Color |
| ---- | ----- |
| r | Red|
| o | Orange |
| w | White |
| y | Yellow |
| g | Green |
| b | Blue |
### Faces Represented as 2D Arrays
These are the initial values of each face as intialized in the constructor in [template_class.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/template_class.py). </br>
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
All move functions are implemented in [cube.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/cube.py) (see under "Backend Cube Implementation" below). </br>
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
The [recursive_solver.py](https://github.com/owencqueen/final_project_302/blob/master/recursive_solver.py) file contains the implementation of a recursive solver to the Rubik's Cube. This solver works in a similar style as Dr. Plank's [sudoku solver](http://web.eecs.utk.edu/~jplank/plank/classes/cs140/Notes/Sudoku/index.html) works.</br>
</br>
After testing this solver, we quickly realized that this solution would not be practical. For many reasons such as general time complexity of the solver, we abandoned this brute-force technique. However, the file has been left in the repo for reference.
### CNN Solver
When we began this project, we intended to explore using reinforcement learning (RL) to build a solver for the Rubik's Cube. However, after we started researching, we realized that developing a model using RL techniques would be far too time consuming and would require more advanced knowledge of machine learning than we possessed, or had time to learn. Thus, we decided that supervised learning may be the better approach due to the wider availability of Python libraries specifically for supervised rather than unsupervised learning. </br>

After much research, we were able to develop a supervised learning model built on deep neural networks. This model is based on a convolutional neural network ([CNN](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)), a type of neural network typically used for image processing. The inspiration for this came from a similar implementation of a [CNN for a sudoku solver](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11). </br> </br>

All of the files associated with building the CNN solver are in the [cnn_solver](https://github.com/owencqueen/final_project_302/tree/master/cnn_solver) directory. </br>

Here is the process by which we developed this model:

#### 1. Generating data
Our first approach to this problem was to generate a data set by recording the moves by which we shuffled the cube, and recording the initial state of the cube along with the series of moves by which we would solve the cube. The original data set can be found in [old_data.csv](https://github.com/owencqueen/final_project_302/blob/master/example_data/old_data.csv). However, this posed several problems for our model, the primary problem being the output of the data set. </br>

CNN's work best when they have a definite set of outputs. In other words, CNN's are not good at generating original output. Thus, our model was going to have a hard time generating a solution to a shuffle permutation it had not seen before. Consider the following:

```
Math about how many permutations there are
```
Thus, it was decided that we needed a finite output space for our model. Naturally, we thought that the possible moves on the cube (see previous references) would serve as an appropriate output space. In the [sudoku solver](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11), Verma ran into a similar problem with his model, so he took the approach of attempting to solve the sudoku board one square at a time. This strategy was effective for him, so we decided to pursue a similar strategy in our model. </br> </br>

So, we decided on generating a data set that included one move at a time. The goal was that if the model saw enough moves on the cube at different permutations, it would learn how each move manipulated the cube and which moves were effective at solving the cube at different permutations. The CNN lends well to detecting complex patterns within the input data, so this strategy seemed to be advantageous with our choice of methodology. </br> </br>

Our final input data looked like this: </br>
![one_by_one screenshot](https://github.com/owencqueen/302_final_project/blob/master/doc_supplements/one_by_one-screenshot.png)
</br>

The state of the cube is stored in the "state" column, and the move in response to this state is stored in the "move" column (see Standard Indexing System below). </br>

This is the data which our model would train on.

#### 2. Processing data
The function for the processing of the data is in the //////process_data.py file. This file must read in our data from the csv to a pandas dataframe and then convert it into a numpy array (the format by which the Keras model expects the data). </br></br>

One additional step we had to work through was converting the character data of the cube into numerical data for the ML model. This was done by using helper functions written in solver_helpers.py. </br></br>

This file is necessary to the building of our model in //////model.py.

#### 3. Building the model
The model is built in the file model.py (within the same function by which it is trained and compiled).

#### 4. Training the model

#### 5. Testing the model

##### model_tester.py

##### model_tester_random.py
This model was built to combat some downfalls of relying only on our machine to solve the cube. 

#### Results
Although we received relatively poor accuracies from the training of our model, we anticipated that our model would produce more accurate results in the long run (since our model relied not on the one-step performance of our model but rather how it performed succesive moves). After running our testers several times here are our conclusions.


To run the model and create other models:
1. Get your data
- You can do this by either runnning rs_one.py or by downloading the 'one_by_one.csv' data set from the Google drive (link in README).
3. Create a directory called "models"
2. Run obo_model_driver.py
- Set the batch size and epoch number
- Specify the name of the file to be stored in "models" directory
### Machine Learning Solver
#### Data 
##### Generation
We generated this data in the file [reverse_shuffle.py](https://github.com/owencqueen/302_final_project/blob/master/reverse_shuffle.py). This file works by prompting the user as so:
```
How many rotations? 
How many shuffles? 
```
Rotations denotes the maximum number of times the cube will be rotated when being shuffled. Shuffles denotes the number of shuffles that are performed for each number of rotations in a shuffle. For example, if 20 rotations and 10 shuffles are specified, the program will perform 10 iterations of k rotation(s) shuffles, for k = 1, 2, ..., 20. Thus, the total number of trials performed would be 200 (20 x 10). 
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
2.  
 
## Backend Cube/ Solvers Implementation
All backend implementation of the Rubik's Cube workings is in cube.py. </br>
All of the rotation functions came down to two main functions: rotate and check_cube. Each move function calls rotate which then calls check_cube.
### Rotate
Rotate simply moves all of the colors on one face in either a clockwise or counterclockwise direction. Given a face, this function performs the rotation of each color on that face in the specified direction
### Check_cube
This function is called after the rotation of colors on one face. After the main rotation, this function decides which faces are adjacent to the previously rotated face, and then it rotates the colors on those adjacent faces in the same manner as the previous face was rotated.

### Solver_helpers
This file contains many of the functions that were used to help in writing the solvers, including the CNN model.

#### Standard indexing system:
This was the standard method for representing the moves of the cube in characters and integer values.

| Move        | Index     | Character name | Character name adj. |
| -------     | --------- | -------------- | ------------------- |
| front       | 0         | F  | F |
| front_prime | 1         | F` | f |             
| back        | 2         | B  | B |
| back_prime  | 3         | B` | b |
| up          | 4         | U  | U |
| up_prime    | 5         | U` | u |
| down        | 6         | D  | D |
| down_prime  | 7         | D` | d |
| left        | 8         | L  | L |
| left_prime  | 9         | L` | l |
| right       | 10        | R  | R |
| right_prime | 11        | R` | r |
| null_move   | 12        | 0  | 0 |

#### 1. random_move
```
random_move(cube)
```
- General purpose:
	- Performs a single random move on a given rubiks_cube() object
- Inputs:
	- cube: rubiks_cube() object for which you will perform the random move on
- Return value(s):
	- No return, just a by reference modification of the cube passed as the argument

#### 2. moves
```
moves(cube)
```
- General purpose:
	- Returns move functions for a given rubiks_cube() object
- Inputs:
	- cube: singular rubiks_cube() object
- Return values(s):
	- mvs: An array of functions for that given cube, based off of the standard indexing system

#### 3. names_of_moves
```
name_of_moves()
```
- General purpose:
	- Returns an array of character names of moves (not adjusted)
- Inputs:
	- No inputs
- Return values(s):
	- Array of character names

#### 4. flatten_faces
```
flatten_faces(rc)
```
- General purpose:
	- Converts the state of a rubiks_cube() into a one-dimensional string
	- For use in building csv data for training the models
- Inputs:
	- rc: rubiks_cube() object
- Return values(s):
	- flat: One standardized string of the following format:
```
s = flatten_faces(rc)
s indices:
              +-------------+
              | s[16] s[17] | 
              | s[18] s[19] |
+-------------+-------------+-------------+-------------+
| s[6]  s[7]  | s[0]  s[1]  | s[2]  s[3]  | s[4]  s[5]  |
| s[14] s[15] | s[8]  s[9]  | s[10] s[11] | s[12] s[13] | 
+-------------+-------------+-------------+-------------+
              | s[20] s[21] | 
              | s[22] s[23] |
              +-------------+
```
See representation standards above for the orientation of this diagram.

#### 5. counter_move
```
counter_move(char_name)
```
- General purpose:
	- Gets the opposite move of the input
- Inputs:
	- char_name: Character name of a move (not adjusted)
- Return values(s):
	- Returns the opposite move of the given input
	- Ex: if input is F, returns F`
	- Also: if input is F`, returns F


#### 6. counter_move_f
```
counter_move_f(r, char_name)
```
- General purpose: 
	- Returns a counter function for the given cube that matches the character name (not adj.)
- Inputs:
	- r: rubiks_cube() object
	- char_name: Character name of the move you want the function for
- Return values(s):
	- Counter function based off of the given character name
	- The return function is callable, i.e. not called by the function
	- Ex:
```
f = counter_move_f(rc, ‘B’) # Assigns rc.back to f
f()                         # Calls rc.back_prime()
```

#### 7. get_move
```
get_move(r, char_name)
```
- General purpose:
	- Returns a move based directly off of the character name (not adj.)
- Inputs:
	- r: rubiks_cube() object
	- char_name: Character name (or index) of the move you are requesting (based off of the standardized indexing system above)
	
- Return values(s):
	- Callable function based off of the corresponding character name (or number)
	- Similar to example above (counter_move_f)


#### 8. ch_to_num
```
ch_to_num(ch)
```
- General purpose:
	- Turns a character from the faces of the cube into the number system
- Inputs:
	- ch: character abbreviation of color
- Return values(s):
	- Returns a numerical value based off input for the machine learning model
	- Conversion:
	
	| Color code | Numerical value |
	| ---------- | --------------- |
	| 'w'        | -1.5            |
	| 'r'        | -1              |
	| 'b'        | -0.5            |
	| 'o'        | 0.5             |
	| 'g'        | 1               |
	| 'y'        | 1.5             |

#### 9. two_dim_data
```
two_dim_data(ring)
```
- General purpose:
	- Two-dimensionalizes the string representation of the cube
- Inputs:
	- ring: (short for string) string representation of the current state of the cube
- Return values(s):
	- numpy array of numerical representations of each face
	- Array of dimension 2x12

## User Interaction

