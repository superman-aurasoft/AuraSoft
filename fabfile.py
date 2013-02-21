from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['cha@49.247.226.10']
env.warn_only = True

def push():
    local("git push")

def prepare_deploy():
    # local("./manage.py test something")
    push()

def deploy():

    prepare_deploy()

    with cd('/var/git/AuraSoft'):
        run("git pull");
        
    sudo("apachectl stop")
    sudo("rm -rf /home/aurasoft/www/AuraSoft");
    sudo("cp -R /var/git/AuraSoft/ /home/aurasoft/www/");
    sudo("mv /home/aurasoft/www/AuraSoft/AuraSoft/settings.deploy.py /home/aurasoft/www/AuraSoft/AuraSoft/settings.py");
    sudo("echo \"yes\" | /home/aurasoft/www/AuraSoft/manage.py collectstatic")
    sudo("chown -R apache.apache /home/aurasoft/www/");
    sudo("apachectl start")
