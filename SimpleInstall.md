# Installing Python and mechanize on windows #

1. Get Python

    1. Download the windows binary of Python 2.7.2.  

        "Python 2.7.2 Windows Installer (Windows Binary -- does not include source)"

    2. Install the windows binary of Python. 

    3. **Important**: Note where Python is (probably `C:\Python27`)


2. Get mechanize

    1. Download mechanize and unzip it in your home directory
    
    2. **Important**: Note where mechanize is (probably) C:\Documents and Settings\*USERNAME*\My Documents\Downloads\mechanize-0.2.5)
    
    3. Open Accessories/Command Prompt and move to where mechanize is:

		Replace USERNAME with your username
    
        Type `cd "C:\Documents and Settings\USERNAME\My Documents\Downloads\mechanize-0.25"`
        
        You can also use tab completion, i.e. `Docu<tab>`. 
    
    4. Check which folder you are in:
    
        Type `dir`, which will list the files in the current directory. 
        
        If you see `setup.py`, you are in business. 
        
        If you see another mechanize folder, type `cd mechanize-0.25` (or the version of mechanize you have)


3. Install mechanize

    1. Assuming you see `setup.py` when you type `dir`, type:

		`C:\Python27\python setup.py install`
		
		If python is not located in `C:\Python27`, change as necessary
    
    2. Magic should occur. Hopefully there are no errors. 


4. Use mechanize

    1. Open Start/Programs/Python 2.7/Python (command line)
    
        Remember that the python prompt is `>>>`
    
    2. Type `import mechanize` at the python prompt
    
        Confusingly, success is nothing happening (a new blank line with `>>>`)
        
        A name error means mechanize has not been installed properly. 
