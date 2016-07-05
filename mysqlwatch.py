"""
Script for checking to on the replication status of MySQL slaves

Meant to be run as a cron job such that if everything is functioning correctly
no output is generated. If there is a problem, then the issue is output and
cron will capture it and send it to an administrator via email.
"""


class MySqlWatch(object):
    def __init__(self):
        """
        Initialization steps
        """
        pass


    def check(self):
        """
        Initiates the check to see if the slave is working properly
        """
        pass


if __name__ == '__main__':
    watchdog = MySqlWatch()
    watchdog.check()
