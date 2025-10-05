import random
def roll_dice():
    dice_roll = random.randint(1, 6)
    print(f"Выпало число: {dice_roll}")

    if dice_roll in [5, 6]:
        print("Вы победили!")
    elif dice_roll in [3, 4]:
        roll_dice()
    else:
        print("Вы проиграли.")
if __name__ == "__main__":
    roll_dice()