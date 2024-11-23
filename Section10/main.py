from enemy import Enemy, Troll, Vampire, VampireKing
from player import Player


def tim_player():
    tim: Player = Player("Tim")

    print(tim.name)
    print(tim.lives)
    tim.lives -= 1
    print(tim)

    tim.lives -= 1
    print(tim)

    tim.lives -= 1
    print(tim)

    tim.lives -= 1
    print(tim)

    tim.lives = 9
    print(tim)

    tim.level += 2
    print(tim)

    tim.level += 3
    print(tim)

    tim.level += -1
    print(tim)

    tim.level += -5
    print(tim)

    tim.score = 500
    print(tim)


def enemy_player():
    random_monster: Enemy = Enemy("Basic enemy", 12, 1)
    print(random_monster)
    random_monster.take_damage(4)
    print(random_monster)
    random_monster.take_damage(8)
    print(random_monster)
    random_monster.take_damage(9)
    print(random_monster)

    print("*" * 80)

    ugly_troll: Troll = Troll("Pug")
    print(f"Ugly troll - {ugly_troll}")

    another_troll: Troll = Troll("Ug")
    print(f"Another troll - {another_troll}")

    brother: Troll = Troll("Urg")
    print(f"Brother - {brother}")

    ugly_troll.grunt()
    another_troll.grunt()
    brother.grunt()

    print("*" * 80)

    daddy = Vampire("Daddy")
    ehhh = Vampire("Ehhh")
    dead = Vampire("Dead")

    daddy.take_damage(1)
    ehhh.take_damage(2)
    dead.take_damage(3)

    print("*" * 80)

    while daddy.alive:
        daddy.take_damage(1)
        # print(daddy)

    print("*" * 80)

    mommy = VampireKing("Mommy")
    print(mommy)

    while mommy.alive:
        mommy.take_damage(40)  # Should take 10 damage


def main():
    # tim_player()
    enemy_player()


if __name__ == "__main__":
    main()
