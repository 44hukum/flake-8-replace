# flake-8-replace

This script remove double quote from the code.

## Before using this make sure
* `flake8` `flake8-quotes`, `flake8-use-fstring` are installed

# Working Mechanism

This script walkdown the project root directory and travel down to all the files that doesnot ends with pyc and use flake8 on each file and then catches the error file and location, fetch data and replaces the single quote with double quote

# How to run ?
Just talke it and run 