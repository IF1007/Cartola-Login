# Login

To start your application server:

  * Install dependencies with `pip install -r requirements.txt`
  * Start CherryPy webservice `python webservice.py`

Now you can send your requests to [`localhost:3001`](http://localhost:3001).

Available services:

  * Signup:
    - method: `POST`
    - url: `http://localhost:3001/signup`
    - params: `username`, `password`
    - return: `success`
    
  * Signin:
    - method: `POST`
    - url: `http://localhost:3001/signin`
    - params: `username`, `password`
    - return: `success`

