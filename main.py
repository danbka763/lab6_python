#
class PRICE:
    def __init__(self, product, shop, price):
        self.product = product
        self.shop = shop
        self.price = price
    def __str__(self):
        return f'|{self.product}|{self.shop}|{self.price}|'
    def __del__(self):
        print('Товар был удален.')

#
def sorting(obj):
    return obj.product

def check_int(string: str) -> int:
    while True:
        try:
            return int(string)
        except ValueError:
            print('Это не число.')
            string = input('>>> ')

def delete_product(List, del_obj: str):
    for obj in List:
        if obj.product == del_obj:
            try:
                List.pop(List.index(obj))
                print('Товар был удалён.')
                return
            except ValueError:
                print('Товара не существует.')

def Menu():
    count = check_int(input('Количество товара: '))
    List = []
    
    for i in range(count):
        List.append( PRICE(input('Товар: '), input('Магазин: '), check_int(input('Стоимость: '))) )
    
    while True:
        List.sort(key = sorting)
        
        if len(List) == 0:
            break
        print('1) Добавить\n2) Удалить\n3) Список\n4) Выход')
        cmd = input('>>> ')
        
        if cmd == '1':
            List.append( PRICE(input('Товар: '), input('Магазин: '), check_int(input('Стоимость: '))) )
        elif cmd == '2':
            delete_product(List, input('>>> '))
        elif cmd == '3':
            for obj in List:
                print(obj)
        elif cmd == '4':
            exit()
        else:
            print('Некорректный ввод.')

#
def main():
    Menu()
#
if __name__ == "__main__":
    main()
