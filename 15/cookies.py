import pprint


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return 'Name: ' + str(self.name) + ' Capacity: ' + str(self.capacity) + ' Durability: ' + str(self.durability) + ' Flavor: ' + str(self.flavor) + ' Texture: ' + str(self.texture) + ' Calories: ' + str(self.calories)

    def __repr__(self):
        return 'Name: ' + str(self.name) + ' Capacity: ' + str(self.capacity) + ' Durability: ' + str(self.durability) + ' Flavor: ' + str(self.flavor) + ' Texture: ' + str(self.texture) + ' Calories: ' + str(self.calories)


class Cookie:
    def __init__(self, capacity=0, durability=0, flavor=0, texture=0, calories=0):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def add_ingredient(self, ingredient, quantity):
        self.capacity += ingredient.capacity * quantity
        self.durability += ingredient.durability * quantity
        self.flavor += ingredient.flavor * quantity
        self.texture += ingredient.texture * quantity
        self.calories += ingredient.calories * quantity

    def score_cookie(self):
        # Part 2 adds in the calories check
        return (self.capacity if self.capacity > 0 else 0) * (self.durability if self.durability > 0 else 0) * (self.flavor if self.flavor > 0 else 0) * (self.texture if self.texture > 0 else 0) if self.calories == 500 else 0


list_of_ingredients = []

with open('input.txt') as file:
    for line in file:
        line = line.replace(':', '').replace(',', '').strip().split(' ')
        ing = Ingredient(line[0], int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10]))
        list_of_ingredients.append(ing)

best_cookie = Cookie()

for i in range(0, 100):
    for j in range(0, 100):
        for k in range(0, 100):
            h = 100 - i - j - k
            tmp_cookie = Cookie()
            tmp_cookie.add_ingredient(list_of_ingredients[0], i)
            tmp_cookie.add_ingredient(list_of_ingredients[1], j)
            tmp_cookie.add_ingredient(list_of_ingredients[2], k)
            tmp_cookie.add_ingredient(list_of_ingredients[3], h)
            if tmp_cookie.score_cookie() > best_cookie.score_cookie():
                best_cookie = Cookie()
                best_cookie.add_ingredient(list_of_ingredients[0], i)
                best_cookie.add_ingredient(list_of_ingredients[1], j)
                best_cookie.add_ingredient(list_of_ingredients[2], k)
                best_cookie.add_ingredient(list_of_ingredients[3], h)
                print(i, j, k, h)


print(best_cookie.score_cookie())
print(list_of_ingredients)

