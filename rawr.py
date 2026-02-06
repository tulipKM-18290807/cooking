#import random & time as well
import random
import time

#function
def what_day_bro(day):
    if day == 0:
        return 'Happy Monday'
    elif day == 1:
        return 'Happy Tuesday'
    elif day == 2:
        return 'Happy Wednesday'
    elif day == 3:
        return 'Happy Thursday'
    elif day == 4:
        return 'Happy Friday'
    elif day == 5:
        return 'Happy Saturday'
    else:
        return 'Happy Sunday'


#main program

current_time = time.localtime()
print(what_day_bro(current_time.tm_wday))
formatted= time.strftime("%H:%M%p", time.localtime())
print("Current time right now is: ",formatted)

k = ['Fried','Salad','Soup']
meat_or_no_meat = ['yes meat','no meat']
types_of_carb = [ 'rice','vermecellis','noodles']
s = random.choice(k)
meat = random.choice(meat_or_no_meat)
carbs = random.choice(types_of_carb)

print("Today's meal is: ",s , meat, carbs)

#recipes_included = [

