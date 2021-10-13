* ssh-server
``` bash
cd ssh-server
docker-compose rm
docker-compose up --build
``` 
* ansible 
``` bash
cd ansible
./sshSetup.sh
ansible-playbook -i host.ini files-creation/playbook.yml -u {SSH_MASTER_USER}
```
