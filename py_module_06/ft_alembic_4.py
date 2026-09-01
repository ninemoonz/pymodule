import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that no all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: "
      f"{alchemy.create_earth()}")
