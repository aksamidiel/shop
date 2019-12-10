from reference.models import *
from escooters.models import *


# функции, которые создают объекты каталогов
def create_manufacturer(name, c):
    obj = Manufacturer(name=name, country=c)
    obj.save()
    print('В каталоге "Компании_производители" был создан объект {} с ключом={}'.format(obj.name, obj.pk))


def create_serie(n, d):
    obj = Series(name=n, description=d)
    obj.save()
    print('В каталоге "Серии" был создан объект {} с ключом={}'.format(obj.name, obj.pk))


# удаляет определенный объект
def delete_object(r_name, p_key):
    r_name.objects.get(pk=p_key).delete()
    print('Из каталога {} был удален объект с ключом={}'.format(r_name, p_key))


# считает количество объектов в таблице
def count_on_count(table_name):
    x = table_name.objects.count()
    print("Количество объектов в таблице {} - {}".format(table_name, x))


# создает объект или обновляет, если уже объект создан
def update_create(name, cntr):
    obj, created = Manufacturer.objects.update_or_create(
        first_name=name,
        defaults={'country': cntr}
    )


# выводит все самокаты, связанные с полем в каталоге
def list_of(ref_name, pr_key):
    obj = ref_name.objects.get(pk=pr_key)
    for i in obj.escooter.all():
        print(i)


# создает самокат из каталога
def create_escooter(bk):
    obj = EScooter(name=bk['name'], price=bk['price'], year=bk['year'], identityNum=bk['identityNum'],
                   weight=bk['weight'], description=bk['description'],
                   escooter_amount=bk['amount'], available=bk['available'])
    obj.serie = Series.objects.get(name=bk['serie_name'])
    obj.save()
    manuf = Manufacturer.objects.get(pk=bk['manufacturer_name'])
    obj.manufacturer.add(manuf)


# пример который можно забросить в функцию create_escooter
new_book = {'name': 'новый_самокат', 'price': 1000, 'year': 2017, 'identityNum': '8475158945248', 'weight': 8000,
            'amount': 20, 'available': True, 'serie_name': 'Город',
            'manufacturer_name': 'Xiaomi'}
