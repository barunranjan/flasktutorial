# flasktutorial
First Create the virtual enviorment.

You can make sure that pip is up-to-date by running:
py -m pip install --upgrade pip

for Linux
python3 -m pip install --user --upgrade pippython3 -m pip install --user --upgrade pip

Afterwards, you should have the newest pip installed in your user site:
python3 -m pip --version
pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)

Installing virtualenv:
python3 -m pip install --user virtualenv

Creating a virtual environment:
python3 -m venv env

Activating a virtual environment:
source env/bin/activate

Leaving the virtual environment:
deactivate


