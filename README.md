# Installing Python and mechanize on windows #

1. Get Python
a. Download the windows binary of Python 2.7.2. 
b. Install the windows binary of Python. 
c. Note where Python is (probably C:\Python27)

2. Tell your computer where Python is
a. Right click on My Computer and go to Properties or whatever
b. Click the Advanced tab, click the Environment Variables button
c. Below the System variables box, click "New"
Variable name: PYTHON_HOME
Variable value: C:\Python27 (or whatever from step 1c)
Click OK
d. Find the system variable called Path, click it, click Edit
This should be a bunch of random shit with a semicolon between each thing
Arrow to the end, add a semicolon if there isn't one, then type
%PYTHON_HOME%
Click OK
Click OK until the window goes away

3. Make sure your computer knows where Python is
Go to Start/Run and type python and hit enter (or type python into Command Prompt)
If you get a python prompt (triple right brackets... >>>) success
If you get "python is not recognized as a command" and a c prompt (single right bracket >) FAILURE

4. Get mechanize
a. Download mechanize and unzip it somewhere in your home directory
(Let's say this is somewhere like C:\Documents and Settings\MFE\Downloads\mechanize)
b. Open Accessories/Command Prompt and type dir
This should list the files in the path the Command Prompt is currently in
c. You probably see Downloads, so go there:
d. Type cd Downloads (you can usually use tab completion, i.e. Dow<tab>)
e. Repeat alternating dir and cd commands until you are in the mechanize folder and
***you see setup.py when you type dir***
This is what I meant by "being in the path where mechanize is"
This is the most critical part to getting mechanize working

5. Install mechanize
a. Assuming you see setup.py from dir, type python setup.py install
b. Magic should occur

6. Use mechanize
a. Open python.exe
b. Type import mechanize
c. If nothing appears to happen (new blank line), success
d. If Name Error, FAILURE