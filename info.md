# Information on the tasks performed

I have used different approaches to perform the tasks.

1.A couple of files and directories are created:

| File/directory       | Contents                                                            |
|----------------------|---------------------------------------------------------------------|
| api                  | Directory where Fast API has been Implemented                       |
| DB                   | Directory where physical data model resides                         |
 | docs                 | Directory where useful documents like requirements are placed       | 
 | task                 | Directory Where actual task is performed                            |
 | .env                 | File containing secret keys/password                                |
 | main.py              | Program runs from here                                              |
 | requirement.txt      | File containing the dependency of the project                       |
 | transactions.db      | this file is available in root and test which contains the database |
 | test                 | Directory where unit test are performed                             |
 | task/config.py       | contains the configurations to run the tasks                        |
 | task/dbconnection.py | different methods to connect to the database                        |


2. Db connections are performed via different ways using db specific connection and sqlalchemy
3. As I love TDD unittest are created and run for the first 2 tasks.
4. A sample API via FastAPI is done which is not part of the requirement just to add some value to the task
5. Changelog captured in each file and docstring provided for each function implementation.


