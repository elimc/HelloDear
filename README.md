# HelloDear
ConversationalAI for romance scammers

### Requirements
We need to ensure python3 and pip are installed.
For Mac/Unix:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```

For Windows:
Please ensure that you have python3 on your computer. If you are unsure, you can download the most up-to-date version by following the steps at this link: https://docs.python.org/3/using/windows.html#windows-full
```sh
py -m pip install --upgrade pip
py -m pip --version
```

### Installation of project
1) Clone this project to a folder on your computer
2) Open a terminal or command prompt
3) Navigate to the folder with your requirements.txt
4) We will need to install venv.
For Mac/Unix:
```sh
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate
```

For Windows:
```sh
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
deactivate
```
5) You are done installing the project and it's dependencies. We can deactivate now:

### Working in your project
You will need to ensure you project is activated. This will allow python libraries to be run locally instead of globally.
For Mac/Unix:
```sh
source env/bin/activate
which python
```

For Windows:
```sh
.\env\Scripts\activate
where python
```

To deactivate your venv for both Mac/Unix and Windows:
```sh
deactivate
```