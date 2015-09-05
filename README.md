#PyDFGlue

This script glues multiple PDF to one PDF.


##Usage

    $ python PyDFGlue <outputfilename> [<inputfilename> ...]
    

###Addition

**PyDFRotate** let's your PDF rotate clockwise with the given angle.
**Warning:** Development pending.

###Usage PyDFRotate

	$ python PyDFRotate <outputfilename> <angle> [<inputfilename> ...]

Requirements
------------

* Python 2
* pyPdf


##Build (only PyDFGlue)

    $ python setup.py py2exe

Requires

* py2exe

##(Optional)

After that move the PyDFGlue folder anywhere you want to (e.g. Program Files).
Then add the PyDFGlue folder to your PATH variable.