from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    potion_msg: str = (f"Healing potion brewed with '{create_earth()}' "
                       f"and '{create_air()}'")
    return potion_msg


def strength_potion() -> str:
    potion_msg: str = (f"Strength potion brewed with '{create_fire()}' "
                       f"and '{create_water()}'")
    return potion_msg
