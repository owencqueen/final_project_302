# Exploring the 2x2 Rubik's Cube
Final project for CS302 at UTK.

### Developers:
[John Greathouse](https://github.com/jgreatho) </br>
[Owen Queen](https://github.com/owencqueen) </br>
[Jared Staman](https://github.com/jstaman5) </br>

Access our Google Drive folder with log information [here].

[here]: https://drive.google.com/drive/folders/1hIw_WaZPfqpyH6AnfTdHOG10UUI7ogju?usp=sharing

This README is a supplement to our [documentation.md](https://github.com/owencqueen/final_project_302/blob/master/documentation.md) file, which contains a detailed explanation of this project as well as how to run every program in the project.

## Introduction
As the title suggests, we decided to tackle the infamous Rubik's Cube with our project. This problem is very simple on the surface, but solving a Rubik's Cube has perplexed humankind since its invention in 1974. This problem is not only difficult to solve for humans, but also for computers. Considered an NP-complete problem, artificial intelligence systems have only [recently been developed](https://www.engadget.com/2019-07-17-ai-rubiks-cube-machine-learning-neural-network.html) that can solve the cube in the optimal number of rotations (["God's Number"](https://ruwix.com/the-rubiks-cube/gods-number/)).

Therefore, we decided to take on this problem and figure out a way to not only represent the cube, but also to be able to interact with a virtual cube while also developing a machine learning solver for the cube. We finally came down to using a convolutional neural network (CNN) to solve the cube, and while our results are not optimal, we were able to solve the cube over 50% of the time for up to 7 rotations for a shuffle. We all learned a lot through this process, picking up new skills such as Python and learning the Keras library for deep learning. We worked quite hard on this project, and we are very happy with our results.  

## Running the code
Here are the major sections of this project that are of particular interest.

### UI
We have a text-based UI for our project which is implemented in the [Cube_text.py](https://github.com/owencqueen/final_project_302/blob/master/Cube_text.py) file.
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
  
A more detailed guide to this interface is described in the documentation.

### CNN
This was one of the major parts of the project where we attempted to solve the Rubik's Cube using a convolutional neural network (CNN). There are many parts to this part of the project, and these are described in detail in the documentation. 

#### Models
We have included two models in this repo. The first is obonew1.model, and the second is oboorg1.model. The difference between these is described in the documentation, but the accuracy results of these two are practically the same (see Results section in documentation).

#### Testing the Model
To run the testers for the CNN, run either one of the following programs:

1. [model_tester.py](https://github.com/owencqueen/final_project_302/blob/master/model_test.py)
  - This tester simply calls on the model to predict the next move, and then it outputs the predictions, stopping when the model has solved the cube.
  - It can be run as follows:
```
Model to test:
Number of rotations for shuffle:
```
  - See the "Models" header above for the names of both of the models.
  - Then specify the number of rotations that you will perform in your initial shuffling of the cube.
  
2. [model_tester_random.py](https://github.com/owencqueen/final_project_302/blob/master/model_test_random.py)
  - This model runs the exact same as the one above, but it implements a random move element when it detects that the model is in a repetitive state.
  - As one can see in the Results section in the documentation, this model has a similar success rate to model_tester.py

## Libraries/ software required:
All of our was writen in [Python 3.8](https://www.python.org/downloads/), so you must have this downloaded before running the code.
Before running our code, you'll also want to install the following libraries:

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

