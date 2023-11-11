
from getinfo import readPage
from splitpage import split_page
from toJSON import toJson


def extract_from_page(page) :

    data = readPage("google.com")
    # split_page(data)
    splitted_data = split_page(data)

    toJson(splitted_data[0])

    fhandle = open("page.html" , 'w')
    fhandle.write(splitted_data[1])
# fhandle = open("output.txt" , "w")

# fhandle.write(data)