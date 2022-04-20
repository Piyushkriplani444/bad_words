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