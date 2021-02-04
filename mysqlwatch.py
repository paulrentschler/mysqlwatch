#!/usr/bin/env python
"""Check the replication status of MySQL replica servers

Meant to be run regularly by Cron. As such output is only generated when
there is a problem so Cron can forward it an administrator via email.
"""
import subprocess


class MySqlWatch(object):
    def check(self):
        """Initiates the check to see if the replica is working properly"""
        status_text = self._get_status()
        if not status_text:
            print('Failed to get the status of the MySQL server!')
            return
        status = self._parse_status(status_text)
        replica_io_error = status['Slave_IO_Running'] != 'Yes'
        replica_sql_error = status['Slave_SQL_Running'] != 'Yes'
        if replica_io_error or replica_sql_error:
            print('The MySQL Replica server is not replicating!\n')
            print(' IO Running: {}'.format(status['Slave_IO_Running']))
            print('SQL Running: {}'.format(status['Slave_SQL_Running']))
            print('\nLast Error:\n{}'.format(status['Last_Error']))
            print('\nLast SQL Error:\n{}'.format(status['Last_SQL_Error']))
            print('')

    def _get_status(self):
        """Returns the replication status of the MySQL server"""
        try:
            return subprocess.check_output(
                ['mysql', '-e', 'SHOW SLAVE STATUS\\G'],
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError as e:
            print(e)
            return False

    def _parse_status(self, status_text):
        """Parse the status text returned by the MySQL server into a dict

        Arguments:
            status_text {str} -- Output from the MySQL status command

        Returns:
            {dict} -- MySQL status key/value output converted to Python dict
        """
        status_dict = {}
        for line in status_text.decode('utf-8').strip().split('\n'):
            try:
                (key, value) = line.strip().split(':', 1)
            except ValueError:
                # There was no colon (:) in `line`, so ignore it
                pass
            else:
                status_dict[key.strip()] = value.strip()
        return status_dict


if __name__ == '__main__':
    watchdog = MySqlWatch()
    watchdog.check()
