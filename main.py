import random
##Hecho por Valeria martinez y Valeria Bastidas
print("="*60)
print("MEDIEVAL KINGDOM")

print("1. Easy \n"+
      "2. Medium \n"+
      "3. Hard \n"+
      "4. Exit")

print("="*60)
print("Choose a difficulty number: \n" + 
                "="*60)
option=input()

#MOTOR DE JUEGOS

##Juan Bolaños y Randy Pérez

if option == "4" :
    print("Exit The Game")
else:
    wheat = 0
    firewood = 0
    gold = 0  

 #ASIGNACION DE RECURSOS

 ##Salomon Garcia y Mathias Fernandez
  
    if option == "1":
        
        wheat = 200
        firewood = 200
        gold = 150  
        spent_wheat = 10
        spent_firewood = 5
        spent_gold = 4
      

    elif option == "2":
        
        wheat = 150
        firewood = 150
        gold = 100                  
        spent_wheat = 15
        spent_firewood = 6
        spent_gold = 8
      

    elif option == "3":
        
        wheat = 80
        firewood = 60
        gold = 40  
        spent_wheat = 20
        spent_firewood = 8
        spent_gold = 10
 
    else:
        print("Invalid option...")
        wheat = 0
        firewood = 0
        gold = 0
     
#Validación y conteo de días

## Andrés Cortés y Alejandro Villanueva

    if wheat > 0 and gold > 0 and firewood > 0:
        day = 0
        keep_playing = "Y"

        while keep_playing == "Y" and wheat > 0 and gold > 0 and firewood > 0:
            day += 1
            
            #Consumo base
            wheat = wheat - spent_wheat
            firewood = firewood - spent_firewood
            gold = gold - spent_gold 
            event = "No events today."
            wheat_loss = 0
            firewood_loss = 0
            gold_loss = 0

            #events generator

            random_number = random.randint(1,100)
            
            if random_number <= 20:
                event = "Ravenous hunger"
                wheat_loss = random.randint(10,30)
                wheat = wheat - wheat_loss
        
            elif random_number <= 40:
                event = "Asault"
                gold_loss = random.randint(10,30)
                gold = gold - gold_loss

            elif random_number <= 60:
                event = "Burning"
                firewood_loss = random.randint(10,30)
                firewood = firewood - firewood_loss
            
    #Daily info
            print("="*60)
            print(f"Day: {day}")
            print(f"Actual resources: wheat {wheat} - firewood {firewood} - gold {gold}  ")
            print("="*60)
            print(f"Daily event: {event}")
            print(" ")
            print(f"additional wheat loss {wheat_loss}")
            print(" ")
            print(f"additional firewood loss {firewood_loss}")
            print(" ")
            print(f"additional gold loss {gold_loss}")
            print("="*60)
            if wheat <= 0 or firewood <= 0 or gold <= 0:
                    print("Your kingdom has fallen")
            
            else:
                print("="*60)
                keep_playing = input("move on the next day? (Y/N): ").upper()
