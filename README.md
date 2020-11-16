# ansible-tp

# ssh-server
``` bash
docker-compose up 
``` 
#ansible
``` bash
ssh-keygen -R <IP_container>
ssh-copy-id kubecorn@<IP_container>
ansible-playbook -i host.ini jobs.yml -u kubecorn
```
