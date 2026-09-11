def ticket_price(age):
    if age>=18:
        return 20
    else:
        return 10

print (ticket_price(20))
print (ticket_price(15))

def calculate_cost (quantity,expensive):
    if expensive:
        return quantity*10
    else:
        return quantity*5

print (calculate_cost(3,True))
print (calculate_cost(3,False))
