from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_elements: list[str] = dark_spell_allowed_ingredients()
    for element in allowed_elements:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
