from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed_elements: list[str] = (
        light_spellbook.light_spell_allowed_ingredients()
        )
    for element in allowed_elements:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
