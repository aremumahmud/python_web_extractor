def split_page(data:str) :
    
    lines = data.split('\n')
    pageContent = ""
    pageInfo = []
    mode = 'info'
    
    for line in lines :

        if(len(line.replace('\r' , '')) == 0) :
            mode = 'content'

        if mode == 'info' :
            pageInfo.append(line)
        elif mode == 'content' :
            pageContent = pageContent + line

    return [ pageInfo , pageContent]

  