import json

def toJson(data:list) :
    data_dict = {}

    for line in data :
        first_pos = line.find(":")

        if first_pos < 0 :
            key = line.strip()
            value = ""
        else :
            key = line[0:first_pos].strip()
            value = line[(first_pos+1):].strip()

        data_dict[key] = value
    
    fhandle = open("info.json" , 'w')

    try :
        fhandle.write(json.dumps(data_dict))
        return True
    except :
        return False
     