import os
from datetime import datetime

from fabric.api import task, run, env, local, put
from fabric.contrib.project import upload_project

env.hosts = ['lawton.clayg.info']
env.use_ssh_agent = True

@task
def hostname():
    run('hostname')

def create_release():
    env.release = 'release-%s' % datetime.now().strftime('%Y%m%d-%H%M%S')
    local('tar czvf %s.tar.gz www' % env.release)

def ship_release(release):
    files = os.listdir('.')
    for filename in files:
        if release in filename:
            break
    put(filename, filename)

def install_release(release):
    pass

def clean_release():
    local('rm 2013*.tar.gz')

def push_static():
    pass

@task
def upload():
    upload_project(os.path.abspath('www'), '/var', use_sudo=True)
