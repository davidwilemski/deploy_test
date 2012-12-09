
from fabric.api import *
from fabtools import require
import fabtools

@task
def start():
    with fabtools.python.virtualenv('deploy_test_env'):
        with cd('deploy_test'):
            fabtools.supervisor.start_process('app')

@task
def stop():
    with fabtools.python.virtualenv('deploy_test_env'):
        with cd('deploy_test'):
            fabtools.supervisor.stop_process('app')

@task
def setup():
    require.python.pip()

    # Create venv
    require.python.virtualenv('deploy_test_env')

    # activate venv
    with fabtools.python.virtualenv('deploy_test_env'):
        # clone repo
        run('git clone git@github.com:davidwilemski/deploy_test.git')
        
        # install requirements
        require.python.requirements('deploy_test/requirements.txt')

    start()
