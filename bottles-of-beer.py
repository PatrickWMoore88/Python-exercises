import time

#Set Variables
bottles_of_beer = 99
on_the_wall = " on the wall"
take_one = "Take one down and pass it around, "

#While Loop containing song made out of above varibales
while bottles_of_beer > 1:
    bottles_phrase = f"{bottles_of_beer} bottles of beer"
    print(f"{bottles_phrase}{on_the_wall}, {bottles_phrase}")
    time.sleep(3) #delays for 3 secs
    bottles_of_beer = bottles_of_beer -1
    print(f"{take_one} {bottles_of_beer} bottles of beer{on_the_wall}")
    time.sleep(3) #delays for 3 secs
    print("=================================================================")
    #If statement for when we get to 1 bottle of beer
    if bottles_of_beer == 1:
        print(f"1 bottle of beer{on_the_wall}, 1 bottle of beer!")
        time.sleep(3) #delays for 3 secs
        bottles_of_beer = bottles_of_beer -1
        print(f"Take it down and pass it around, no more bottles of beer {on_the_wall}")
        time.sleep(3) #delays for 3 secs
        print("=================================================================")
    #Elif statement for when we get to 0 bottles of beer
    elif bottles_of_beer == 0:
        break
#Closing lines of the song  
print(f"There is no more bottles of beer{on_the_wall}, no more bottles of beer.")
time.sleep(10) #delays for 10 secs     
print("Go to the store and buy some more, 99 bottles of beer on the wall!")
time.sleep(10) #delays for 10 secs
    