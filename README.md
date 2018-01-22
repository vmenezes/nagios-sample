# nagios-sample

```
cd provisioner
vagrant up
vagrant ssh
mkvirtualenv venv
cd /vagrant/
pip install -r requirements.txt
vi inventory
...
...
...
ansible-playbook -i inventory ./playbook.yml
# ansible-playbook -i inventory -l nagios3_server ./playbook.yml
# ansible-playbook -i inventory -l monitored_clients ./playbook.yml
```