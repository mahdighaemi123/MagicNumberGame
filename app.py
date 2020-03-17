import random

all_numbers = [*range(1, 101)]
search_numbers = [*all_numbers]
not_numbers = []


def find_selected_numbers():
    global all_numbers, search_numbers, not_numbers

    if len(search_numbers) == 1:
        print()
        print('Do the magic :)')
        print(f"your number is {search_numbers[0]}")
        return

    search_numbers_select_count = len(search_numbers) // 2
    author_not_numbers_count = len(all_numbers) // 2 - search_numbers_select_count

    nums = random.sample(search_numbers, search_numbers_select_count)
    nums += random.sample(not_numbers, author_not_numbers_count)

    print()
    print(nums)
    find = input("Is the number selected above (Y/n) : ").upper() == "Y"

    if find:
        not_numbers += list(set(search_numbers) - set(nums))
    else:
        not_numbers += list(set(nums) - set(not_numbers))

    search_numbers = list(set(search_numbers) - set(not_numbers))
    find_selected_numbers()


print("Magic Number Game")
print("v1.0.0")
print()

print("Select Number Between 1 and 100")
print("Game start")
find_selected_numbers()
