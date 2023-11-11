## Python WEB EXTRACTOR

This python script fetches a webpage with its headers using HTTP/1.0 . it then goes urther to store header keys and values as json in an `info.json` file and the html contents in a `content.html` file

## Usage

import the `extract_from_web()` function from `main.py` an use it by passing it an argument, only the host of the webpage you want to access i.e `google.com`

```python

from main import extract_from_web

myweb = "google.com" #only the host 
extract_from_web(myweb) #this will get the webpage, store its headers in a json and contents in a html file
```
