
#Might and Magic
#Warrior : ATTACK 200 , Magic : 10
#Magician : ATTACK 10 , Magic : 200

#make character dictionary #1 with Warrior
#1. name : character name
#2. att : attack power
#3. magic : magic power
#4. hp : health point
#5. mp : magic point (count for spell magic)
#6. speed : the faster, attack first
#EX) character_1 = {"name":"Thief", "att":120, "magic":160, "hp":1000, "mp":5, "speed": 100 }

my_character_dict = {"name":"Monkey", "att":1, "magic":100, "hp":300, "mp":10, "speed": 1000 }
my_enemy_dict = {"name":"devil", "att":1000, "magic":1000, "hp":10000, "mp":1000, "speed": 1000 }

#function : show_character_data
#input : character data dictionary
#output : None (just print character data)
def  show_character_data(character_dict):
   print("You are a " +character_dict["name"]+ ". ATTACK : " + str(character_dict["att"]) + " MAGIC : " + str(character_dict["magic"])+" HP: "+ str(character_dict["hp"])+" MP: "+str(character_dict["mp"])+" SPEED: "+str(character_dict["speed"])+".")
  
def  show_enemy_data(character_dict):
   print("You encount a " +character_dict["name"]+ ". ATTACK : " + str(character_dict["att"]) + " MAGIC : " + str(character_dict["magic"])+" HP: "+ str(character_dict["hp"])+" MP: "+str(character_dict["mp"])+" SPEED: "+str(character_dict["speed"])+".")
  
  
#main Program
print("****** WELCOME TO MIGHT AND MAGIC ******")

#Choose character
#getinput from User : choose character : 1:warrior 2:magician
character_number=int(input("choose your character [ Enter number ]:"))

#file read
f= open("character_data.txt")
counter=0
for line in f:
  new_line = line.rstrip()
  counter=counter+1
  if counter==character_number:
    #parse character data 
    #print(new_line)
    char_data = new_line.split(",")
    #print(char_data) # string to list (array)
    #array -> dictionary
    my_character_dict = {"name":char_data[0],"att":char_data[1],"magic":char_data[2], "hp":char_data[3], "mp":char_data[4], "speed":char_data[5]}
    #print(char_dict)
f.close()

show_character_data(my_character_dict)

#Encount Enemy!!!
print("!!!!!! *[CAUTION]* YOU ENCOUNT ENEMY *[CAUTION]* !!!!!!")
enemy_number=int(input("select your enemy[enter number]:"))

f= open("enemy_data.txt")
counter=0
for line in f:
  new_line = line.rstrip()
  counter=counter+1
  if counter==enemy_number:
    #parse character data 
    #print(new_line)
    char_data = new_line.split(",")
    #print(char_data) # string to list (array)
    #array -> dictionary
    my_enemy_dict = {"name":char_data[0],"att":char_data[1],"magic":char_data[2], "hp":char_data[3], "mp":char_data[4], "speed":char_data[5]}
    #print(char_dict)
f.close()

show_enemy_data(my_enemy_dict)


'''
#if - 1: warrior 2: magician
#give instruction of selected character (name :*** , Att:***, Magic:***)
if character_number==1:
  show_character_data(character_1)
elif character_number==2:
  show_character_data(character_2)
else:
  show_character_data(monkey)
'''


#1. Parse data : file(I/O) + split
#2. percentage : randint
#3. make function : select character(int num)
#5. Make Hero
#6. Make Enemy
#3. save game : file output
#4. load game : file read
#7. Fight function :
# which has more power : ATT
# who attack first? 
# remain HP
# remain MP
