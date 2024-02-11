from read import read_file
from datetime import datetime


mydictionary = read_file()


def id_validity():
    '''Checks the validity of the id entered by the user'''
    valid_ID = int(input("Please provide the ID of the Laptop you want to buy: "))
    print ("\n")
   
    #Valid ID
    while valid_ID <= 0 or valid_ID > len(read_file()):
        print("Please provide a valid Laptop ID!!!")
        print("\n")
        valid_ID = int(input("Please provide the ID of the Laptop you want to buy: "))
        print("\n")
                
        
    return valid_ID
        
       
def quantity_validity(valid_ID):
    '''Checks the validity of the quantity entered by the user'''
    #valid quantity
    provided_quantity = int(input("Please provide the number of Laptop you want to buy: "))
    
    our_quantity = mydictionary[valid_ID][3]
    while provided_quantity <= 0 or provided_quantity > int(our_quantity):
        print("The quantity of laptop you are looking for is out of stock. Please look again in the list properly.")
        print("\n")
        provided_quantity = int(input("Please provide the number of Laptop you want to buy: "))
    print("\n")
    return provided_quantity

date_and_time=datetime.now()            
def for_bill(name, contact, date_and_time, bought_laptops):
            '''Contains every details required in a bill'''
            print("\t \t \t \t RK LAPTOP SHOP BILL ")
            print("\t \t \t \t *********************")
            print("\n")
            print("\t \t \t Kamalpokhari, Kathmandi | Phone No: 9876547789 ")
            print("\t \t \t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n")
            print("****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****")
            print("\n")
            print("\t  Laptop Details are:")
            print("\t  ^^^^^^^^^^^^^^^^^^^")
            print("\n")
            print("\t Name of the customer: "+str(name))
            print("\n")
            print("\t Contact number: "+str(contact))
            print("\n")
            print("\t Date and  time of purchase: "+str(date_and_time))
            print("\n")
            print("****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****-----****")
            print("\n")
            print("Purchase Detail are: ")
            print("\n")
            print("====================================================================================================================================")
            print("Item Name \t  Total Quantity  \t Unit Price \t \t  Total")
            print("======================================================================================================================================")
            for i in bought_laptops:
                print(i[0], " \t",i[1], "\t \t", i[2], "\t \t","$",i[3])
            print("========================================================================================================================================")
            

def name_contact():
    '''Stores the name and contact number of the user'''
    name = input("Enter your name: ")
    print("\n")
    while True:
        try:
            contact = input("Enter your mobile number: ")
            print("\n")
            if (len(contact)) != 10:
                print("Please input valid 10 digit numbers")
                print("\n")
                continue
            else:
                 break
        except:
                print("Invalid mobile number")

    return name,contact

 
def buying_info():
    '''Shows the laptop inventory to the user for buying'''
    print("Thank you for buying!!!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print("Here are the list of items available in our shop")
    print("-------------------------------------------------")
    print("\n")
    print("==================================================================================================================================================")
    print("ID \t Name \t \t Brand \t \t Price \t \t Quantity  \t Processor \t Graphic Card ")
    print("===================================================================================================================================================")
    a = 1
    file = open("laptop.txt","r")
    for line in file:
        print(a,"\t" + line.replace(",","\t"))
        a+=1
    file.close()
    print("=====================================================================================================================================================")
    print("\n")
    print("For printing the bill, you will need to give us following informations: ")
    print("\n")


def for_buying(valid_ID,provided_quantity,bought_laptops,total_cost,AmountVAT,all_total):
    ''' Shows the VAT amount and total price in the bill '''
    #Update the text file
    mydictionary[valid_ID][3] = int(mydictionary[valid_ID][3]) + int(provided_quantity)
    file = open("laptop.txt","w")

    for values in mydictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

    #getting user purchased items

    total = 0
    for i in bought_laptops:
        total+=int(i[3])
    AmountVAT = 0.13 * total
    all_total = total + AmountVAT


    date_and_time = datetime.now()
            
    if AmountVAT:
                print("VAT Amount:", AmountVAT)
                print("Total Amount: $"+str(all_total))
                print("\n")
                print("VAT Amount has been added to grand total")
    else:
                print("Total Amount: $"+str(all_total))
    return date_and_time,  AmountVAT , all_total, total_cost,  valid_ID,provided_quantity,bought_laptops
        

def selling_info():
    '''Shows the laptop inventory to the user for purchasing'''
    print("Thank you for selling!!!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print("Here are the list of items available in our shop")
    print("-------------------------------------------------")
    print("\n")
    print("====================================================================================================================================================")
    print("ID \t Name \t \t Brand \t \t Price \t \t Quantity  \t Processor \t Graphic Card ")
    print("====================================================================================================================================================")
    a = 1
    file = open("laptop.txt","r")
    for line in file:
        print(a,"\t" + line.replace(",","\t"))
        a+=1
    file.close()
    print("=====================================================================================================================================================")
    print("\n")
    print("For printing the bill, you will need to give us following informations: ")
    print("\n")

    
def for_selling(valid_ID,provided_quantity,date_and_time, bought_laptops ,shipping_value, all_total):
    ''' Shows the shipping cost and total price'''
    #Update the text file
    
    my_id = mydictionary[valid_ID][3]
    mydictionary[valid_ID][3] = int(my_id) - int(provided_quantity)
    file = open("laptop.txt","w")

    for values in mydictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

    #getting user purchased items

    date_and_time = datetime.now()

    
    shipping_value = input("Do you want your laptop to be shipped?(Y/N)").upper()
    if shipping_value == "Y":
        total = 0
        shipping_value = 500
        for i in bought_laptops:
            total+= int(i[3])
        all_total = total + shipping_value
        print("Your Shipping Cost is: ",shipping_value)
        print("Total Amount: $"+str(all_total))
        print("\n")
        print("Shipping cost is added to the grand total")
    else:
        print("Total Amount: $"+str(all_total))
        print("Shipping cost is not added to the grand total")

    return date_and_time, bought_laptops ,shipping_value, all_total, valid_ID,provided_quantity

    
