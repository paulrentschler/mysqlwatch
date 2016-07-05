#!/usr/bin/env python
"""
Script for checking to on the replication status of MySQL slaves

Meant to be run as a cron job such that if everything is functioning correctly
no output is generated. If there is a problem, then the issue is output and
cron will capture it and send it to an administrator via email.
"""
import subprocess


class MySqlWatch(object):
    def check(self):
        """
        Initiates the check to see if the slave is working properly
        """
        status_text = self._get_status()
        if not status_text:
            print("Failed to get the status of the MySQL server!")
            return
        status = self._parse_status(status_text)
        if status['Slave_IO_Running'] != 'Yes' or status['Slave_SQL_Running'] != 'Yes':
            print("The MySQL Slave Server is not replicating!\n")
            print(" Slave IO Running: %s" % status['Slave_IO_Running'])
            print("Slave SQL Running: %s" % status['Slave_SQL_Running'])
            print("\nLast Error:  %s" % status['Last_Error'])
            print("\nLast SQL Error: %s" % status['Last_SQL_Error'])
            print("")


    def _get_status(self):
        """
        Returns the status of the MySQL server
        """
        try:
            status = subprocess.check_output(
                ['mysql', '-e', 'show slave status\G'],
                stderr=subprocess.STDOUT,
                )
        except subprocess.CalledProcessError as e:
            print(e)
            return False
        else:
            return status


    def _parse_status(self, status_text):
        """
        Parse the status text returned by the MySQL server into a dict
        """
        status_dict = {}
        for line in status_text.decode('utf-8').strip().split("\n"):
            try:
                (key, value) = line.strip().split(":", 1)
            except ValueError:
                # There was no colon (:) in `line`, so ignore it
                pass
            else:
                status_dict[key.strip()] = value.strip()
        return status_dict


if __name__ == '__main__':
    watchdog = MySqlWatch()
    watchdog.check()

