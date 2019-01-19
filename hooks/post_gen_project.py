from pathlib import Path
from urllib import request
import os
import subprocess

pre_commit = Path('.git', 'hooks', 'pre-commit')
ignore = Path('.gitignore')
license = Path('LICENSE')

with open(os.devnull, 'w') as fp:
    subprocess.run(['git', 'init'], stdout=fp)

with open(pre_commit, 'w') as f:
    f.write(
        '#!/usr/bin/env sh\n\n'
        '# Check requirements.txt exists\n'
        'if [ ! -f requirements.txt ]; then\n'
        '    echo "No requirements.txt file found, please write one!"\n'
        '    exit 1\n'
        'fi\n'
        '\n'
        '# Check requirements.txt is up to date\n'
        'poetry show --no-dev | tr -s " " | sed \'s/ /==/\' | sed \'s/ .*//\' > .reqs.txt\n'
        'if cmp -s requirements.txt .reqs.txt; then\n'
        '    rm .reqs.txt\n'
        '    make lint && make test\n'
        'else\n'
        '    echo "Outdated requirements.txt file found, please update it!"\n'
        '    rm .reqs.txt\n'
        '    exit 1\n'
        'fi\n'
    )

with open(os.devnull, 'w') as fp:
    subprocess.run(['chmod', '+x', str(pre_commit)], stdout=fp)

gitignore_url = 'https://www.gitignore.io/api/{{cookiecutter.project_gitignore_sets|replace(" ", ",")}}'
license_url = ''.join([
    'http://li-gen.herokuapp.com/license?',
    'project_name={{cookiecutter.project_name|replace(" ", "%20")}}&',
    'author_name={{cookiecutter.author_name|replace(" ", "%20")}}&',
    'author_email={{cookiecutter.author_email|replace("@", "%40")}}&',
    'license={{cookiecutter.project_license|lower}}&',
    'raw=true'
])

request.urlretrieve(gitignore_url, ignore)
request.urlretrieve(license_url, license)

with open(ignore, 'a') as f:
    f.write('\n# Extra lines needed for Flint\n')
    f.write('coverage')
