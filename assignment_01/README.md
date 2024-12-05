# 1) Introduction

Goal of the assignment is to create script for processing data stored in JSON 
got from specific URL addresses. It saves them into one file under module's name. 
Secondly it searches for duplicated keys in all modules and stores them with their values 
in second file. 

# 2) Requirements

Requirements for this project are located in master README.md in root folder of this repository.

# 3) Running project

After environment set up you can run this project with command:

```sh
python {workplace_folder}/assignment_01/src/localizationProcessing.py
```

where `{workplace_folder}` is root folder of repository.

# 5) Project details

Both files can be found on `JSON_MERGED_PATH` and `JSON_DUPLICIT_PATH`. 
It can be configured in `assignment_01/src/config.py`.

Script also has log feature. It prints messages in console and into `LOG_PATH` 
(found in `config.py`).