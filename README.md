# End to End Machine Learning Project

Setup project with GitHub
1. Data Ingestion
2. Data Transformation
3. Model Trainer
4. Model Evaluation
5. Model Deployment

CI/CD Pipelines - GitHub Actions
Deployment - AWS

---------------------------------------------------------------------------------
 
1. Setup the Github {Repository}
 a) new environment
    Navigate vs code -> Open Anaconda terminal and navigate to the folder then type
   ```
   code .
   ```
    In vs code terminal->
   ```
   conda create -p venv python==3.8 -y
   ```
    environment created.
    ###### Clear terminal -> ```cls```
    Activated environment ->
   ```
   conda activate venv/
   ```

Clone GitHub repository and sync with vs code:
##### in vs code terminal -> ```git init```
		      create README.md file manually
##### add readme file to git repo -> ```git add README.md```
commit readme file -> ```git commit -m "First Commit"```
See the status of committed ->  ```git status```
push our file to git -> ```git branch -M main```
		   	```git remote add origin https://github.com/{}/{}.git```
check whether sync with right repo -> git remote -v
eneble git global -> git config --global user.name "your_name" (if first time)
		     git config --global user.email your@email.com
push data -> git push -u origin main

create .gitignore file in git repo manually. Select python template.

all the changes are done then pull code to the vs code -> git pull

 b) setup.py
    Create "setup.py" file manually. -> this will be responsible in creating ML application as a package. You can also install this package in your projects and you can also use it. With the help of setup.py will be able to build entire ML application as a package.

setup.py->
from setuptools import find_packages,setup -> automatically find out all the packages that are available in the entire ML application.

setup()-> include metadata information of the project
setup(
name = "",
version = "",
author="",
author_email="",
packages=find_package(),
install_requires=['pandas','numpy']
)

Create new folder as 'src' (source). If want to the src to be found as a package, inside the 'src' create a file '__init__.py'. In 'setup.py', 'find_packages' running, it go and see in how many folders you have this '_init_.py'. It will directory consider this 'src' as a package itself and it will try to build this. Once it builds you can probably import this anywhere you want. 

In setup(), install_requires=['pandas','numpy'] typing is not practical. So to do that we can right a function.
install_requires = get_requirements('requirement.txt')

from typing import List

def get_requirements(file_path:str)->List[str]: # this will return a list
	'''
	this function will returns the list of reuirements
	'''
	requirements = []
	with open(file_path) as file_obj: # let create this as a tempory object file object
		requirements=file_obj.readlines() # read line by line in requirements.txt file
		'''		
		one specipic problem over here.
		Inside this requirements.txt when we go to the next line, there will be '\n' that will get added.
		Once we get this requirements we will try to replace \n with the blank.
		''' 
		requirements=[req.replace("\n","")for req in requirements]

 c) requirements.txt
    Create "requirements.txt" Manually. -> this will have all the packages that needs to install while implementing the project.

within requirements.txt -> add your all libraries.

in requirements.txt -> '-e .' {automatically tigger 'setup.py' file and build package when we are installing requirements.txt}

execite this -> pip install -r requirements.txt


------------------------------------------------------------------------------------

Project Structure

src
 |--__init__.py
 |--exception.py
 |--logger.py
 |--utils.py
 |--components
 |       |-----__init__.py
 |       |-----data_ingestion.py
 |       |-----data_transformation.py
 |       |-----model_trainer.py
 |--pipeline
         |-----train_pipeline.py
         |-----predict_pipeline.py
         |-----__init__.py


In the src create folder 'components' -> this folder will be created as a package. so in this folder we need to create '__init__.py' file. 
It can be exported or it can be imported to some other file location. 

Data Ingestion is a one component of this project. So withing the components folder we need to create 'data_ingestion.py' file.

other components are data_transformation,model_trainer. we need to create data_transformation.py ,model_trainer.py files also.

within the src folder we need to create another folder call 'pipeline'. Basically we are going to create two pipelines. 
one for training and other one for predictions.

we need to create script files for them -> train_pipeline.py 
{this will basically have all the code for training pipeline itself. 
From this training pipeline will try to tigger or call data_ingestion.py, data_transformation.py, model_trainer.py files.}

Then we need to create three importnt files with in the src folder. They are
logger.py -> for logging purpose
exception.py -> for exception handling
utils.py -> for any functionalities probably writing in a common way.

1. exception.py
(search google 'exception python')

import sys -> any exception basically getting control sys library will automatically have that information.

------------------------------------------------------------------
You can see this through : http://127.0.0.1:5000/predictdata
