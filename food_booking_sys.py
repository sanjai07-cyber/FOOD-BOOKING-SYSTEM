
import pywhatkit as what
import time as t
from datetime import datetime, timedelta

Menu={
    "100":["CHICKEN BRIYANI",149],
    "101":["CHICKEN 65",129],
    "102":["CHICKEN PERI PERI(LARGE)",199],
    "103":["CHICKEN WINGS",159],
    "104":["CHICKEN MANJURIAN",159],
    "105":["CHICKEN LOLPOP",199],
    "106":["GRILED CHICKEN",259],
    "107":["MUTTON BRIYANI",259],
    "108":["MUTTON GRILL",355],
    "109":["MUTTON GRAVY",350],
    "110":["MUTTON KEBAB",220],
    "111":["MUTTON GEEROAST",280],
    "112":["FISH FRY",180],
    "113":["FISH BRIYANI",350],
    "114":["CHILL FISH",180],
    "115":["PRAWN VARUVAL",199],
    "116":["PAR0TTA WITH EGGCURY",169],
    "117":["BUTTER NAN",120],
    "118":["GARLIC NAN",145],
    "119":["MOJITO MINT",120],
    "120":["ICE CREAM",145]
}


order=[]
shop_name="SLM HOTEL"

def menu():
    
    print(shop_name.center(60,"="))
    print("\nCode     Item Name                      Price")
    print("="*60)
    for i in Menu:
        item_detail=Menu[i]
        food_name=item_detail[0]
        food_price=item_detail[1]
        print(f"{i}      {food_name:<30} Rs:{food_price:.2f}")
    print("="*60)



def order():
    wel="WELCOM TO SLM ONLINE ORDER"
    print(wel.center(60,"="))

    name=input("Enter Your Name:")
    
    phone=input("Enter Your phone Number:")
    order_type=int(input("\n1.dine-in\n2.takeaway\nSelect Your Order Type:"))
    
    customer_cart=[]


    while True:
        menu()
        item_code=input("Enter Item code to add to your cart or type 'exit' or 'e' to Exit:")

        if item_code=="e" or item_code=="exit" or item_code=="EXIT" or item_code=="Exit":
            if len(customer_cart)==0:
                print("your cart is empty!")
                return
            break
        
        if item_code in Menu:
            qty=int(input("Enter how many pices do you want:"))
            if qty<=0:
                print("Quantity must be atleast one or morethan one")
                continue

            ordered_food = Menu[item_code]
            add_item = {
                "code":item_code,
                "name":ordered_food[0],
                "price":ordered_food[1],
                "qty":qty
            }

            customer_cart.append(add_item)
            print("FOOD ADD TO YOUR BUCKET!".center(60," "))
        else:
            print("Invaild code. please select code from menu!")


    Total=0
    for a in customer_cart:
        item_cost= a["price"]*a["qty"]
        Total+=item_cost
    gst=Total*0.16
    Grand_Total=Total+gst


    receipt=""

    receipt+="="*60
    receipt+="\n"
    receipt+=shop_name.center(60,"=")
    receipt+="\n"
    receipt+=f"customer: {name}\nphone no: {phone}\n"
    receipt+="-"*60
    for a in customer_cart:
        item_total=add_item["price"]*add_item["qty"]
        receipt+=f"\n{a['name']:<20}                {a['qty']}x      Rs:{item_total:.2f}\n"
    receipt+="-"*60
    receipt+="\n"
    receipt+=f"subtotal:                                  rs{Total:.2f}\n"
    receipt+=f"GST(16%):                                  rs{gst:.2f}\n"
    receipt+="="*60
    receipt+="\n"
    receipt+=f"Total paid:                                rs{Grand_Total:.2f}\n"
    receipt+="="*60

    print(receipt)

    
    for j in range(1):
        if order_type==1:
            print("Your order is Ready in 5 mintiues")
            t.sleep(10)
            print("Your order is ready 'STAY THERE Your order reach Your table'")
        elif order_type==2:
            print("Your order is Ready in 10-15 mintues")
            t.sleep(10)
            print("Your order is ready 'GET FROM COUNTER'")
        else:
            print("incorrect input try again")

    now = datetime.now() + timedelta(minutes=2)
    what .sendwhatmsg(
        phone,
        f"dear customer {name}\nYour order is ready !\n{receipt} ",
        now.hour,
        now.minute
        )


        
            




def main():
    while True:
        print("\n==========================================")
        print("          SLM HOTEL BOOKING ENGINE          ")
        print("==========================================")
        print("1. Order Food ")
        print("2. Turn Off System")


        MENU_selection=int(input("sectect an option:"))


        if MENU_selection==1:
            order()
        elif MENU_selection==2:
            print("exit from apllication")
            break
        else:
            print("Incorrect input")

if __name__=="__main__":
    main()

        
            

            
    
        
        


        
    
    
