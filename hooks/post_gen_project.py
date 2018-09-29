from pathlib import Path
import os
import subprocess


PROJECT_NAME = '{{ cookiecutter.project_repo_name }}'
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if __name__ == '__main__':
    PROJECT_SRC_DIRECTORY = Path(PROJECT_DIRECTORY, PROJECT_NAME)
    p = Path(PROJECT_SRC_DIRECTORY, f'{PROJECT_NAME}.py')

    with open(str(p), 'w') as f:
        f.write('print(\'Hello, world!\')')

    subprocess.run(['git', 'init'])
