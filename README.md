# bad_words

### Help tace to run code
```
$ python main.py -h
usage: main.py [-h] --text TEXT --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --text TEXT  Enter the text to check and remove bad words
  --path PATH  Enter the path of bad word dataset

```

#### Example run comand
```
$ python main.py --text "You are an ass" --path ./data/badwords.txt

```
#### Result
```
!!Warning bad word(s) are present!!
You are an $$$
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