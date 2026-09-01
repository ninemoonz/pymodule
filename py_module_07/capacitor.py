from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing_creautre_test(healing_creature: HealingCreatureFactory) -> None:
    sprout = healing_creature.create_base()
    bloom = healing_creature.create_evolved()
    print("base:")
    print(sprout.describe())
    print(sprout.attack())
    print(sprout.heal())
    print("evolved:")
    print(bloom.describe())
    print(bloom.attack())
    print(bloom.heal())


def transform_creature_test(transform_creature:
                            TransformCreatureFactory) -> None:
    shift = transform_creature.create_base()
    morph = transform_creature.create_evolved()
    print("base:")
    print(shift.describe())
    print(shift.attack())
    print(shift.transform())
    print(shift.attack())
    print(shift.revert())
    print("evolved:")
    print(morph.describe())
    print(morph.attack())
    print(morph.transform())
    print(morph.attack())
    print(morph.revert())


if __name__ == "__main__":
    print("[Testing Creature with healing capability]")
    healing_creautre_test(HealingCreatureFactory())
    print()
    print("[Testing Creature with transform capability]")
    transform_creature_test(TransformCreatureFactory())
