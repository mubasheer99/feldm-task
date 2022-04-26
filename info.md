# Information on the task performed

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


2. Db connection are performed via different way used db specific connection and sqlalchemy
3. As I love TDD unittest are carted and run for first 2 tasks.
4. A sample API via FastAPI is done which uis not part of teh requirement some values add.
5. Changelog captured in each file and docstring provided for each package implementation.


