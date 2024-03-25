recipes = []

with open('recipes.txt', 'rt', encoding='utf8') as f:
    for text in f:
        dish_name = text.strip()
        dish = {'name': dish_name, 'ingredients': []}
        ingredients_count = f.readline()
        for ing in range(int(ingredients_count)):
            ingredients = f.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
        line = f.readline()
        recipes.append(dish)

def get_shop_list_by_dishes(list_dish, people):
    purchases = {}
    for dish in list_dish:
        for dish_book in recipes:
            if dish_book['name'] == dish:
                for ing in dish_book['ingredients']:
                    if ing['name'] not in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
                    
                    elif ing['name'] in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity']) + int((purchases[ing['name']])['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
    return purchases

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)