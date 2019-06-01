from fabric import *

env.hosts = [
    '192.168.1.6',
    '192.168.1.7',
    '192.168.1.8',
    '192.168.1.9'
]

env.password = 'raspberry'


@parallel
def cmd(command):
    sudo(command)
