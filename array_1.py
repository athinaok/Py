ShoppingCart =[1,2,3,4]
'''
ShoppingCart.append( input("Add new item:"))
ShoppingCart.append( input("Add new item:"))
ShoppingCart.append( input("Add new item:"))
ShoppingCart.append( input("Add new item:"))
'''

print(ShoppingCart)
ShoppingCart.pop(1)
print(ShoppingCart)
ShoppingCart.pop()
print(ShoppingCart)
ShoppingCart.pop()
print(ShoppingCart)



print ("List Contains:" , len(ShoppingCart))
ShoppingCart.clear()
print ("List Contains:" , len(ShoppingCart), "after clear")

