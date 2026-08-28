# define the menu of restaurant
menu={                                 #using list
    'pizza':40,
    'shaurma':60,
    'pasta':50,
    'noodles':70,
    'burgers':80,
    'chicken rice':100,
    'salad':200,
   'coffee':300,
}
#greet
print("welcome to our python restaurant sir/mam")
print(menu)
#print("pizza:RS40\nshaurma:RS60\npasta:RS50\nnoodles:RS70\nburger:RS80\nfrankie:RS90\nchicken rice:RS100\nsalad:RS200\ncoffee:RS300")
order_total=0
item_1=input("enter the name of the item you want to order:")
#print("item_1")
if item_1 in menu:
 order_total+=menu[item_1]
 print(f"your item {item_1} has been added to your order")
else:
 print(f"sorry ordered item {item_1} is not available yet")
another_order=input("do you want to add another item?(y/n):")
if another_order=="y":
 item_2=input("enter the name of the second item:")
 if item_2 in menu:
  order_total+=menu[item_2]
 print(f"your item {item_2} has been added to your order successfully")
else:
  print("ok!,thank you for visiting our restaurant!")
print(f"total amount of your item to pay is rs {order_total}")
print("thank you for visiting our restaurant!")