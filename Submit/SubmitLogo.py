import pyfiglet 

#Morphun Logo

def print_logo():
  
  print("-----------------COOL MORPHUN LOGO------------------")  
  print("     ______  _______               ")  
  print("    |      \/       \              ")  
  print("   /          /\     \             ") 
  print("  /     /\   / /\     |            ")
  print(" /     /\ \_/ / /    /|            ")
  print("|     |  \|_|/ /    / |            ")
  print("|     |       |    |  |            ")
  print("|\____\       |____|  /0RPHUN      ")
  print("| |    |      |    | /             ")
  print(" \|____|      |____|               ")

  logo1 = pyfiglet.figlet_format("Morphun", font = "starwars"  )
  logo2 = pyfiglet.figlet_format("Morphun", font = "starwars"  )
  logo = pyfiglet.figlet_format("Morphun", font = "poison"  ) 
  print(logo)
  print(logo1)
  print(logo2)
