import yaml

d = [{'windows':{
        'hosts':{
                'lfrbuild': '',
                'lfrbuild2': '',
                'lfrbuild3': ''},
        'vars':{
                'ansible_password': '{{optispwd}}',
                'ansible_connection': 'ssh',
                'ansible_shell_type': 'cmd',
                'ansible_python_interpreter': r'C:\Users\dcorbin\AppData\Local\Programs\Python\Python37\python.exe'},
                }
     }]
with open('data.yml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False)
    
    
# - windows:
#     hosts:
#       lfrbuild: ''
#       lfrbuild2: ''
#       lfrbuild3: ''
#     vars:
#       ansible_connection: ssh
#       ansible_password: '{{optispwd}}'
#       ansible_python_interpreter: C:\Users\dcorbin\AppData\Local\Programs\Python\Python37\python.exe
#       ansible_shell_type: cmd
