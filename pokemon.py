import random

def map():

    # Printing the map.
    pokemonFile = open ("pokemon.txt" , "r")
    address = open("address.txt" , "r")
    location = address.read()
    addressList = location.split(',')
    a = int(addressList[0])
    b = int(addressList[1])
    file = pokemonFile.readlines()
    for i in range(len(file)):
        x = file[i]
        for j in range(len(file[i])):
            if i == a and j == b:
                print('x',end="")
            else:
                if x[j] == '0':
                    print('o',end="")
                elif x[j] == '2':
                    print('#',end="")
        print("")
    address.close()
    pokemonFile.close()

def menu():

    # Choices of movements
    print("1 . Left", "\n")
    print("2 . Right", "\n")
    print("3 . Up", "\n")
    print("4 . Down", "\n")
    print("5. Save and Exit", "\n")

def main():

    # Main program.
    map()
    menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        moveLeft()
    elif choice == 2:
        moveRight()
    elif choice == 3:
        moveUp()
    elif choice == 4:
        moveDown()
    elif choice == 5:
        print("saved")
    else:
        print("1-5 Only!")
        main()

def moveLeft():

    # Move the address of the player (to the left)
    address = open("address.txt" , "r")
    location = address.read()
    addressList = location.split(',')
    a = int(addressList[0])
    b = int(addressList[1])
    b -= 1
    address.close()

    # Check if player is out of map.
    if b >= 0:
        addressList[1] = str(b)
    else:

        # If player reached the end of the map, save the previous address instead.
        address = open("address.txt", "w")
        print("End of Map!")
        addressList[1] = '0'
        new = ",".join(addressList)
        address.write(new)
        address.close()

        main()

    # Save the new address of the player.
    address = open("address.txt", "w")
    new = ",".join(addressList)
    address.write(new)
    address.close()

    # Randomize the chances of encountering something.
    pokemonFile = open("pokemon.txt", "r")
    file = pokemonFile.readlines()
    for i in range(len(file)):
        for j in range(len(file[i])):
            if i==a and j==b:
                if file[a][b] == '2':
                    rand = random.randint(0,100)
                    if rand >= 50:
                        print("You encountered something!")
                    else:
                        print("Nothing is here!")
    pokemonFile.close()
    main()

def moveRight():

    # Move the address of the player (to the right)
    address = open("address.txt" , "r")
    location = address.read()
    addressList = location.split(',')
    a = int(addressList[0])
    b = int(addressList[1])
    b += 1
    address.close()
    address = open ("address.txt","w")

    # Check if player is out of map.
    if b <= 7:
        addressList[1] = str(b)
    else:

        # If player reached the end of the map, save the previous address instead.
        print("End of Map!")
        addressList[1] = '7'
        new = ",".join(addressList)
        address.write(new)
        address.close()

        main()

    # Save the new address of the player.
    new = ",".join(addressList)
    address.write(new)
    address.close()

    # Randomize the chances of encountering something.
    pokemonFile = open("pokemon.txt", "r")
    file = pokemonFile.readlines()
    for i in range(len(file)):
        for j in range(len(file[i])):
            if i==a and j==b:
                if file[a][b] == '2':
                    rand = random.randint(0,100)
                    if rand >= 50:
                        print("You encountered something!")
                    else:
                        print("Nothing is here!")
    pokemonFile.close()
    main()

def moveUp():

    # Move the address of the player (moving up)
    address = open("address.txt" , "r")
    location = address.read()
    addressList = location.split(',')
    a = int(addressList[0])
    b = int(addressList[1])
    a -= 1
    address.close()
    address = open ("address.txt","w")

    # Check if player is out of map.
    if a >= 0:
        addressList[0] = str(a)
    else:

        # If player reached the end of the map, save the previous address instead.
        address = open("address.txt", "w")
        print("End of Map!")
        addressList[0] = '0'
        new = ",".join(addressList)
        address.write(new)
        address.close()

        main()

    # Save the new address of the player.
    address = open("address.txt", "w")
    new = ",".join(addressList)
    address.write(new)
    address.close()

    # Randomize the chances of encountering something.
    pokemonFile = open("pokemon.txt", "r")
    file = pokemonFile.readlines()
    for i in range(len(file)):
        for j in range(len(file[i])):
            if i==a and j==b:
                if file[a][b] == '2':
                    rand = random.randint(0,100)
                    if rand >= 50:
                        print("You encountered something!")
                    else:
                        print("Nothing is here!")
    pokemonFile.close()
    main()

def moveDown():

    # Move the address of the player (moving down)
    address = open("address.txt" , "r")
    location = address.read()
    addressList = location.split(',')
    a = int(addressList[0])
    b = int(addressList[1])
    a += 1
    address.close()
    address = open ("address.txt","w")

    # Check if player is out of map.
    if a <= 7:
        addressList[0] = str(a)
    else:

        # If player reached the end of the map, save the previous address instead.
        print("End of Map!")
        addressList[0] = '7'
        new = ",".join(addressList)
        address.write(new)
        address.close()

        main()

    # Save the new address of the player.
    new = ",".join(addressList)
    address.write(new)
    address.close()

    # Randomize the chances of encountering something.
    pokemonFile = open("pokemon.txt", "r")
    file = pokemonFile.readlines()
    for i in range(len(file)):
        for j in range(len(file[i])):
            if i==a and j==b:
                if file[a][b] == '2':
                    rand = random.randint(0,100)
                    if rand >= 50:
                        print("You encountered something!")
                    else:
                        print("Nothing is here!")
    pokemonFile.close()
    main()

# Calling the main program
main()
