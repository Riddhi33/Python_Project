from datetime import datetime
from read import  read_file
from operation import for_buying, for_selling,name_contact,id_validity,quantity_validity, buying_info,for_bill, selling_info
from write import buy_write, sell_write
date_and_time=datetime.now()


print("\n")
print("*****-----*****-----******------*******------******------*******-----******-------******-------******-----******------*******------******")
print("\n")
print("\t \t \t Welcome to RK Laptop Shop")
print("\t \t \t *************************")
print("\n")
print("\t Address:KamalPokhari, Kathmandu       Contact no.: 542378/9842593404")
print("\n")
print("*****-----*****-----******------*******------******------*******-----******-------******-------******-----******------*******------******")
print("\n")
mydictionary = read_file()


continueLoop = True
while continueLoop == True:
    print("\n")
    print("========================================================================================================================================")
    print("Press 1 to buy from manufacturer")
    print("Press 2 to sell to customer")
    print("Press 3 to exit")
    print("=========================================================================================================================================")
    print("\n")
    

    try:
        user_choice = int(input("Press 1,2 or 3: "))
        print("\n")
        if user_choice not in [1,2,3]:
             print ("Please enter only 1,2 or 3")
             print ("\n")
             continue
        
    except:
        print ("\n")
        print("Please enter only the choices provided above")
        continue

    if user_choice == 1:
        buying_info()
        name,contact=name_contact()
        bought_laptops = []

        buy_loop = True
        while  buy_loop == True:
            valid_ID=id_validity()
            provided_quantity=quantity_validity(valid_ID)
            AmountVAT=0
            product_name =  mydictionary[valid_ID][0]
            quantity_by_user = provided_quantity
            unit_price = mydictionary[valid_ID][2]
            price_of_an_item = mydictionary[valid_ID][2].replace("$","")
            total_cost = int(price_of_an_item)*int(quantity_by_user)
        
            bought_laptops.append([product_name, quantity_by_user, unit_price, total_cost])
            
            buy_more = input("Do you want to buy more laptops?(y/n):")
            print("\n")
            
            if buy_more.lower() == "y":
                buy_loop = True
                
            else:
                total = 0
                AmountVAT = 0
                for i in bought_laptops:
                    total+=int(i[3])
                AmountVAT = 0.13 * total
                all_total = total + AmountVAT

                for_bill(name, contact, date_and_time, bought_laptops)
                for_buying(valid_ID,provided_quantity,bought_laptops,total_cost,AmountVAT,all_total)
                buy_write(name,contact,bought_laptops,AmountVAT,all_total)
                buy_loop = False
            
    elif user_choice == 2:
        selling_info()
        name,contact=name_contact()
        bought_laptops = []
        
        sell_loop = True
        while  sell_loop == True:
            valid_ID=id_validity()
            provided_quantity=quantity_validity(valid_ID)
            shipping_value=0
            product_name =  mydictionary[valid_ID][0]
            quantity_by_user = provided_quantity
            unit_price = mydictionary[valid_ID][2]
            price_of_an_item = mydictionary[valid_ID][2].replace("$","")
            total_cost = int(price_of_an_item)*int(quantity_by_user)
            
            bought_laptops.append([product_name, quantity_by_user,price_of_an_item, total_cost])

            sell_more = input("Do you want to purchase more laptops?(y/n):")
            print("\n")

            if sell_more.lower() == "y":
                    sell_loop = True
                      
            else:   
                    total = 0
                    shipping_value = 0
                    for i in bought_laptops:
                        total+=int(i[3])
                    all_total = total + shipping_value

                    
                    for_bill(name, contact, date_and_time, bought_laptops)
                    for_selling(valid_ID,provided_quantity,date_and_time, bought_laptops ,shipping_value, all_total)
                    sell_write(name,contact,date_and_time,bought_laptops,shipping_value,all_total)
                    

                    sell_loop=False

    elif user_choice == 3:
        print("Thank you for visiting our shop!!! ")
        print("Hoping to see you again!!!")
        continueLoop = False

    
