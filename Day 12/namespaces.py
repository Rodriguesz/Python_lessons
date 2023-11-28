################### Scope ####################

enemies = 1 # Global variable

def increase_enemies():
  enemies = 2 # Local variable (can't be accessed outside the  function)
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drin_potion():
  potion_strengh = 2
  print(potion_strengh)