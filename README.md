# FastAPI_Postgresql_VRdart

to set up environment and activate it

  ``` 
  python3 -m venv env
  source env/bin/activate
  ```
  
after that we need to install the needed package 

```
pip install -r requirements.txt
```
and then we can run our backend on localhost with this command

```
cd src
uvicorn main:app --reload
```
or you can run it on your IP address that other device in local network can access to 

```

cd src
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

