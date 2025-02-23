# DevSecOps and IAC Process Automation

ContainerLab/Docker -> only on a local computer

Docker Swarm -> using multiple virtual machines to stimulate multiple devices

Solution:
1. Deploy network infrastructure over the cloud
2. Automated configuration and deployment
3. DevSecOps (added security measures)

Tools used -> Docker, Docker Swarm, ContainerLab, Ansible, Jenkins, GitHub, Docker Hub

Simple network topology this stimulates: CSR 1000V Router, Apache Server, Ubuntu Client


ContainerLab/Docker Files and its purpose:

clab.yml -> ContainerLab topology file ( defines the network topology)
plb.yml -> Ansible script for deploying topology file 
configuring_apache.yml -> Ansible script for installation of ip route, ping, net tools and start the ssh service for Ansible to go into the server to make changes
configuring_ubuntu.yml -> Ansible script for installation of ip route, ping and net tools
configuring_router_interfaces.py -> Configuring router interfaces G2 and G3 with specific ip addresses
configuring_router_interfaces.yml -> Ansible script to run the Telnet python script to assign router interfaces with ip addresses
apache_ip_route2.yml -> Ansible script to set IP routes in the Apache container to connect to the router and client
ubuntu_ip_route2.yml -> Ansible script to set IP routes in the Ubuntu container to connect to the router and server
update_telnet_configuration.py -> Python script to update hostname of router
update_1.yml -> Ansible script to trigger the telnet configuration script to update the hostname of the router
ssh2.yml -> Ansible script to change contents of the default Apache Server
router_hardening.py -> Python script to harden the router, part of the DevSecOps process eg secured privileged exec mode with username and password
update_router.yml -> Ansible script to run the Python script to harden the router


Docker Swaarm Files and its purpose:

ansible.cfg
docker-compose.yml
swarm-deploy.yml
swarm-inventory.yml
swarm-leave.yml
