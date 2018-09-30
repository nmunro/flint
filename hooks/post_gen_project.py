import os
import subprocess
from urllib import request


with open(os.devnull, 'w') as fp:
    subprocess.run(['git', 'init'], stdout=fp)

request.urlretrieve(
    'https://www.gitignore.io/api/{{cookiecutter.project_gitignore_sets|replace(" ", ",")}}',
    '.gitignore',
)

