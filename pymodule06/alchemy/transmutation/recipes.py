from alchemy.elements import create_air
from alchemy.potions import strength_potion
import elements

def lead_to_gold() -> str:
	return f"Recipe transmuting Lead to Gold: '{create_air()}' and '{strength_potion()}' mixed with '{elements.create_fire()}'"