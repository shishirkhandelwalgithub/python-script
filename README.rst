pgbackup
========

CLI for backup remote postgreesql database either locally or to s3

preparing the developement
---------------------------
1. ensure ``pip`` and ``pipenv`` are installed
2. clone the repo using : ``git clone git@github.com:example/pgbackup``
3. ``cd`` into the repository
4. fetch development dependencies ``make install``
5. activate virtualenv : ``pipenv shell``

usage
-----
pass in a full databse URL , the storage driver , and the destination

S3 Example w/ bucket name:

::
        $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

:: 
        $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql



running tests
-------------
run tests locally using ``make`` if virtualenv is active

::
        
        $make

if virtualenv isn't active then use:

::

        $ pipenv run make


