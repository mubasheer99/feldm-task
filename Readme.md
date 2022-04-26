# Interview Task For FELDM

Complete the Task using the SQLite database transactions.db containing dummy data


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependency for the project.
All the dependency available in requirements.txt file

```bash
pip install -r requirements.txt
```

How to Use This
-------------------


1. Create an  virtual environment using 
```
python3 -m venv
```
2. Install dependencies using below command.
```
pip install -r requirements.txt
```
3. Update the .env file in the root folder with the secret and environmental variable

4. Run tasks using below command.
```
python main.py
```

Testing
---------------
Run Test using the command 
```
python -m unittest -v  .\test\test.py
```

Run API
-----------
An api interface provided using FastAPI and can be run with below command

```
uvicorn api.apidevice:app --reload
```

check api response
-----------------------------
http://127.0.0.1:8000/docs





## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
License file is available in root LICENSE.txt
