start /b pipenv run pelican --debug --autoreload -r content -o output -s .\pelicanconf.py 


cd output 


start /b pipenv run python -m http.server 9000