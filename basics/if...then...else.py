def calculate_cost (quantity,expensive):
    if expensive:
        return quantity*10
    else:
        return quantity*5

print (calculate_cost(3,True))
print (calculate_cost(3,False))

def ticket_price(age):
    if age<13:
        return 5
    elif age<=17:
        return 10
    else:
        return 20

print (ticket_price(10))
print (ticket_price(17))
print (ticket_price(15))
print (ticket_price(20))
