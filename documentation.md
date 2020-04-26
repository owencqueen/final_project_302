# Documentation
This is the documentation for this repo. We based our intial structure and notation off of the [standard convention for the Rubik's Cube](http://www.rubiksplace.com/move-notations/).

### Contents
1. Rubik's Cube Representation
- Cube Dimension
- Orientation
- Color Codes
2. Move Functions
3. Solvers
- Recursive Solver: [recursive_solver.py](https://github.com/owencqueen/final_project_302/blob/master/recursive_solver.py)
- CNN Solver: [cnn_solver](https://github.com/owencqueen/final_project_302/tree/master/cnn_solver)
4. Backend Cube/ Solvers Implementation
- [cube.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/cube.py)
- [solver_helpers.py](https://github.com/owencqueen/final_project_302/blob/master/r_cube/solver_helpers.py)
	- Standard Indexing System 
5. User Interaction
6. Libraries used

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

After testing this solver, we quickly realized that this solution would not be practical. For many reasons such as general time complexity of the solver, we abandoned this brute-force technique. However, the file has been left in the repo for reference.
### CNN Solver
When we began this project, we intended to explore using reinforcement learning (RL) to build a solver for the Rubik's Cube. However, after we started researching, we realized that developing a model using RL techniques would be far too time consuming and would require more advanced knowledge of machine learning than we possessed, or had time to learn. Thus, we decided that supervised learning may be the better approach due to the wider availability of Python libraries specifically for supervised rather than unsupervised learning. </br>

After much research, we were able to develop a supervised learning model built on deep neural networks. This model is based on a convolutional neural network ([CNN](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)), a type of neural network typically used for image processing. The inspiration for this came from a similar implementation of a [CNN for a sudoku solver](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11). </br>

All of the files associated with building the CNN solver are in the [cnn_solver](https://github.com/owencqueen/final_project_302/tree/master/cnn_solver) directory. Note: another copy of solver_helpers.py is included in this file because we had trouble with importing and packages in Python. </br>

Here is the process by which we developed this model:

#### 1. Generating data
Our first approach to this problem was to generate a data set by recording the moves by which we shuffled the cube, and recording the initial state of the cube along with the series of moves by which we would solve the cube. An example of the original data set can be found in [old_data.csv](https://github.com/owencqueen/final_project_302/blob/master/example_data/old_data.csv). However, this posed several problems for our model, the primary problem being the output of the data set. </br>

CNN's work best when they have a definite set of outputs. In other words, CNN's are not good at generating original output. Thus, our model was going to have a hard time generating a solution to a shuffle permutation it had not seen before. In addition, the idea of training the model to treat the output as labels (for example, UDF would be a series of moves that is a label) would mean that the model would have to have seen every possible series of moves of outputs that it could make. However, this defeats the purpose of training a machine learning model because then we could simply lookup the cube permutation, which would give us a fast solution. </br>

Thus, it was decided that we needed a finite output space for our model. Naturally, we thought that the possible moves on the cube (see previous references) would serve as an appropriate output space. In the [sudoku solver](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11), Verma ran into a similar problem with his model, so he took the approach of attempting to solve the sudoku board one square at a time. This strategy was effective for him, so we decided to pursue a similar strategy in our model. </br> </br>

So, we decided on generating a data set that included one move at a time. The goal was that if the model saw enough moves on the cube at different permutations, it would learn how each move manipulated the cube and which moves were effective at solving the cube at different permutations. The CNN lends well to detecting complex patterns within the input data, so this strategy seemed to be advantageous with our choice of methodology. </br> </br>
##### reverse_shuffle.py
We generated this data in the program [reverse_shuffle.py](https://github.com/owencqueen/final_project_302/blob/master/reverse_shuffle.py) (in the  primary repository). Upon running the program, it prompts the user as so:
```
How many rotations per shuffle? # Self-explanatory
How many shuffles?              # Full iterations to be considered in output file
Name of output file?            # Self-explanatory
```
- The total number of rows in your output file will be (num. shuffles)x(rot. per shuffle). 
- Your output file will be located in the [cnn_solver](https://github.com/owencqueen/final_project_302/tree/master/cnn_solver) directory.</br>

The output data from this program is stored in the following format: </br>
![one_by_one screenshot](https://github.com/owencqueen/302_final_project/blob/master/doc_supplements/one_by_one-screenshot.png)
</br>

- The state of the cube is stored in the "state" column, and the move in response to this state is stored in the "move" column (see Standard Indexing System below). </br>

This is the data which our model would train on.

##### Our data
We worked off of two primary datasets in this project: one_by_one.csv and cube_data.csv (both of which can be found in this public [Google Drive folder](https://drive.google.com/drive/folders/18-pDI7ZcoNsYXTu68iljprL7TQ4-Rgpj?usp=sharing)). We stored the data in a Google Drive folder because the data far exceeded the Github maximum file size. </br>

The first file was one_by_one.csv, which was built with the following parameters:
```
UNIX> python3 reverse_shuffle.py
How many rotations per shuffle? 20
How many shuffles? 100000
Name of output file? one_by_one.csv
```

The second file was cube_data.csv, which was built with the following parameters:
```
UNIX> python3 reverse_shuffle.py
How many rotations per shuffle? 20
How many shuffles? 400000
Name of output file? cube_data.csv
```

#### 2. Processing data
The function for the processing of the data is in the [process_data.py](https://github.com/owencqueen/final_project_302/blob/master/cnn_solver/process_data.py) file. This file must read in our data from the csv to a pandas dataframe and then convert it into a numpy array (the format by which the Keras model expects the data). </br></br>

One additional step we had to work through was converting the character data of the cube into numerical data for the ML model. This was done by using helper functions written in solver_helpers.py. </br></br>

This file is necessary to the model built in model.py.

#### 3. Building the model
The model is built in the file [model.py](https://github.com/owencqueen/final_project_302/blob/master/cnn_solver/model.py) (within the same function by which it is trained and compiled). The structure of this model is based off a similar structure from the [sudoku solver](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11) that we used as a reference. </br>

This model consists of the following structure:
```
(Layer): input -> [Convolution] -> [Convolution] -> [Convolution] -> [Dense] -> output
(Size):	       	      [50]             [50]             [100]          [13]
```
##### Convolutional Layers
The convolutional layers perform a mathematical operation called [convolution](https://en.wikipedia.org/wiki/Convolution) on the input data. These layers are what make these types of networks unique, and this process has been shown to be very effective at detecting both high-level and low-level patterns in the data.
###### Size:
The size of our convolutional layers was relatively arbitrary. We did not do much research into optimizing this section of the network, so we based our structure off of the aforementioned sudoku solver. The third convolutional layer had more nodes that the first two, and that is due to the kernel size which is discussed below.
###### Kernel size:
The kernel is a parameter in the convolution function. Basically, the kernel is a matrix that iterates over the data and performs convolution at each step. Kernel size is important for the detection of patterns within the data. </br>

We chose our kernel size in the following structure:
```
(Layer order):  [1] -> [2] -> [3]
(Kernel size): (2,2)  (2,2)  (1,1)
```
The first two layers consisted 2x2 kernels and the last one consisted of a 1x1 kernel. We made a choice on these sizes thinking that as the data progressed through the model, we should have smaller kernels to pick up smaller patterns.

###### Activation function:
We chose our activation function to be [RELU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)), which has been proven to be very effective on neural networks due to its linear form.

###### Padding:
Padding is explained in much more detail in the article below on CNN's. We chose to use it because this is what the sudoku solver used.

##### BatchNormalization
Some of the sources that we came across claimed that using the [BatchNormalization](https://machinelearningmastery.com/batch-normalization-for-training-of-deep-neural-networks/) function, which normalizes the data in between layers in the network, improves model performance and accuracy. Naturally, we decided to implement this in our model. 

##### Flatten
Most of the models that we referenced in building our model, including the sudoku solver, flattened the data before the Dense layer in their model; therefore, we implemented a similar strategy in our model.

##### Dense layer
The dense layer represents the output layer in our model. It contains 13 nodes because we have 13 possible outputs from our model (see Standard Indexing System below). 

##### Activation
We chose to use [softmax](https://medium.com/data-science-bootcamp/understand-the-softmax-function-in-minutes-f3a59641e86d) as our activation function in this model. This was used by many of the other models that we referenced, and we had found some references that claimed it was highly effective in neural networks (see link in this paragraph).

##### Optimizer
We chose to use the [adam optimizer](https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c) in our model with a learning rate of 0.001. This has been shown to perform better, in some instances, than the popular stochastic gradient descent algorithm. We chose a relatively low learning rate because we discovered that as we increased the learning rate, our model's accuracy was lowered.

##### Compiling the model
We used the compile() function to compile our model. This was the second-to-last step of creating our model.
###### Loss function
We chose spare categorical crossentropy solely because the sudoku model used this same loss function.

For more information on the anatomy and physiology of convolutional neural networks, see [this article](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53) on towardsdatascience.com.

#### 4. Training the model
The model is trained by running the model_driver.py script, which calls the train_obo (function in model.py file). Upon running this script, the user is prompted:
```
Name of new model:     # Self-explanatory
Data to be trained on: # csv file in local directory to train model on
Batch size:            # batch_size
Num epochs:            # epochs  
```
The batch_size and epochs are arguments in the fit() function in model.py. Batch size denotes the number of samples in the data that are to be processed before the internal model parameters are updated. The number of epochs simply denotes the number of times the training process will iterate through the dataset. See [this article](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/) for more information about batch_size and epochs. </br>

We have included two of our trained models in this repository, located in the [cnn_solver/models](https://github.com/owencqueen/final_project_302/tree/master/cnn_solver/models) folder.
##### [oboorg1.model](https://github.com/owencqueen/final_project_302/blob/master/cnn_solver/models/oboorg1.model)
This was the first model that was built, and it was trained on the one_by_one.csv dataset (see above under "Our data"). These were the parameters for the model along with the accuracy results: </br>
![Training oboorg1.model](https://github.com/owencqueen/final_project_302/blob/master/doc_supplements/one_by_one-model-terminal-output.png)
Please note that the name of the file which this program was run on is now "model_driver.py" instead of "obo_model_driver.py". </br>

The final accuracy of this model was 37.51%.
##### [obonew1.model](https://github.com/owencqueen/final_project_302/blob/master/cnn_solver/models/obonew1.model)
This model was trained on the cube_data.csv dataset (see above under "Our data"). This model was built after oboorg1.model. These were the parameters for the model along with the accuracy results: </br>
![Training obonew1.model](https://github.com/owencqueen/final_project_302/blob/master/doc_supplements/cube_data-model-terminal-output.png)
Please note, as is above, that the name of the file which this program was run on is now "model_driver.py" instead of "obo_model_driver.py". </br>

The final accuracy of this model was 38.54%, as was to be expected for running this model on a larger dataset as compared to oboorg1.model.

##### Conclusions after training the model
Neither of our models achieved high accuracy in the initial training stages which would normally be very disappointing. However, because our model is only making individual guesses of moves, we should expect that when it comes to solving the Rubik's Cube, the model should perform better. In other words, our model may make bad individual guesses, but over the series of moves, these guesses may actually be effective. </br>

We chose to use only three epochs because the improvement on the accuracy of the model seemed to diminish after 2-3 epochs.

#### 5. Testing the model

##### [model_tester.py](https://github.com/owencqueen/final_project_302/blob/master/model_test.py)
This tester simply shuffles a Rubik's Cube and then extracts predictions from the model based on the current state of the cube. Upon running this module, the user is prompted with the following:
```
Model to test:
Number of rotations for shuffle:
```
Note: ignore the garbage that is printed after entering your response. This is a result of using the keras/tensorflow modules. </br>
Simply input the name of the model to be tested (i.e. no need to deal with file structure), and then input the number of rotations for which you will shuffle the cube before attempting to solve. </br>

##### [model_tester_random.py](https://github.com/owencqueen/final_project_302/blob/master/model_test_random.py)
This tester was built to combat some downfalls of relying only on our machine to solve the cube. It operates differently from model_tester.py in that if the model predicts repeating, redundant moves, this solver makes a random move. As far as running this tester, it takes the exact same parameters as model_tester.py.

#### Results
Although we received relatively poor accuracies from the training of our model, we anticipated that our model would produce more accurate results in the long run (since our model relied not on the one-step performance of our model but rather how it performed succesive moves). After running our testers several times here are our conclusions.


To run the model and create other models:
1. Get your data
- You can do this by either runnning rs_one.py or by downloading the 'one_by_one.csv' data set from the Google drive (link in README).
3. Create a directory called "models"
2. Run obo_model_driver.py
- Set the batch size and epoch number
- Specify the name of the file to be stored in "models" directory

##### Data Compression
To compress the data to fit easily in the .csv file, there is:
1. flatten_faces ([solver_helpers.py](https://github.com/owencqueen/302_final_project/blob/master/solver_helpers.py)): this function takes all the data in the faces within the Rubik's Cube and outputs them into a single string.
2.  
 
## Backend Cube/ Solvers Implementation
### cube.py
All backend implementation of the rubiks_cube class (in [template_class](https://github.com/owencqueen/final_project_302/blob/master/r_cube/template_class.py)) workings is in cube.py. </br>
All of the rotation functions came down to two main functions: rotate and check_cube. Each move function calls rotate which then calls check_cube.
#### Rotate
Rotate simply moves all of the colors on one face in either a clockwise or counterclockwise direction. Given a face, this function performs the rotation of each color on that face in the specified direction
#### Check_cube
This function is called after the rotation of colors on one face. After the main rotation, this function decides which faces are adjacent to the previously rotated face, and then it rotates the colors on those adjacent faces in the same manner as the previous face was rotated.

### solver_helpers.py
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
### Antoher way to get comfortable with a cube
This interface was useful for testing our object.
    It is based on python version python3
```
usage: python3 Cube_text.py cube_dimensions
```
- What can you do with the interface?
  (typing "help" will show you all the commands)

	- Reset
	- Shuffle
	- Print
	- Check
	- Rotate
- Rotation commands:
	- Commands can be typed in any format, so long as it follows this convention:
	- R or r or R' or r' or R2 or r2 or R'2 or r'2 
		- " ' " (or prime) means opposite direction
		- number is the amount of turns (must be single digit 1-9)
		- commands need no spaces between them
		- if the commands are correct, the rotations will be read in order.


## Libraries:
You can install all of these libraries using [pip](https://pip.pypa.io/en/stable/). For example:
```
UNIX> pip install keras
```
Installs the keras library. You can repeat this for all other libraries.

1. csv 
2. keras (v. 2.3.1)
3. math  
4. numpy (v. 1.18.2)
5. pandas (v. 1.0.3)
6. pygame
7. random
8. scikit-learn (v. 0.22.2.post1)
9. sys
10. tensorflow (v. 2.2.0rc3)
