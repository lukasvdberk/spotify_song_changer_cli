
### About
An terminal based application for switching songs on spotify (really nice for i3wm)

### Installation
requirements
1. pipenv (with python3)

To install all the requirements for this project
```bash
pipenv install
```


#### Run
First activate the shell
```bash
pipenv shell
```

**Note**

Fill in the variables in the .example-env file.
Client id and secret come from the spotify api. 
Make sure when creating an application on the spotify developer platform that redirect url is http://locahost:8080.
When you filed in the information in the .example-env file rename it to .env

Then run with 
```bash
python app.py
```
