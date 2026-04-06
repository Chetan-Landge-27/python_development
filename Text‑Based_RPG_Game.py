import random
import os

player = {"health": 100, "gold": 0, "inventory": []}

def clear_screen():
    """Clear the terminal screen for better UX"""
    os.system('cls' if os.name == 'nt' else 'clear')

def game_over():
    """Handle game over condition"""
    print("\n💀 GAME OVER!")
    print("Better luck next time!")
    show_stats()
    return False

def victory():
    """Handle victory condition"""
    print("\n🏆 VICTORY! You've conquered the land!")
    show_stats()
    return False

def show_stats():
    """Display player stats"""
    print("\n📊 Player Stats:")
    print(f"❤️ Health: {player['health']}")
    print(f"💰 Gold: {player['gold']}")
    print(f"🎒 Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    print()

def use_item():
    """Allow player to use items from inventory"""
    if not player["inventory"]:
        print("📦 No items in inventory!")
        return True
    
    print("📦 Your inventory:", ", ".join(player["inventory"]))
    item = input("Use item (or 'none'): ").strip().lower()
    
    if item == "healing potion" and "Healing Potion" in player["inventory"]:
        player["health"] = min(100, player["health"] + 50)
        player["inventory"].remove("Healing Potion")
        print("💊 Health restored!")
    elif item == "magic sword" and "Magic Sword" in player["inventory"]:
        print("⚔️ Magic Sword equipped! (Boosts combat)")
    elif item == "none":
        pass
    else:
        print("❌ Invalid item!")
    
    return True

def start_game():
    clear_screen()
    print("🎮 Welcome to the Text-Based RPG!")
    print("You wake up in a mysterious land with many dangers and treasures...")
    print("Type 'stats' to check your status, 'use' to use items, 'quit' to exit.")
    return True

def explore_forest():
    print("\n🌲 You enter the dark forest and encounter a wild wolf!")
    print("🐺 Wolf Health: 50 | Your Health:", player["health"])
    
    action = input("Fight, run, hide, stats, use, or quit? ").strip().lower()
    
    if action in ["stats", "use"]:
        if action == "stats":
            show_stats()
        else:
            use_item()
        return True
    
    if action == "quit":
        return False
    
    if action == "fight":
        # Better combat with inventory bonus
        player_attack = random.randint(20, 40)
        if "Magic Sword" in player["inventory"]:
            player_attack += 20
            print("⚔️ Magic Sword boosts your attack!")
        
        if player_attack > 30:  # Better chance with sword
            print("✅ You defeat the wolf! Found treasure!")
            player["gold"] += 50
            if random.choice([True, False]):
                player["inventory"].append("Healing Potion")
        else:
            damage = random.randint(20, 40)
            print(f"💀 Wolf attacks! You lose {damage} health.")
            player["health"] -= damage
    
    elif action == "run":
        if random.choice([True, True, False]):  # 66% success
            print("🏃 You escape safely!")
        else:
            print("💀 You trip while running! Lose 10 health.")
            player["health"] -= 10
    
    elif action == "hide":
        print("👀 You hide successfully and find healing herbs!")
        player["health"] = min(100, player["health"] + 20)
    
    else:
        print("😵 You hesitate... wolf attacks! Lose 20 health.")
        player["health"] -= 20
    
    return True

def explore_castle():
    print("\n🏰 A massive castle looms before you. A guard blocks the entrance.")
    
    action = input("Talk, attack, bribe, stats, use, or quit? ").strip().lower()
    
    if action in ["stats", "use"]:
        if action == "stats":
            show_stats()
        else:
            use_item()
        return True
    
    if action == "quit":
        return False
    
    if action == "talk":
        print("🗣️ Your silver tongue works! Guard lets you in.")
        player["gold"] += 100
    
    elif action == "attack":
        if random.choice([True, False]) or "Magic Sword" in player["inventory"]:
            print("⚔️ You defeat the guard! Found Magic Sword!")
            if "Magic Sword" not in player["inventory"]:
                player["inventory"].append("Magic Sword")
        else:
            damage = random.randint(30, 60)
            print(f"💀 Guard counterattacks! Lose {damage} health.")
            player["health"] -= damage
    
    elif action == "bribe":
        if player["gold"] >= 20:
            player["gold"] -= 20
            print("💰 Bribe successful! You enter the castle.")
            player["gold"] += 80  # Net gain
        else:
            print("💸 Not enough gold!")
    
    else:
        print("🚫 Guard throws you out!")
    
    return True

def explore_village():
    print("\n🏡 A peaceful village marketplace bustles with activity.")
    
    action = input("Market, healer, tavern, stats, use, or quit? ").strip().lower()
    
    if action in ["stats", "use"]:
        if action == "stats":
            show_stats()
        else:
            use_item()
        return True
    
    if action == "quit":
        return False
    
    if action == "market":
        if player["gold"] >= 30:
            player["gold"] -= 30
            player["inventory"].append("Healing Potion")
            print("🛒 Bought Healing Potion!")
        else:
            print("💸 Not enough gold!")
    
    elif action == "healer":
        cost = 25 if player["health"] < 100 else 0
        if player["gold"] >= cost:
            player["gold"] -= cost
            player["health"] = 100
            print("💊 Fully healed!")
        else:
            print("💸 Not enough gold for healing!")
    
    elif action == "tavern":
        print("🍺 You hear rumors of treasure in the forest...")
        if random.choice([True, False]):
            player["gold"] += 10
            print("💰 Lucky gambler wins 10 gold!")
    
    else:
        print("🏚️ You wander aimlessly...")
    
    return True

def main_game_loop():
    if not start_game():
        return
    
    while True:
        show_stats()
        
        if player["health"] <= 0:
            return game_over()
        
        if player["gold"] >= 200 and "Magic Sword" in player["inventory"]:
            return victory()
        
        choice = input("\n🌍 Explore: Forest, Castle, Village, or Quit? ").strip().lower()
        
        if choice == "quit":
            print("\n👋 Thanks for playing!")
            break
        elif choice == "forest":
            if not explore_forest():
                break
        elif choice == "castle":
            if not explore_castle():
                break
        elif choice == "village":
            if not explore_village():
                break
        else:
            print("❓ Invalid choice. Try again!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_game_loop()