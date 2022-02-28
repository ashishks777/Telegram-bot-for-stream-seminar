from datetime import datetime


def sample_responses(input_text):
    user_message=str(input_text).lower()
    
    if user_message in ("hello","hi","sup"):
        return"HEY! How's it going?"
        
        
    if user_message in ("who are you","who are you?"):
        return"I am a bot"
        
    if user_message in ("hello","hi","sup"):
        return"HEY! How's it going?"   

    if user_message in ("time","time?","date","date?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_message in ("who made you","who made you?"):
        return"I was made by Ashish Kumar Singh "
        
        
        
    if user_message in ("what you can do","what you can do?","what can you do?","what can you do"):
        return"you can check the price list of the food items here"
        
        
    if user_message in ("menu"):
        return'Type \n1."Burgers" to see the list of Burgers\U0001F354\n2."combos" to see the list of combos\U0001F354\U0001F32E\n3."wraps" to see the list of wraps\U0001F32F	\n4."Service" to contact customer service'
    
    if user_message in ("burgers"):
        return"This is the list of tasty burgers available at our place\U0001F60B\n1.McSpicy Paneer Burger -Rs.159\n2.McVeggie Burger -Rs.118\n3.McChicken Burger - Rs.112\n4.McAloo Tikki Burger - Rs.45\n5.Filet-O-Fish Burger- Rs.138	 "
    
    if user_message in ("combos"):
        return"This is the list of Super Combos available at our place\U0001F60B\n1.2 McAloo Tikki + 2 Fries Large- Rs.293\n2.2 McSpicy Paneer + 2 Veg Pizza McPuff + 2 Fries Large + Coke Medium- Rs.688\n3.2 American Cheese Supreme Chicken + 2 Fries Large + 2 Chocolate Shakes- Rs.790\n4.McSpicy Chicken + American Cheese Supreme + McChicken + Chicken Maharaja + 3 Fries Large- Rs.913\n5.McSpicy Paneer + McSpicy Chicken + 2 Fries Large + Coke Medium- Rs.606"
    
    if user_message in ("wraps"):
        return"This is the list of wraps available at our place\U0001F60B\n1.Big Spicy Paneer Wrap- Rs.184\n2.Veg Maharaja Mac- Rs.184\n3.Big Spicy Chicken Wrap- Rs.194\n4.McSaver Big Spicy Chicken Wrap Meal- Rs.310"
    
    
    if user_message in ("service"):
        return"contact us at\n mob:011 2460 4045\n website:https://www.mcdonaldsindia.com/"
        
    if user_message in ("about"):
        return"This bot is made by Ashish Kumar Singh to show the implementation of simple chatbots\n this bot gives information about the pricing of different food items available at mc donalds\n"    
    
    if user_message in ("thank you","thnx","thanks",):
        return"Most Welcome"
    
    return "I don't understand you."
