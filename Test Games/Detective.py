import pygame
import sys
import random

# Initialize Pygame core modules
pygame.init()
pygame.font.init()

# --- WINDOW CONFIGURATION ---
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚨 390 Belmont Avenue - Forensic Investigation Layout")
clock = pygame.time.Clock()

# --- DESIGN & COLOR PALETTE ---
COLOR_BG = (18, 22, 28)          # Dark Slate
COLOR_SIDEBAR = (28, 33, 41)     # Lighter gray for data HUD
COLOR_TEXT = (230, 235, 240)     # Clean white
COLOR_TEXT_DIM = (140, 150, 160) # Gray labels
COLOR_BORDER = (50, 60, 75)      # Normal walls

# Room specific colors matching your blueprint
COLOR_LR = (102, 0, 0)           # Dark red fill
COLOR_K = (51, 0, 51)            # Dark Purple
COLOR_MC = (103, 171, 159)       # Corridor Teal
COLOR_B1 = (0, 0, 51)            # Deep blue
COLOR_B2 = (0, 51, 51)           # Dark Teal
COLOR_T = (51, 51, 0)            # Dark Yellow/Olive
COLOR_BY = (0, 138, 0)           # Backyard Dark Green
COLOR_SHED = (96, 169, 23)       # Light Green

COLOR_ORANGE_ARROW = (180, 101, 4) # Lock path marker

# --- ENGINE FONTS ---
font_title = pygame.font.SysFont("Helvetica", 20, bold=True)
font_body = pygame.font.SysFont("Helvetica", 14)
font_hud = pygame.font.SysFont("Helvetica", 15, bold=True)

# --- 1. GAME DATA STATE ---
current_room = "LR"
inventory = set()
health = 100
blood_contamination = 0
TOTAL_EVIDENCE = 7
game_log = ["System Initialized. Step into a room to sweep for clues."]

# --- 2. COORDINATES MAP GENERATION (Sourced from Diagram File coordinates) ---
rooms = {
    "LR": {
        "name": "Living Room",
        "rect": pygame.Rect(480, 280, 120, 120),
        "color": COLOR_LR,
        "description": "Center room. Heavy rain pounces on glass paneling.",
        "connections": ["K", "MC", "T"],
        "has_searched": False,
        "trap_active": False,
        "item": "Evidence Piece #6: Broken Gold Watch",
        "hidden_key": "Kitchen Key"
    },
    "K": {
        "name": "Kitchen",
        "rect": pygame.Rect(480, 160, 120, 120),
        "color": COLOR_K,
        "description": "Overturned units. Heavy trace blood markers found near sink.",
        "connections": ["LR", "MC", "BY"],
        "requires": {"MC": "Corridor Keycard", "BY": "Backyard Key"},
        "has_searched": False,
        "trap_active": True,
        "trap_desc": "⚠️ CORROSIVE GAS LINE behind oven drawer handle!",
        "item": "Backyard Key"
    },
    "MC": {
        "name": "Main Corridor",
        "rect": pygame.Rect(240, 160, 220, 20), 
        "color": COLOR_MC,
        "description": "Long hallway connecting deep residential bedroom wings.",
        "connections": ["LR", "K", "B1", "B2"],
        "requires": {"K": "Kitchen Key", "B1": "Bedroom 1 Key", "B2": "Bedroom 2 Key"},
        "has_searched": False,
        "trap_active": False,
        "item": "Corridor Keycard"
    },
    "B1": {
        "name": "Bedroom 1",
        "rect": pygame.Rect(240, 180, 120, 120),
        "color": COLOR_B1,
        "description": "Shattered window layout. Footprints cover carpet fibers.",
        "connections": ["MC"],
        "has_searched": False,
        "trap_active": True,
        "trap_desc": "⚠️ RAZOR WIRE SPRING SNARE hidden under loose drapes!",
        "item": "Evidence Piece #2: Shattered Glass Fibres"
    },
    "B2": {
        "name": "Bedroom 2",
        "rect": pygame.Rect(360, 180, 120, 120),
        "color": COLOR_B2,
        "description": "Ransacked storage compartments. Shredded paper litter.",
        "connections": ["MC"],
        "has_searched": False,
        "trap_active": False,
        "item": "Evidence Piece #3: Threatening Letter"
    },
    "T": {
        "name": "Toilet",
        "rect": pygame.Rect(400, 300, 80, 80),
        "color": COLOR_T,
        "description": "Cramped corner unit. Bleach trace smells overlaying air.",
        "connections": ["LR"],
        "has_searched": False,
        "trap_active": True,
        "trap_desc": "⚠️ PRESSURE NEEDLE RIG built into lock latch cabinet!",
        "item": "Bedroom 1 Key",
        "hidden_key": "Evidence Piece #7: Torn Silk Fabric"
    },
    "BY": {
        "name": "Backyard",
        "rect": pygame.Rect(240, -10, 360, 170), 
        "color": COLOR_BY,
        "description": "Muddy outdoor segment showing distinct track patterns.",
        "connections": ["K", "SHED"],
        "requires": {"SHED": "Shed Key"},
        "has_searched": False,
        "trap_active": False,
        "item": "Evidence Piece #4: Fence wire denim strands"
    },
    "SHED": {
        "name": "Shed",
        "rect": pygame.Rect(450, -90, 150, 80),
        "color": COLOR_SHED,
        "description": "Cold storage cell. Dense weapon fragments present.",
        "connections": ["BY"],
        "has_searched": False,
        "trap_active": True,
        "trap_desc": "⚠️ COLLAPSING CEILING spiked deadfall above entrance rim!",
        "item": "Evidence Piece #5: Discarded Iron Tool"
    }
}

