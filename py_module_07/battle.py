from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory_testing(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle_testing(factory_1: CreatureFactory,
                   factory_2: CreatureFactory) -> None:
    print("Testing battle")
    base_1 = factory_1.create_base()
    base_2 = factory_2.create_base()
    print(base_1.describe())
    print("vs.")
    print(base_2.describe())
    print("fight!")
    print(base_1.attack())
    print(base_2.attack())
    print()


if __name__ == "__main__":
    factory_testing(FlameFactory())
    factory_testing(AquaFactory())
    battle_testing(FlameFactory(), AquaFactory())
