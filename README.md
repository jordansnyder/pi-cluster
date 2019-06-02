# pi-cluster

**NOTE: Change your Pi hostnames! If they're all the default raspberrypi, k3s won't work correctly. 

# Prerequisites
1. Set up as many Raspbian SD cards as you need, with Raspbian Lite. Touch the /boot/ssh file so that SSH is enabled on first boot. (Possibly add SSH key to authorized_keys during this step?)
2. Add your ssh public key to every one of the hosts' authorized_keys file (not covered here) - you need to SSH into the Pi's individually and create this file.

# On your machine (not the Raspberry Pis)

1. Install Ansible (not covered here)
2. `sudo mkdir /etc/ansible && sudo pico /etc/ansible/hosts` (add hosts in either yaml or INI style). For example, if you have 4 Pi's in the cluster: 
```
[master]
k3s-master ansible_host=192.168.1.6
[workers]
k3s-worker-01 ansible_host=192.168.1.7
k3s-worker-02 ansible_host=192.168.1.8
k3s-worker-03 ansible_host=192.168.1.9
```
4. Assuming that you put your public SSH key in the `pi` user's .ssh/authorized_keys file, you'll want to run ansible as the `pi` user so it can login properly with the SSH key. Using `--become` tells Ansible to upgrade to sudo when necessary.

```ansible-playbook ./playbooks/setup_cgroups.yml --user pi --become```

The playbook will seem to fail because the Pi's should reboot at this point. Wait for them to come back, and run the next playbook...

5. 
```ansible-playbook ./playbooks/setup_k3s.yml --user pi --become```

6. If everything was set up correctly and this works, you can SSH into the master host and run `kubectl get node -o wide` to see all the nodes connected.