rsync -uvaz acone3:myapps-acone3/convbot/ ./ --exclude=.venv --exclude=.pytest_cache --exclude=convbot/__pycache__/ 
