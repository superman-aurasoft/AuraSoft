from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['cha@49.247.226.10']

def push():
    local("git push")

def prepare_deploy():
    # local("./manage.py test something")
    push()

def deploy():
    run("cd /var/git/AuraSoft/; git pull");
    sudo("rm -rf /home/aurasoft/www/AuraSoft");
    sudo("cp -R /var/git/AuraSoft/ /home/aurasoft/www/");
    sudo("mv /home/aurasoft/www/AuraSoft/Aurasoft/settings.deploy.py /home/aurasoft/www/Aurasoft/settings.py");
    sudo("chown -R apache.apache /home/aurasoft/www/");
