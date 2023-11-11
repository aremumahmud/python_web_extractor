
from getinfo import readPage
from splitpage import split_page
from toJSON import toJson


def extract_from_page(page) :

    data = readPage("google.com")

    if data == False :
        return { "error":True, "message":"could not connect to server"}
    # split_page(data)
    splitted_data = split_page(data)

    covert_and_store = toJson(splitted_data[0])

    if covert_and_store == False :
        return { "error":True, "message":"could not store json file"}

    try :
        fhandle = open("page.html" , 'w')
        fhandle.write(splitted_data[1])
    except :
        return { "error":True, "message":"could not store html file"}
    
    return {"error": False, "message":"sucessfully extracted and stored the extracted data"}
    
    
# fhandle = open("output.txt" , "w")

# fhandle.write(data)