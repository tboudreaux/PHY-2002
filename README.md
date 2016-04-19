A repository for PHY-2002 code (SAUL)
Authors: Thomas M. Boudreaux, Padraig N. Clancy
SAUL is liscensed under the LGPL licsense

<b>Install Prossess:</b>

1) Download the SAUL master branch, either threw a pull or a zip archive

2) Run BPlot.py with anaconda, while SAUL technically works with standard python and will try to install its own dependencies it is much better to use with anconda and have SAUL install only the 3-4 dependanciy's it has not in anaconda.

    a) this prosses can take some time, and will likely involve multiple restarts of saul and clever use of the super user permissions
  
    b) if saul failes in installing dependencies pip may be set up differently on your computer and you will have to install dependenceied manually, SAUL lets you know what dependencies it failes on as well it entire prerun log in the prerun.log file
  
    c) dependencies list
  
      i) de423
      ii) jplephem
      iii) ephemris
      iv) all other dependencies are part of anaconda
    
3) Once SAUL launches you are presented with the perfect in all ways interface (Pleasebe aware the interface is not perfect in all ways despirte what the nice man on git hub tells you...I was working there, stop messing with my mojo John!)

4) From the perfect in...most ways interface (There are you happy now, no?!, wow no respect around here) one can access Spectral plotting, Cross corelation, Orbital Fitting, and Gaussian fitting through the labels buttons, the labels should make sense. [Gfit = guassian fitting] [X-Cor = Cross Correlation] [Orb Fit = Orbital Fitting]

<b> Use of SAUL, other wise known as, very slightly more use freinedly than IRAF</b>

1) Generating Path Files

    a) make sure the data files are in the directory you are in or lower (subdirectories)
    b) click generate path files
    c) click reload to reload SAUL so the path files propegrate threwout the computereized matrix system (that's utter nonsesnse but it sounds fancy, do reload SAUL at this point it helps to keep down bugs)

2) Cross Correlation

    a) click the X-Cor Button
    b) copy a target to the target box 
    c) copy a template to the tamplate box
    d) set polynominal normilization order and crop window size
    e) if you sish to see all plots click Show all plots (crazy right?)
      i) in all plots scan threw orders, thats easty enoguh
      ii) use check boxes to tell X-Cor to ignore orders when duing math, only checkd orders will be used
      iii) click advance to begin forming the text file
      iv) dont forget to click save in the ASCII editor!
    f) if one plot at a time don't click show all plots, that should make sense, because...logic?
      i) use 'a' to advance orders and use 'b' to go back orders
      ii) use 'r' to force a refit of the gauusian to the location of your mouse cursor
        I) if the fit failes it will revert to the origional guess so dont freak out try another location a pixel off or something, the whimes of computers are known only to magicians...and me, HAHAHHAHAHAHAHAHAHAHA, no thats a lie
      iii) once you finish all orders a plot of all orders at once will show up (SO sucks to be you, you only wanted to see one order at a time, either way your seeing all of them) but with any adjustments you made applied to it
      iv) Same thing, advance to form a text file, save, whatnot, you know the deal
      
3) Guassian Fitting

    a) click G-fit from main SAUL amazing window of amazingness
    b) pasete an observation in from the list
    c) select an absorbtion feature (in reality it works best with only one right now)
    d) click fit and plot
      i) this has generated, or appened an ascii file with the velocities, they are fully good now, all the new lines and what not so ready to plug into orbital fit routinen
    e) repete for all observations

4) Spectral Plotting:

    a) Non Stacked:
      i) paste in a file path to a single file in the SINGLE FILE PATH box
      ii) if you want to fit a function select fit, set the degree
        I) to show the normalized spectra as well as the non normalized spectre select the big button -- show fit (its a boolean that doesent induce action)
      iii) click plot (the small boring sad button) and thats the rub
        I) 'd' to advance an order
        II) 'a' to go back an order
        III) 'j' to bring up jump to order
    b) stacked:
      i) enter 'PathTo[STARNAME]' in the Stacked box
      ii) check stack
      iii) enter the inital number of targets you would like to stack or check all (dont check all it is bad as you cant modigy with all, I'll change that when I get to it)
      iv) same function stuff as before
      v) same kestrokes with the added ones:
        I) 'e' to add spectra
        II) 'q' to remove spectra
5) Orbital Fitting

    a) click orb fit
    b) enter the period, keep period is know checked
    c) enter the path to the RV file
      i) X-Cor output files named like: 'CCorOutput[TARGETSTARNAME].csv'
      ii) Guas fit outputs files name like: 'GaussuianFitOutput[STARNAME].csv'
    e) decide whether you want to introduce a linear or sinusodual trend onto the sin fit
      i) if you click one and change your mind click the big obvious button
    d) click attempt fit, to you know...bake dinner, no that was lie, im just hungry, to attempt an orbital fit solution
6) terminal Commands

SAUL has a serise of terminal commands (that work now), they are similar to UNIX commands, but different because I want to make everyones lives harder. 'cd' and 'ls' work the same, however they do not have any assosicate options as UNIX does. 'view' is analogous to 'cat', the edit program is a very simple ascii editor, use like 'nano' or 'vim' (in exceution not function). 'lcom' will provide a nearly complete list of commands. 'stanPlot' plots a data file of either 2 or three colums with the first colum beign the x data the second being y and if there is a third it becomes the y error. the sytax there is stanPlot [filename] [xlabel (no spaces)] [ylabel (no spaces)]. secrets are fun. 'comp' creates a comparision based on cross correlation, thats a pretty usless commands really that should be generalized more. 'clear' clears the terminal. there are a bunch of functions related to user definable buttons, see 'lcom' for those. 'mkdir' works, 'rm' does not. 'reload' will reload SAUL. 'pyrun' will run a python file, standard output will go to the terminal, any standard input will BREAK EVERYTHING. 'pwd' does what you would expect. Tab completion does nothing and is not in, previous commands were in then brokw and currently work like 3% of the time. Yea thats the consol.

If you have any issues please contact Thomas Boudreaux, he has really nothing to do so would enjoy fixing issues. Thanks so much for looking out out humble (amazing, shut up, humble, shhhhhh, amazing, I SAID BE QUITE) software.
    
