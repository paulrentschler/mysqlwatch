# MySQL Watch

A watchdog to monitor whether or not a MySQL slave server is receiving data
from the master.


## What it's checking

The script executes the `SHOW SLAVE STATUS` command in the MySQL client and
checks that the `Slave_IO_Running` and `Slave_SQL_Running` values are both `Yes`.


## Output

When the slave is properly replicating from the master, there is no output from
the watchdog.

If `Slave_IO_Running` or `Slave_SQL_Running` report `No` then the values of
each of these are output along with the values for `Last_Error` and
`Last_SQL_Error`.
