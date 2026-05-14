Radio Panik
===========

OSP has designed the 2012 program for Brussels based alternative radio station, Radio Panik.
The program (‘the grille’) is constructed through what is considered a type crime—
horizontally squashing the text to make it fit. We debuted our new typeface Reglo for this job.

Next to the design of the program, we constructed a web interface that provides a means
for the employees of Radio Panik to generate cd covers and posters in the same style.

The web interface allows one to browse and choose from the various image categories of Wikimedia Commons,
input a text and choose a paper size, after which it will generate a design in a vector file format.
The output is an SVG file which can be further edited in proprietary and libre image editors.


- - -

In this repository one finds the 2012 program for Radio Panik (the Grille),  
as designed by OSP Open Source Publishing.

In addition a web interface provides a means to generate posters  
and cd covers in the style of the Grille.

The design is licensed under the Free Art License  
http://artlibre.org/licence/lal/en  
The Python code is licensed under General Public License  
gpl-3.0.txt  
The text in the Grille remains property of Radio Panik.

## Web interface ##

These are instructions to run the web interface locally.
These instructions were tested on Ubuntu Linux and  
should be similar on Debian Linux.
 
First make sure you have installed the Reglo font (see below)

Run these commands in a terminal window:

    python -m venv panik-env
    source panik-env/bin/activate
    pip install Flask pillow pycairo svgwrite

To run the web interface, move into the folder where you downloaded the OSP files.
Then:

    cd PanikGenerator  
    python panik_app.py

In your terminal window you will see a message that you have now launched the webserver.  
This means the program is running locally.  
You can visit the address http://127.0.0.1:5000/ in your web browser.

PS:  
The application is a standard WSGI application: to install  
on your webserver you can follow the same steps as for  
installing other python applications on your server.


## The Reglo font ##

The identity makes use of the OSP typeface Reglo.  
To properly calculate the type stretching the python script needs  
Reglo installed. Also to subsequently view / edit the SVG’s  
one needs this font.

You can find it in the repository as Reglo.otf, or online at:  
http://ospublish.constantvzw.org/foundry/reglo/

-------
OSP Open Source Publishing  
http://ospublish.constantvzw.org/  
Radio Panik  
http://www.radiopanik.org/
