# quick_image_labeling

This is a small python program to interactively label images. It shows all the images in a folder consecutively and moves them into folders corresponding to the label class. The number of classes and the folder containing the images have to be supplied as input arguments:

python quick_labeling "Path/To/Images" n_classes

The images are moved by pressing the key corresponding to the class (1,2,3,...,9). Pressing backspace, +, or delete undos the last move and the entire moving history is saved in history.txt in the image folder. Pressing escape ends the program.
