#!/usr/bin/env python3

import os


def check_security_updates_available():
    updates_available_path = '/var/lib/update-notifier/updates-available'
    if os.path.exists(updates_available_path):
        with open(updates_available_path, 'r') as f:
            print(f.read())


if __name__ == '__main__':
    if os.geteuid() == 0:
        check_security_updates_available()
    else:
        output = os.popen(
            '/usr/bin/sudo /usr/bin/python3 /usr/lib/nagios/plugins/check_security_updates').read()
        for line in output.split('\n'):
            if line.find('security update') >= 0 and \
               int(line[:line.index(' ')]) > 0:
                print(line)
                exit(2)
        print('No updates available')
        exit(0)


##################
### EXIT CODES ###
##################

# exit 0 - Whenever the status of the output of the executed script is "OK", Nagios Server would highlight the check with Green color.
# exit 1 - Whenever the status of the output of the executed script is "WARNING", Nagios Server would highlight the check with Yellow color.
# exit 2 - Whenever the status of the output of the executed script is "CRITICAL", Nagios Server would highlight the check with Red color.
# exit 3 - Whenever the status of the output of the executed script is "UNKNOWN", Nagios Server would highlight the check with Grey color.


#############
### Links ###
#############

# Sample custom plugin for NRPE
# http://www.logiqwest.com/TechnicalPapers/HowToRemoteNagiosScript.html

# Digitalocean tutorial
# https://www.digitalocean.com/community/tutorials/how-to-install-nagios-4-and-monitor-your-servers-on-ubuntu-16-04

# Ubuntu tutorial
# https://help.ubuntu.com/lts/serverguide/nagios.html

# Nagios tutorials
# https://support.nagios.com/kb/article/nrpe-how-to-install-nrpe-v3-from-source-515.html#Ubuntu
