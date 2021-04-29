# Infinite Remixer
Infinite Remixer is a Python application that creates remixes, patching 
together multiple songs.


## Installation
To install the package, move to the root of the repo and type in the console:

`$ pip install .`

If you plan to develop the package further, install the package in editable 
mode also installing the packages necessary to run unittests: 

`$ pip install -e .[test]`


## Testing
To run unittests, issue the following command from the root of the repo:

`$ pytest`


## Package structure 
The package is divided into 4 sub-packages:
- segmentation
- data
- search
- remix

*segmentation* is responsible to segment groups of songs into beats and 
store the beats as separate wav files.

*data* can be used to batch extract audio features from a directory containing 
audio files, aggregate the features, and storing the data ready to be 
consumed by *search*.

*search* contains facilities to fit a scikit-learn NearestNeighbour object, 
and a wrapper class around this object to apply nearest neighbour search.

*remix* is responsible for generating new remixes.


## How to generate a remix
To generate a remix, there are two main high-level steps to carry out. 
First, preprocess a group of songs you want to remix. Second, 
generate a remix, which will leverage the preprocessed data.

### Preprocessing
To preprocess data follow these steps:

1- Segment a group of tracks into beats
2- Extract features and prepare data from the beats
3- Fit a Nearest Neighbour object

To run the steps above, use the entry points below. You can find more info 
on the entry points, in the respective modules.

`$ segment path/to/dir/with/files path/to/save/dir/for/beats`

`$ create_dataset path/to/dir/with/audio/files save/dir`

`$ fit_nearest_neighbours dataset/path save/path`


### Remixing
Once you have gone through the preprocessing steps, you're ready to create 
remixes with the command below:

`$ generate_remix 0.1 50 save/path/example.wav`

The first positional argument is the *jump rate*. It's a value between 0 
and 1, which indicates how frequently the system should jump from one song 
to another. The greater the value the higher the chance to jump to a new track.

The second positional argument indicates the number of beats in the remix.

In order to load the necessary artifacts for running the remix, you'll have 
to change the paths to your artifacts directly in the top part of the 
`remix/generateremix.py` script.

## Dependencies
Infinite Remixer uses the packages below to extract audio features and for 
nearest neighbour search:

- librosa
- scikit-learn

## YouTube video
Learn more about Infinite Remixer in this project presentation video on The 
Sound of AI YouTube channel.