def push_log(message):
    global game_log
    game_log.append(message)
    if len(game_log) > 12:
        game_log.pop(0)

# --- ENGINE MAIN UTILITY LOOPS ---
running = True
won = False

while running:
    map_offset_x = 40
    map_offset_y = 200
    
    evidence_count = sum(1 for item in inventory if "Evidence" in item)
    
    if health <= 0:
        screen.fill((20, 5, 5))
        loss_text = font_title.render("🚨 DETECTIVE COLLAPSED: CRITICAL TRAP DAMAGE Sustained", True, (255, 50, 50))
        sub_text = font_body.render("Press ESCAPE to abandon operations and exit.", True, COLOR_TEXT)
        screen.blit(loss_text, (WIDTH // 2 - 250, HEIGHT // 2 - 20))
        screen.blit(sub_text, (WIDTH // 2 - 130, HEIGHT // 2 + 10))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and not won:
            mouse_pos = pygame.mouse.get_pos()
            
            # Map Room Clicks Logic
            for room_id, r_data in rooms.items():
                adjusted_rect = r_data["rect"].copy()
                adjusted_rect.x += map_offset_x
                adjusted_rect.y += map_offset_y
                
                if adjusted_rect.collidepoint(mouse_pos):
                    if room_id == current_room:
                        push_log("You are already standing in this section.")
                    elif room_id in rooms[current_room]["connections"]:
                        
                        # Leaving standard check
                        if "requires" in rooms[current_room] and room_id in rooms[current_room]["requires"]:
                            key_need = rooms[current_room]["requires"][room_id]
                            if key_need not in inventory:
                                push_log(f"⛔ LOCKED PATH: Key required: {key_need}")
                                break
                        
                        # Entering standard check
                        if "requires" in r_data and current_room in r_data["requires"]:
                            key_need = r_data["requires"][current_room]
                            if key_need not in inventory:
                                push_log(f"⛔ ACCESS DENIED: Requires: {key_need}")
                                break

                        # Trigger blind active booby trap state mechanics
                        if r_data["trap_active"]:
                            dmg = random.randint(35, 45)
                            health -= dmg
                            blood_contamination = min(100, blood_contamination + 25)
                            push_log(f"💥 TRAP DETONATED inside {r_data['name']}!")
                            push_log(f"Received -{dmg} HP damage.")
                            r_data["trap_active"] = False 
                            
                        current_room = room_id
                        blood_contamination = min(100, blood_contamination + random.randint(3, 7))
                        push_log(f"Moved successfully into: {r_data['name']}")
                        
                        if current_room == "LR" and evidence_count == TOTAL_EVIDENCE:
                            won = True
                    else:
                        push_log("❌ This section does not link cleanly over current walls.")
                    break
            
            # Search Button Logic
            btn_search = pygame.Rect(20, HEIGHT - 70, 160, 40)
            if btn_search.collidepoint(mouse_pos):
                r_now = rooms[current_room]
                if not r_now["has_searched"]:
                    r_now["has_searched"] = True
                    
                    if r_now["trap_active"]:
                        push_log("⚡ Scanner Alerted! Trap localized and defused safely.")
                        r_now["trap_active"] = False
                    
                    if r_now["item"]:
                        inventory.add(r_now["item"])
                        push_log(f"💼 Found clue: {r_now['item']}")
                    if "hidden_key" in r_now:
                        inventory.add(r_now["hidden_key"])
                        push_log(f"🔑 Obtained utility: {r_now['hidden_key']}")
                        
                    if current_room == "K":
                        inventory.add("Bedroom 2 Key")
                        push_log("🔑 Obtained utility: Bedroom 2 Key from container.")
                    elif current_room == "SHED":
                        inventory.add("Evidence Piece #1: Bloody Footprint")
                        push_log("💼 Found clue: Evidence Piece #1: Bloody Footprint")
                else:
                    