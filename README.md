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

Install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install), then install [Ubuntu for Windows](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6?hl=en-us&gl=US).

Once you have that, install pip:
```
sudo easy_install pip
```

Follow the Mac/Unix steps for creating a virtual environment.

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

For Windows (w/o Windows Subsystem for Linux):

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

### Dashboard Setup
Run
```
py serve_dashboard.py
```
or
```
python serve_dashboard.py
```
depending on your OS.

