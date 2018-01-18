#!/usr/bin/env python3

import os, socket

def check_restart_required():
    if os.path.exists('/var/run/reboot-required'):
        print('*** System restart required *** ')
        exit(2)
    print('OK, no system restart needed')
    exit(0)


if __name__ == '__main__':
    check_restart_required()


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
