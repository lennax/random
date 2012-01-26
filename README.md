# Installing Python and mechanize on windows #

1. Get Python

    1. Download the windows binary of Python 2.7.2. 

    2. Install the windows binary of Python. 

    3. Note where Python is (probably C:\Python27)


2. Tell your computer where Python is

    1. Right click on My Computer and go to Properties or whatever

    2. Click the Advanced tab, click the Environment Variables button

    3. Below the System variables box, click "New"

        Variable name: `PYTHON_HOME`
    
        Variable value: `C:\Python27` (or whatever from step 1.3)
    
        Make sure there are no spaces in either field. Click OK.
        
    4. Find the system variable called Path, click it, click Edit

        This should be a bunch of folders and variables with a semicolon between each thing
Arrow to the end, add a semicolon if there isn't one, then type
`%PYTHON_HOME%`

        Again, make sure there are no spaces. Click OK
        
        Click OK until the window goes away


3. Make sure your computer knows where Python is

    Go to Start/Run and type python and hit enter (or type python into Command Prompt)
    
    If you get a python prompt (triple right brackets... `>>>`) success
    
    If you get "python is not recognized as a command" and a c prompt (single right bracket `>`) FAILURE


4. Get mechanize

    1. Download mechanize and unzip it somewhere in your home directory
    
        (Let's say this is somewhere like C:\Documents and Settings\USERNAME\Downloads\mechanize)
    
    2. Open Accessories/Command Prompt and move to where mechanize is:
    
        Type `cd C:\"Documents and Settings"\USERNAME\Downloads\mechanize`
        
        You can also use tab completion, i.e. `Docu<tab>`. 
    
    3. Check which folder you are in:
    
        Type `dir`, which will list the files in the current directory. 
        
        If you see **setup.py**, you are in business. 
        
        If you see another mechanize folder, type `cd mechanize<tab>` (or whichever version of mechanize shows up)


5. Install mechanize

    1. Assuming you see **setup.py** when you type `dir`, type `python setup.py install`
    
    2. Magic should occur. Hopefully there are no errors. 


6. Use mechanize

    1. Open python.exe (or Command Prompt, `python`, or Start/Run/python)
    
        Remember that the python prompt is `>>>`
    
    2. Type import mechanize
    
        Confusingly, success is nothing happening (a new blank line with `>>>`)
        
        A name error means mechanize has not been installed properly. 
