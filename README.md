# nagios-sample

```
git clone https://github.com/vmenezes/nagios-sample.git
cd nagios-sample/cli-01
vagrant up
cd ../cli-02
vagrant up
cd ../nagios-server
vagrant up
cd ../provisioner
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
# ansible-playbook -i inventory -l ubuntu_clients ./playbook.yml
exit
cd ../nagios-server
vagrant ssh
/usr/lib/nagios/plugins/check_nrpe -H 33.33.33.101 -c check_users
```