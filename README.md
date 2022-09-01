# Virtual environment
## Install package
pip install pipenv

## Create virtual environment according to Pipfile and Pipfile.lock
pipenv install

## Activate environment
pipenv shell

# Execute
## cmd
python .\YoutubeDownloader.py
## package it to .exe
pyinstaller.exe -F -w .\YoutubeDownloader.py
