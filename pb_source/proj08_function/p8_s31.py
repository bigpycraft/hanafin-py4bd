def orderMenu(menu):
    print('손님, %s를 주문하였습니다' % (menu))

orderMenu('카페모카')
# TypeError
# orderMenu()

# Default Argument
def orderCoffee(menu='카페라떼'):
    print('손님, %s를 주문하였습니다.' % (menu))

orderCoffee()



