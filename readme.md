# Homework4 Project Setup
##  Faker, Generating test data, and adding package to command line app.

1. Add the "faker" libary with the command "pip install faker" and then do a  pip install -r requirements.txt then do pip freeze > requirements.txt.  
2. Add a new command to pytest to generate N number of records, so that we can run the following command: pytest --num_records=100 to generate 100 records. The code to do this is in the tests/conftest.py file.
3. Add a main.py file to serve as an entry point to my program and add the code from my main.py, so that we can have some exception handling to program.

## Instructions:
1. create clone the repo.
2. First Deactivate the virtual environment with the command "deactivate" and then activate it again command.
  i. source venv/bin/activate
3. Add the "faker" libary with the command :
   i.   pip install faker
   ii.  pip install -r requirements.txt
   iii. pip freeze > requirements.txt

Note When someone copies / clones your repository they will install the specfic library / dependency requirements for your project using the command:

-> pip install -r requirments.txt
-> Finally, Open VScode and test code.
   i. code .

## Testing

1. pytest
2. pytest --pylint
3. pytest --num_records=10
4. pytest --pylint --cov

## Other commands used during project
 1. mv oldfile newfilename
 2. git remote remove origin
 3. rm -rf .pytest_cache
 4. To add multiple specific files: git add path/to/file1.py path/to/file2.py path/to/file3.py
