# pi-cluster

**NOTE: The fabfile.py is for an older version of Fabric and doesn't work with fabric 2

**NOTE: Change your Pi hostnames! If they're all the default raspberrypi, k3s won't work correctly. 

1. Install Ansible
2. sudo mkdir /etc/ansible
3. sudo pico /etc/ansible/hosts (add hosts in either yaml or INI style). For example: 
```
[master]
k3s-master ansible_host=192.168.1.6
[workers]
k3s-worker-01 ansible_host=192.168.1.7
k3s-worker-02 ansible_host=192.168.1.8
k3s-worker-03 ansible_host=192.168.1.9
```