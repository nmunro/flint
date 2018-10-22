from pathlib import Path
from urllib import request
import os
import subprocess

pre_commit = Path('.git', 'hooks', 'pre-commit')

with open(os.devnull, 'w') as fp:
    subprocess.run(['git', 'init'], stdout=fp)

with open(pre_commit, 'w') as f:
    f.write('#!/usr/bin/env sh\n\n')
    f.write('make lint && make test')

with open(os.devnull, 'w') as fp:
    subprocess.run(['chmod', '+x', str(pre_commit)], stdout=fp)

request.urlretrieve(
    'https://www.gitignore.io/api/{{cookiecutter.project_gitignore_sets|replace(" ", ",")}}',
    '.gitignore',
)

