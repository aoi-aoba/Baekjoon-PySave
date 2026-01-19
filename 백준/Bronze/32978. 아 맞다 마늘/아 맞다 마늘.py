n = int(input())
pasta_ingredients = set(input().split())

for ingredient in input().split():
    pasta_ingredients.remove(ingredient)

print(pasta_ingredients.pop())