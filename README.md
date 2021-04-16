# MySQL Watch

![Python 3][python-badge]
[![MIT licensed][mit-badge]][mit-link]

A watchdog to monitor whether or not a MySQL replica server is receiving data
from the primary server.


## What it's checking

The script executes the `SHOW REPLICA STATUS` command in the MySQL client and checks that the `Replica_IO_Running` and `Replica_SQL_Running` values are both `Yes`.

The code falls back to the older `SHOW SLAVE STATUS` command and `Slave_IO_Running` and `Slave_SQL_Running` values for older versions of MySQL that do not support the more modern terminology.


## Output

When the replica is properly replicating from the primary, there is no output from the watchdog.

If `Replica_IO_Running` or `Replica_SQL_Running` report `No` then the values of each of these are output along with the values for `Last_Error` and `Last_SQL_Error`.


## Dependencies

None.


## Installation

All that is needed is the single `mysqlwatch.py` file.

1. Clone the repository into a directory (like `/usr/local/src`)
1. Give the `mysqlwatch.py` execute permissions
1. Run the script at the command line with `./mysqlwatch.py`

The script is designed to be run on a regular basis via something like Cron. As such, if everything is functioning correctly no output is generated. If there is a problem, then the issue is output and Cron will send it to an administrator via email.


## Terminology

The author recognizes that the terms used by the MySQL software to describe the server roles in replication, "master" and "slave", are technical accurate but racially insensitive and generally inappropriate. The author further recognizes and appreciates the MySQL community's efforts to address this issue and replace "slave" with "replica".

Wherever possible, the more modern and culturally sensitive terms "primary" and "replica" are used in this project.


## License

[MIT][mit-link]


## Author

Created by Paul Rentschler in 2016.


[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-link]: https://github.com/paulrentschler/mysqlwatch/blob/master/LICENSE
[python-badge]: https://img.shields.io/badge/python-3.x-blue
