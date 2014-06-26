# ########################################################################### #

For our purposes you'll need the following

python == 2.7.6 (and standard libraries)
pip >= 1.5.6
iPython >= 2.1.0
numpy >= 1.8
scipy >= 0.14.0
matplotlib >= 1.3.1
spyder >= 2.2.5

# ########################################################################### #
Installation

# ======================= Method 1:
Install using a distribution.

__Anaconda__
If you have an academic email (e.g. u??????@utah.edu) then download the full distribution at
https://store.continuum.io/cshop/academicanaconda

Else if you don't have an academic email you can install their free version which will work for our purposes.

Alternatives to Anaconda are:
  * Enthought Canopy : https://www.enthought.com/products/canopy/academic/
  * XYPython : (Windows Only) https://code.google.com/p/pythonxy/wiki/Downloads


# ======================= Method 2:
Mac OSX comes pre-installed with python. Though most recommendations say to install a different version, this one will work for our purposes. These instructions work if you already have a python version installed

1) use easy_install to get pip (both easy_install and pip are package installers)
`easy_install pip`

2) use pip to install 
`pip install iPython`
`pip install numpy`
`pip install scipy`
`pip install matplotlib`

3) Install spyder install from the following URL
https://bitbucket.org/spyder-ide/spyderlib/downloads
or 
use easy_install to install spyder 
`easy_install spyder`


# ======================= Method 3: 
The physics computers have most of what you need. To have a full distribution add to your tcshrc/bashrc/cshrc startup script:

source /home/grad/dsg/applications/anaconda/source_python_tcsh

Then open a new terminal to have the effects take place





