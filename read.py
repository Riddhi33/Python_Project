
def read_file():
    file = open("laptop.txt","r")
    Laptop_ID=1
    mydictionary={}
    for line in file:
        line = line.replace("\n","")
        mydictionary.update({Laptop_ID:line.split(",")})
        Laptop_ID+=1
    file.close()
    return mydictionary

