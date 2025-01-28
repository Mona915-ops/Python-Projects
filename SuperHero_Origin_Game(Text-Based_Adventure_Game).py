power = None
morality = 50

def encounterVillain():
    global morality
    print("A villain is threatening the city. What will you do?")
    actions = ['fight', 'negotiate']
    userInput = ""
    while userInput not in actions:
        print("Options: fight/negotiate")
        userInput = input().lower()
        if userInput == "fight":
            print("You bravely fight and defeat the villain. The city is saved!")
            morality += 10
        elif userInput == "negotiate":
            print("You try to reason with the villain, but it backfires, and they escape.")
            morality -= 10
        else:
            print("Please choose a valid option.")
    trainingScene()

def trainingScene():
    global power
    print("\nYou begin training to master your powers.")
    print("1. Train your super strength.")
    print("2. Practice controlling your telekinesis.")
    print("3. Experiment with your elemental abilities.")
    choice = input("choose your training focus (1, 2, or 3): ")

    if choice == '1':
        power = "Super Strength"
    elif choice == '2':
        power = "Telekinesis"
    elif choice == '3':
        power = "Elemental Control"
    else:
        print("Invalid choice. Let's try again.")

    print(f"\nYour training has made you stronger in {power}")
    finalChallenge()

def finalChallenge():
    global morality
    print("\nThe ultimate test awaits. A powerful enemy threatens the entire world.")
    print("Will you face them alone or rally others to your cause?")
    actions = ["alone", "rally"]
    userInput = ""
    while userInput not in actions:
        print("Options: alone/rally")
        userInput = input().lower()
        if userInput == "alone":
            print("You face the enemy alone and triumph, but at great personal cost.")
            morality += 20
            break
        elif userInput == "rally":
            print("You gather allies and defeat the enemy together, becoming a symbol of unity.")
            morality += 30
            break
        else:
            print("Please choose a valid option.")
    
    checkEnding()

def checkEnding():
    print("\nThe story concludes based on your decisions...")
    if morality >= 70:
        print("You are celebrated as a true hero, inspiring generations to come!")
    elif 40 <= morality < 70:
        print("You walk the line between hero and anti-hero, respected but feared.")
    else:
        print("You are seen as a villain, but you believe you did what was necessary.")
    print("Thanks for playing!")
    input("\nPress Enter to exit the game...")

def introScene():
    print("Welcome to The Superhero Origin game!")
    print("You’re an ordinary person until a life-changing eventgrants you superpowers. You must decide how to use yourpowers while balancing personal struggles, relationships,andmoral dilemmas.Will you become the world’s savior, or willyou walk a darker path?")
    print("Your journey begins now.....")
    print("\nOne day, something extraordinary happens....")
    print("1. A lab explosion grants you super strength.")
    print("2. A mysterious artifact gives you telekinesis.")
    print("3. A lightening strike gives you control of electricity.")
    choice=input("choose your origin (1, 2 or 3): ")
    if choice == '1':
        print("The lab accident granted you incredible strength and speed!")
    elif choice == '2':
        print("The artifact gave you control over telekinetic powers!")
    elif choice == '3':
        print("The lightning storm granted you the ability to control electricity!")
    else:
        print("Invalid choice. Let's try that again.")
        introScene()
        return
    
    encounterVillain()
def characterCreation():
    print("\nLet's create your superhero!")
    name=input("Enter your hero's name: ")
    print(f"\nWelcome, {name}!")
    print("You will soon discover your powers...")
    print("CheemTabakaTamTam")
    introScene()
if __name__ == "__main__":
    try:
        print("Welcome to The Superhero Origin Adventure Game! ")
        characterCreation()
    except Exception as e:
        print(f"An error occured: {e}")
        input("Press Enter to exit...")
