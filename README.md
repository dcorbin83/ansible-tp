* ssh-server
``` bash
cd ssh-server
docker-compose up 
``` 
* ansible
``` bash
cd ansible
./sshSetup.sh
ansible-playbook -i host.ini files-creation/playbook.yml
```
