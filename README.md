# CV-Settlers
This is a computer vision settlers of catan application that will be able to read gamestate and, in the future hopefully supply potential move options to each user.
# Environment Setup
To get everything you need for this project you will need to install some python libraries.

Here are the pip install commands necessary to get everything working:

```
pip install numpy
```

```
pip install matplotlib
```

```
pip install opencv-python
```

If you are unsure if you installed these libraries correctly just run python in your terminal/command window and type out the import statements.

It should look something like this:

```
$ python3
Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import matplotlib
>>> import cv2
>>>
```

**NOTE:** importing opencv-python is done by using the ```import cv2```

As long as there were no errors displayed when typing those import statement congrats, you have your environment setup correctly and can move forward with this project with ease.

# MatPlotLib Errors

There is a chance that even if you did everything correctly you will end up getting an error when trying to run the code in the repository. If not an error then your program might just sit there forever and never actually do anything. This is something inside of **MatPlotLib** and can be fixed.

You might get an error similar to this: 

```
/usr/local/lib/python2.7/dist-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
```

If your error is similar to this, and the one that I got was exactly the same except for my python version, here is how to fix it.

You need to find ```~/.matplotlib``` and ```~/.cache``` to do that you can type

```
import matplotlib as mpl
print mpl.get_cachedir()
```

in any python environment you want and it will give you the location of the ```~/.cache``` directory. Once you make it in there you want to delete the **fontconfig** directory. After that back out of the ```~/.cache``` and move into the ```~/.matplotlib``` and delete any contents that have **font** or **cache** anywhere in their names.

This should fix the problem and you should be able to continue with the project. If my instructions were unclear I used these two stackoverflow pages to solve this problem on my end: https://stackoverflow.com/questions/34771191/matplotlib-taking-time-when-being-imported, https://stackoverflow.com/questions/35734074/problems-with-matplotlib-is-building-the-font-cache-using-fc-list-this-may-tak

# Online Sources

Sentdex openCV for python tutorials: https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

Catan-omous Dealer: https://www.ece.cmu.edu/~ece549/spring16/team08/website/index.html

Markerless Tracking: https://docs.opencv.org/2.4/doc/tutorials/features2d/feature_homography/feature_homography.html#feature-homography

Watershed Algorithm: https://www.pyimagesearch.com/2015/11/02/watershed-opencv/

Card Game CV: http://arnab.org/blog/so-i-suck-24-automating-card-games-using-opencv-and-python

Chess Board Recognition: https://github.com/SukritGupta17/Chess-Board-Recognition

OpenCV Shape Recognition: https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
