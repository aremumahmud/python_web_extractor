## Python WEB EXTRACTOR

This python script fetches a webpage with its headers using HTTP/1.0 . it then goes further to store header keys and values as json in an `info.json` file and the html contents in a `content.html` file

## Usage

import the `extract_from_web()` function from `main.py` an use it by passing it an argument, only the host of the webpage you want to access i.e `google.com`

```python

from main import extract_from_web

myweb = "google.com" #only the host 
extracted = extract_from_web(myweb) #this will return a dictionary for success and error messages
```

### Message format returned from the function

```python

# for sucess messages it will return 
 {"error": False, "message":"sucessfully extracted and stored the extracted data"}

# for an error message when storing the json fails due to permissions
{ "error":True, "message":"could not store json file"}

## for an error message when storing the html fails due to permissions
{ "error":True, "message":"could not store html file"}
```
