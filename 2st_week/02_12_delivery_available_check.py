shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# def is_available_to_order(menus, orders):
#     menus.sort()
#     orders.sort()
#     check = True
#     for order in orders:
#         for menu in menus:
#             if order == menu:
#                 break
#         else:
#             check = False
#     if check:
#         return True
#     else:
#         return False


# def is_available_to_order(menus, orders):
#     menus.sort()
#     for order in orders:
#         if is_existing_target_menu(menus, order):
#             return True
#     return False
#
#
# def is_existing_target_menu(menus, order):
#     start_index = 0
#     end_index = len(menus) - 1
#     while start_index <= end_index:
#         cur_index = (start_index + end_index) // 2
#         if menus[cur_index] == order:
#             return True
#         elif menus[cur_index] < order:
#             start_index = cur_index + 1
#         else:
#             end_index = cur_index - 1
#     return False

def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
