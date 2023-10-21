def shop_from_grocery_list(budget, grocery_list, *args):
    my_list = []
    money_spent = 0
    final_result = ''

    for product, price in args:
        if product in grocery_list and product not in my_list:
            if price > budget:
                break

            else:
                my_list.append(product)
                grocery_list.remove(product)
                money_spent += price
                budget -= price

    if len(grocery_list) == 0:
        final_result += f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        final_result += f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    return final_result
