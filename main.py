workers = {
    'Porko':{

        'Посада':'Porko - Уборщик',
        'Коефіцієнт ефективності': 'Porko - 90' ,
        'Останні роботи': ["PORKO " ,'Убощик в супермаркеті' , 'На базарі', 'Моряком']
    },

    'Zark':{

        'Посада':'Zark - продавець',
        'Коефіцієнт ефективності':'Zark - 76',
        'Останні роботи':[ 'ZARK ',"Перша робота"]
    },

    'Hovech':{

        'Посада':'Hovech - менеджер',
        'Коефіцієнт ефективності': 'Hovech - 94' ,
        'Останні роботи': ['HOVECH ','Убощик'  , "На підробітці стройки" , 'Касиром']
    }
}
flag = True
while flag:

    while flag:

        wop = input('''Виберіть варіант дії: 
        1 - Призвіща всіх співробітників. 
        2 - Ефективність робітників. 
        3 - Посади усіх співробітників 
        4 - Останні роботи працівника
        5 - Вихід з программи''')

        if wop == '1' or wop == 1:
            zna = 1
            break
        elif wop == '2' or wop == 2:
            zna = 2
            break
        elif wop == '3' or wop == 3:
            zna = 3
            break
        elif wop == '4' or wop == 4:
            zna = 4
            break
        elif wop == '5' or wop == 5:
            zna = 5
            break
        else:
            print('ПОМИЛКА ВЕДІТЬ ВАРІАНТ ЧИСЛА')
    
    
    while flag: 
        if zna == 1:
            print('Призвіща робітників:' , workers.keys())
            break
        elif zna == 2:
            for i in workers:
                print(workers[i]['Коефіцієнт ефективності'])
                
            break        
         
        elif zna == 3:
            print('Роботи працівників:')
        
            for i in workers:
                print( workers[i]['Посада'])
            break    
        elif zna == 4:
            for i in workers:
                print( workers[i]['Останні роботи'])        
            break

        elif zna == 5:
            flag = False
            
















