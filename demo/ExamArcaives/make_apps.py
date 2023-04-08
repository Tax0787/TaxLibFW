from os import system as s

s('python -m compileall .')
s('python -m zipapp introduction -c -o "introduction_app.pyz"')
