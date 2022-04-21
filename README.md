# bad_words

### Help tace to run code
```
$ python assignment/main.py -h
usage: main.py [-h] --text TEXT --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --text TEXT  Enter the text to check and remove bad words
  --path PATH  Enter the path of bad word dataset

```

#### Example run comand
```
$ python assignment/main.py --text "You are an ass" --path ./data/badwords.txt

```
#### Result
```
!!Warning bad word(s) are present!!
You are an $$$
```

#### Command to run the api
```
$ python assignment/api.py
```
##### Response
```
 * Serving Flask app 'api' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 119-119-676
```

#### Example to hit api using curl
```
$ curl --request GET 127.0.0.1:5000/
```
##### Response
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    50  100    50    0     0   7142      0 --:--:-- --:--:-- --:--:--  8333{
  "data": "Bad Word Api is Running Correctly"
}

```

#### Example to post bad words o api
```
$ curl -i -X POST -H "Content-Type: application/json" -d '{"text":"You are a bad ass"}' 127.0.0.1:5000/bad_words/
```
##### Response
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    78  100    50  100    28   6250   3500 --:--:-- --:--:-- --:--:-- 11142HTTP/1.1 200 OK
Server: Werkzeug/2.1.1 Python/3.8.8
Date: Thu, 21 Apr 2022 09:38:07 GMT
Content-Type: application/json
Content-Length: 50

{
  "bad": true,
  "text": "You are a bad $$$"
}
```


### Command to Run Test Cases
```
$ pytest
```

```
============================= test session starts =============================
platform win32 -- Python 3.8.8, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\piyush\Desktop\bad_words
collected 1 item

tests\test_check_bad_word.py .                                           [100%]

============================== 1 passed in 0.04s ==============================
```