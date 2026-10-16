def main():
    # Introduction text
    print("=================================================================")
    print("            METROPOLITAN POLICE - CRIME SCENE INVESTIGATION       ")
    print("=================================================================")
    print("You have been called to a vicious murder at 390 Belmont Avenue.")
    print("Your objective is to secure the property, overcome locked barriers,")
    print("and collect ALL pieces of evidence to complete the game.\n")
    
    # NEW: Clear Command Guide explaining what everything means
    print("-----------------------------------------------------------------")
    print("                      MAP LEGEND & COMMANDS                      ")
    print("-----------------------------------------------------------------")
    print(" LR   means   Living Room")
    print(" K    means   Kitchen")
    print(" MC   means   Main Corridor")
    print(" B1   means   Bedroom 1")
    print(" B2   means   Bedroom 2")
    print(" T    means   Toilet")
    print(" BY   means   Backyard")
    print(" SHED means   Shed")
    print("\n Action Commands:")
    print(" 'search'  means   Look for clues/evidence and keys in your current room.")
    print(" 'quit'    means   Exit the game.")
    print("=================================================================\n")

    # 1. Game State Tracking
    current_room = "LR"
    inventory = set()
    
    # Total evidence items required to finish the game
    TOTAL_EVIDENCE_NEEDED = 7 

    # 2. Diagram Map Configuration
    rooms = {
        "LR": {
            "name": "Living Room",
            "description": "The center of the house. A heavy silence fills the air.",
            "connections": {"K": "K", "MC": "MC", "T": "T"},
            "has_searched": False,
            "item": "Evidence Piece #6: Broken Watch",
            "hidden_key": "Kitchen Key"
        },
        "K": {
            "name": "Kitchen",
            "description": "Cabinets are thrown open. There are deep scratch marks on the counter.",
            "connections": {"LR": "LR", "MC": "MC", "BY": "BY"}, 
            "requires": {
                "MC": "Corridor Keycard",  # Orange Arrow to Main Corridor
                "BY": "Backyard Key"       # Orange Arrow to Backyard
            },  
            "has_searched": False,
            "item": "Backyard Key"
        },
        "MC": {
            "name": "Main Corridor",
            "description": "A long corridor running between the bedrooms.",
            "connections": {"LR": "LR", "K": "K", "B1": "B1", "B2": "B2"},
            "requires": {
                "K": "Kitchen Key",      # Orange Arrow to Kitchen
                "B1": "Bedroom 1 Key",   # Orange Arrow to Bedroom 1
                "B2": "Bedroom 2 Key"    # Orange Arrow to Bedroom 2
            },
            "has_searched": False,
            "item": "Corridor Keycard"   
        },
        "B1": {
            "name": "Bedroom 1",
            "description": "The primary bedroom. The window is completely shattered.",
            "connections": {"MC": "MC"},
            "has_searched": False,
            "item": "Evidence Piece #2: Shattered Glass Fibres"
        },
        "B2": {
            "name": "Bedroom 2",
            "description": "A small guest room. Documents are scattered everywhere.",
            "connections": {"MC": "MC"},
            "has_searched": False,
            "item": "Evidence Piece #3: Threatening Letter"
        },
        "T": {
            "name": "Toilet",
            "description": "A cramped bathroom. The air smells strongly of chemical cleaner.",
            "connections": {"LR": "LR"},
            "has_searched": False,
            "item": "Bedroom 1 Key",
            "hidden_key": "Evidence Piece #7: Torn Fabric"
        },
        "BY": {
            "name": "Backyard",
            "description": "A large, overgrown grassy backyard. The shed sits in the corner.",
            "connections": {"K": "K", "SHED": "SHED"},
            "requires": {"SHED": "Shed Key"}, # Orange Arrow to Shed
            "has_searched": False,
            "item": "Evidence Piece #4: Strands of Fabric on the Fence"
        },
        "SHED": {
            "name": "Shed",
            "description": "Dark and damp. Tools are violently scattered around.",
            "connections": {"BY": "BY"},
            "has_searched": False,
            "item": "Evidence Piece #5: Discarded Weapon"
        }
    }

    # 3. Core Engine Loop
    while True:
        room_data = rooms[current_room]

        print("-" * 60)
        print(f"LOCATION: {room_data['name']} ({current_room})")
        print(room_data["description"])
        
        # Display current inventory stats
        evidence_count = sum(1 for item in inventory if "Evidence" in item)
        print(f"Inventory: {list(inventory) if inventory else 'Empty'}")
        print(f"Evidence Collected: {evidence_count}/{TOTAL_EVIDENCE_NEEDED}")

        # Show exits
        exits = ", ".join(room_data["connections"].keys())
        print(f"Available Exits: {exits}")
        
        # Main Door Win Condition Check
        if current_room == "LR" and evidence_count == TOTAL_EVIDENCE_NEEDED:
            print("\n*** [MAIN DOOR] You have collected all pieces of evidence! ***")
            print("You walk out the Main Door and successfully submit your case file to Headquarters.")
            print("CONGRATULATIONS, DETECTIVE! YOU SOLVED THE CASE!")
            break

        # Get player action
        choice = input("\nWhat is your move? -> ").strip().lower()

        if choice == "quit":
            print("Leaving the crime scene. Investigation incomplete.")
            break

        # Handle Searching the Current Room
        if choice == "search":
            if not room_data["has_searched"]:
                room_data["has_searched"] = True
                found_something = False
                
                # Check for standard items
                if room_data["item"]:
                    item = room_data["item"]
                    inventory.add(item)
                    print(f"\n[FOUND] You uncovered: {item}!")
                    found_something = True
                
                # Check for auxiliary hidden keys
                if "hidden_key" in room_data:
                    key = room_data["hidden_key"]
                    inventory.add(key)
                    print(f"[FOUND] You also found a: {key}!")
                    found_something = True
                    
                # Dynamically give progression keys when searching
                if current_room == "K":
                    inventory.add("Bedroom 2 Key")
                    print("[FOUND] Inside the kitchen drawer, you also find a: Bedroom 2 Key!")
                elif current_room == "SHED":
                    # Injecting a final core piece of evidence mapping back to the diagram
                    inventory.add("Evidence Piece #1: Bloody Footprint")
                    print("[FOUND] Behind the toolrack, you discover: Evidence Piece #1: Bloody Footprint!")
                    
                if not found_something:
                    print("\nYou searched thoroughly but found nothing new.")
            else:
                print("\nYou have already swept this room for clues.")
            continue

        # Handle Navigation
        room_cmd = choice.upper()
        if room_cmd in room_data["connections"]:
            destination = room_data["connections"][room_cmd]
            
            # Orange Arrow Item Gate Checks (Leaving a room)
            if "requires" in room_data and destination in room_data["requires"]:
                needed_item = room_data["requires"][destination]
                if needed_item not in inventory:
                    print(f"\n[LOCKED ⛔] This orange path requires an item! You need: {needed_item}")
                    continue
            
            # Destination side gate check (Entering a room that requires a key)
            target_room = rooms[destination]
            if "requires" in target_room and current_room in target_room["requires"]:
                needed_item = target_room["requires"][current_room]
                if needed_item not in inventory:
                    print(f"\n[LOCKED ⛔] Access Denied! This orange path requires: {needed_item}")
                    continue

            # Update location
            current_room = destination
        else:
            print("\n[INVALID] Invalid command. Use room codes like LR, K, MC, or type 'search'.")

if __name__ == "__main__":
    main()