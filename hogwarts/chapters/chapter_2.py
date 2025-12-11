from hogwarts.universe.character import *
from hogwarts.utils.input_utils import *
import os

def meet_friends(character):
    """Handle the meetings with Ron, Hermione and Draco on the Hogwarts Express.

    Each choice modifies the character's attributes (Courage, Intelligence, Loyalty, Ambition).
    """

    attrs = character["Attributes"]  # shortcut

    print("You board the Hogwarts Express. The train slowly departs northward...")

    # --- Meeting Ron ---
    print("\nA red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    if choice == "1":
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        attrs["Loyalty"] += 1
    else:
        print("Ron looks a bit disappointed, but shrugs and leaves.")
        attrs["Ambition"] += 1

    # --- Meeting Hermione ---
    print("\nA girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    if choice == "1":
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        attrs["Intelligence"] += 1
    else:
        print("Hermione raises an eyebrow: — Well, I suppose there are different kinds of courage...")
        attrs["Courage"] += 1

    # --- Meeting Draco ---
    print("\nThen a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2", "3"]:
            break
        print("Please enter 1, 2 or 3.")

    if choice == "1":
        print("You shake Draco's hand politely. He smirks, satisfied.")
        attrs["Ambition"] += 1
    elif choice == "2":
        print("Draco frowns, annoyed. — You'll regret that!")
        attrs["Loyalty"] += 1
    else:
        print("You respond with confidence. Draco looks taken aback, then glares at you.")
        attrs["Courage"] += 1

    print("\nThe train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!")
    print(f"Your updated attributes: {attrs}")

def welcome_message():
    """Display a welcome message from Professor Dumbledore."""

    print("\n======================================================")
    print("Welcome to Hogwarts School of Witchcraft and Wizardry!")
    print("======================================================\n")

    print("Professor Dumbledore appears with a warm smile:")
    print("“Welcome, dear students, to Hogwarts. Here, you will discover magic,")
    print("forge friendships, and learn more about yourselves than you ever imagined.")
    print("But for now… let the Sorting Ceremony begin!”\n")

    input("Press Enter to continue... ")

def enter_common_room(character):
    """Place the player in their house common room and display its description."""

    house_name = character.get("House")

    if not house_name:
        print("Error: The character has no assigned house.")
        return

    # Load the house data
    # Adapt path if needed!
    house_data = load_file("data/houses.json")

    if house_data is None:
        print("Error: Could not load houses.json")
        return

    # Retrieve info for the player's house
    info = house_data.get(house_name)

    if info is None:
        print(f"Error: House '{house_name}' not found in houses.json")
        return

    emoji = info.get("emoji", "")
    description = info.get("description", "")
    welcome = info.get("welcome", "")
    colors = info.get("colors", [])

    print("\nYou follow the prefects through the castle corridors...")

    # Description
    print(f"{emoji} {description}")

    # Welcome message
    print(f"✨ {welcome}")

    # House colors
    print(f"Your house colors: {', '.join(colors)}\n")
