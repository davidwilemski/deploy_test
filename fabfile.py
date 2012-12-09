
from fabric.api import *
from fabtools import require
import fabtools

@task
def deploy():
    with prefix('source ~/deploy_test_env/bin/activate'):
        with cd('~/deploy_test'):
            run('git pull')

@task
def start():
    with prefix('source ~/deploy_test_env/bin/activate'):
        with cd('~/deploy_test'):
            run('supervisord')

@task
def stop():
    with prefix('source ~/deploy_test_env/bin/activate'):
        with cd('deploy_test'):
            run('kill `cat supervisord.pid`')

@task
def setup():
    require.python.pip()

    # Create venv
    run('virtualenv deploy_test_env')

    # activate venv
    with fabtools.python.virtualenv('deploy_test_env'):
        # clone repo
        run('git clone https://github.com/davidwilemski/deploy_test.git')
        
        # install requirements
        fabtools.python.install_requirements('deploy_test/requirements.txt')

    start()
