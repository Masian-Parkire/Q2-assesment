# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

#PSEUDO CODE.
#  input the attributes(length,lessons,agegroup,and title in my Base Class which are the common attributes for all)
#create subclasses for each wich inherits the base class.
#have a method in each subclass.
#output the title of the story, the narrator and the languages I will want my story translated to

class AncestralStory:
    def __init__(self,length,lessons,agegroup,title): 
        self.length=length
        self.lessons=lessons
        self.agegroup=agegroup
        self.title=title
        
       
    
class Story(AncestralStory):
    def __init__(self,title,length):
        self.length=length
        self.title=title
    def record_story(self):
        
        return f"this story is called {self.title} " 
class StoryTeller(AncestralStory):
    def __init__(self,narrator):
       self.narrator=narrator
    def get_storyteller(self):
        
        return f"This story will be narrated by {self.narrator}"      
        
class Translator(AncestralStory): 
    def __init__(self,languageone, languagetwo ): 
         self.languageone=languageone
         self.languagetwo=languagetwo
    
    def translate_story(self):
        return f"Translate this story from {self.languageone} to {self.languagetwo} "
    
    
story1=AncestralStory("long","Obey your parents","children","The Hare and the Hyena")  
print(story1) 
story2=Story("The Ogre","short")
print(story2.record_story())
story3=StoryTeller("Mzee")
print(story3.get_storyteller())
story4=Translator("Kikuyu","English")
print(story4.translate_story())


# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

#PSEUDO CODE
#input the name as a class attribute
#input price and quantity as parameters in the method
#calculate the total value and output it.

class Product:
    def __init__(self,name):
        self.name=name
        # self.price=price
        # self.quantity=quantity
        
    def calculate_total(self,price,quantity):
      a=  price*quantity
    #   return "the orange is "
      return a
        
prod1=Product("Orange")  
print(prod1.calculate_total(35,7))

prod2=Product("Socks")  
print(prod2.calculate_total(300,9))

prod3=Product("pen")  
print(prod3.calculate_total(40,10))

prod4=Product("Bread")  
print(prod4.calculate_total(65,3))

# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.

#PSEUDO CODE
#input the class attributes
#create a class
#have an empty list to hold my books database
#have methods to add new book,search for books,and display bookdetails.
books=[" "]
class LibraryCatalog:
    def __init__(self,title,author,available,year):
        self.title=title
        self.author=author
        self.available=available
        self.year=year
        
        
    def add_new_book(self):
        newbook="The river between"
        for i in newbook:
            if i not in books:
                books.append(i)
        return books
    
    def search_books(self):
        for book in books:
         if book in books:
            return f"{self.title} authored by {self.author} is available" 
         else:
             return f"{self.title} by {self.author} is not available" 
         
    def display_book_details(self):
         return f"The book {self.title} has been written by {self.author} in the year {self.year}."
    
book1=LibraryCatalog("The River and The Source","Margaret Ogolla","is available",1994)    
print(book1.display_book_details())  
print(book1.add_new_book())   
print(book1.search_books()) 

# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations. 

#PSEUDO CODE
#input attributes that make up a flightbooking
#determine a class FlightBooking
#have methods to perform the booking procedure
#output the details of the flight.

class FlightBooking:
    def __init__(self,destination,date,seat,passenger,id):
        self.destination=destination
        self.date=date
        self.seat=seat
        self.passenger=passenger
        self.id=id
    def booking_confirmations(self):
        return f"This seat number {self.seat}, has been booked for {self.passenger} of id number {self.id}"
    def manage_passenger(self):
        return f"THis is {self.passenger} of id number {self.id} and will sit at seat number {self.seat}"
    def available_flights(self):
        return f"The flight to {self.destination} is available on date {self.date}"
    
flight=FlightBooking("Mombasa","11th November",24,"Purity Wanjiku","38907645")
print(flight.manage_passenger())  
print(flight.available_flights())  
print(flight.booking_confirmations())

# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.
    
# class AfricanCuisine:
#     def __init  