#!/bin/bash

var=$(docker container inspect $(docker container ps -aq) | egrep "IPAddress" | grep [0-9] | awk '{ print $2 }')
source ../ssh-server/docker/.env

for i in $var
do
tmp=${i::-1}
address="${tmp//\"}"
ssh-keygen -R $address
ssh-copy-id $SSH_MASTER_USER@$address
done

