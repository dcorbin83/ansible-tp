#!/bin/bash

ssh-keygen -R $1
ssh-copy-id kubecorn@$1


