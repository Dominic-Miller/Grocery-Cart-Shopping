
ShopInventory = ['Bananas','Cucumbers','Peppers','Zucchini','Sweet Onions', 'Chicken','Beef','Bread']
ItemCost = [0.24,0.58,.5,.76,1.1,2.78,2.25,2.88]
ItemBought= [0,0,0,0,0,0,0,0]


can_spend=float(input("How much money do you plan to spend?: $"))
# can_spend=round(can_spend,2)


to_buy=0
num_bananas=0
num_cucumbers=0
num_peppers=0
num_zucchini=0
num_sweetonions=0
num_chicken=0
num_groundbeef=0
num_bread=0

cost_banana=0
cost_cucumber=0
cost_pepper=0
cost_zucchini=0
cost_sweetonion=0
cost_chicken=0
cost_groundbeef=0
cost_bread=0

total_cost=0

def user_price(number,cost):
  price = float(number*cost)
  return price

def shopping_receipt(x):
  for x in range(len(ShopInventory)):
    if num_bananas>0 or num_bread>0 or num_chicken>0 or num_cucumbers>0 or num_groundbeef>0 or num_peppers>0 or num_sweetonions>0 or num_zucchini>0:
      print("Item    :\t {0}".format(ShopInventory[x]))
      print("Quantity:\t {0}".format(ItemBought[x]))
      print("Price:  :\t ${0:.2f}".format(ItemCost[x]))
    else: 
      print("You have not purchased anything.")


#Main code, buying all the items wanted with given amount of money

while to_buy!="9":

  to_buy=input("What would you like to buy? \n Press 1 for Bananas $0.24 \n Press 2 for Cucumbers $0.58 \n Press 3 for Peppers $0.50 \n Press 4 for Zucchini $0.76 \n Press 5 For Sweet Onions $1.10 \n Press 6 for Chicken $2.78 \n Press 7 for Ground Beef $2.25 \n Press 8 for Bread $2.88 \n Press 9 to exit \n Enter Number: ")
  
  if to_buy=="1":
    num_bananas=int(input("How many Bananas would you like to buy?: "))
    total_cost+=user_price(num_bananas,0.24)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_bananas,0.24)
      num_bananas=0
      break
    else:
      ItemBought[0]=num_bananas
      cost_banana=ItemCost[0]=user_price(num_bananas,0.24)
    
   
  elif to_buy=="2":
    num_cucumbers=int(input("How many Cucumbers would you like to buy?: "))
    total_cost+=user_price(num_cucumbers,0.58)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_cucumbers,0.58)
      num_cucumbers=0
      break
    else:
      ItemBought[1]=num_cucumbers
      cost_cucumber=ItemCost[1]=user_price(num_cucumbers,0.58)
    
    
  elif to_buy=="3":
    num_peppers=int(input("How many Peppers would you like to buy?: "))
    total_cost+=user_price(num_peppers,0.50)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_peppers,0.50)
      num_peppers=0
      break
    else:
      ItemBought[2]=num_peppers
      cost_pepper=ItemCost[2]=user_price(num_peppers,0.50)
    
   
  elif to_buy=="4":
    num_zucchini=int(input("How much Zucchini would you like to buy?: "))
    total_cost+=user_price(num_zucchini,0.76)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_zucchini,0.76)
      num_zucchini=0
      break
    else:
      ItemBought[3]=num_zucchini
      cost_zucchini=ItemCost[3]=user_price(num_zucchini,0.76)
    
    
  elif to_buy=="5":
    num_sweetonions=int(input("How many Sweet Onions would you like to buy?: "))
    total_cost+=user_price(num_sweetonions,1.10)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_sweetonions,1.10)
      num_sweetonions=0
      break
    else:
      ItemBought[4]=num_sweetonions
      cost_sweetonion=ItemCost[4]=user_price(num_sweetonions,1.10)
    
    
  elif to_buy=="6":
    num_chicken=int(input("How much Chicken would you like to buy?: "))
    total_cost+=user_price(num_chicken,2.78)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_chicken,2.78)
      num_chicken=0
      break
    else:
      ItemBought[5]=num_chicken
      cost_chicken=ItemCost[5]=user_price(num_chicken,2.78)
    
    
  elif to_buy=="7":
    num_groundbeef=int(input("How much Ground Beef would you like to buy?: "))
    total_cost+=user_price(num_groundbeef,2.25)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_groundbeef,2.25)
      num_groundbeef=0
      break
    else:
      ItemBought[6]=num_groundbeef
      cost_groundbeef=ItemCost[6]=user_price(num_groundbeef,2.25)
    
    
  elif to_buy=="8":
    num_bread=int(input("How much Bread would you like to buy?: "))
    total_cost+=user_price(num_bread,2.88)
    if total_cost>can_spend:
      print("You do not have enough money.")
      total_cost-=user_price(num_bread,2.88)
      num_bread=0
      break
    else:
      ItemBought[7]=num_bread
      cost_bread=ItemCost[7]=user_price(num_bread,2.88)
   

  elif to_buy=="9":
    break
  

  else:
    print("Please enter a valid number.")
    continue


count=0
for num in ItemBought:
  if num==0:
    ItemCost[count]=0
  count+=1

while 0 in ItemBought:
  ItemBought.remove(0)

while 0 in ItemCost:
  ItemCost.remove(0)
  
#Removing items not bought from list

if num_bananas==0:
  ShopInventory.remove("Bananas")

if num_cucumbers==0:
  ShopInventory.remove("Cucumbers")

if num_peppers==0:
  ShopInventory.remove("Peppers")

if num_zucchini==0:
  ShopInventory.remove("Zucchini")

if num_sweetonions==0:
  ShopInventory.remove("Sweet Onions")

if num_chicken==0:
  ShopInventory.remove("Chicken")

if num_groundbeef==0:
  ShopInventory.remove("Beef")

if num_bread==0:
  ShopInventory.remove("Bread")

shopping_receipt(ItemBought)

if num_bananas>0 or num_bread>0 or num_chicken>0 or num_cucumbers>0 or num_groundbeef>0 or num_peppers>0 or num_sweetonions>0 or num_zucchini>0:
  print("Total Price: ${0:.2f}".format(sum(ItemCost)))
  print("Change Due: ${0:.2f}".format(can_spend-sum(ItemCost)))