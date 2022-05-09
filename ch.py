# Определения
type_engine = 'Тип двигателя:'
engine_location = 'Расположение двигателя:'
fuel_brand = 'Марка топлива:'
number_of_cylinders = 'Количество цилиндров:'
cylinder_arrangement = 'Расположение цилиндров:'
engine_power_system = 'Система питания двигателя:'
boost_type = 'Тип наддува:'
engine_capacity = 'Объём двигателя:'
power = 'Мощность:'
km_h100 = 'Разгон до 100км/час:'
max_speed = 'Максимальная скорость:'
consumption_city = 'Расход в городском цикле:'
extra_urban_consumption = 'Расход в загородном цикле:'
combined_consumption = 'Расход в смешанном цикле:'
fuel_tank = 'Объем топливного бака:'
length = 'Длина:'
width = 'Ширина:'
height = 'Высота:'
wheelbase = 'Колёсная база:'
clearance = 'Клиренс:'
weight = 'Масса:'
trunk = 'Объём багажника:'
transmission = 'Трансмиссия:'
drive_unit = 'Привод:'
front_suspension = 'Передняя подвеска:'
rear_suspension = 'Задняя подвеска:'
front_brakes = 'Передние тормоза:'
rear_brakes = 'Задние тормоза:'
production = 'Производство:'
warranty = 'Гарантия:'

# Типы двигателей

petrol = 'Бензиновый'

# Расположение двигателей

transverse = 'Поперечное'

# Марки топлива

AI = 'АИ-95'

# Nissan Terrano
Nissan_Terrano = f'<b>Nissan Terrano</b>\n<b>{type_engine}</b> {petrol}\n' \
                 f'<b>{engine_location}</b> {transverse}\n' \
                 f'<b>{fuel_brand}</b> {AI}\n' \
                 f'<b>{number_of_cylinders}</b> 4\n' \
                 f'<b>{cylinder_arrangement}</b> Рядное\n' \
                 f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
                 f'<b>{boost_type}</b> -\n' \
                 f'<b>{engine_capacity}</b> 1598\n' \
                 f'<b>{power}</b> 114 л.с\n' \
                 f'<b>{km_h100}</b> 11.0 с\n' \
                 f'<b>{max_speed}</b> 163 км/ч\n' \
                 f'<b>{consumption_city}</b> 9.0/100км\n' \
                 f'<b>{extra_urban_consumption}</b> 6.0/100км\n' \
                 f'<b>{combined_consumption}</b> 7.0/100км\n' \
                 f'<b>{fuel_tank}</b> 50 л\n' \
                 f'<b>{length}</b> 4342 мм\n' \
                 f'<b>{width}</b> 1822 мм\n' \
                 f'<b>{height}</b> 1668 мм\n' \
                 f'<b>{wheelbase}</b> 2674 мм\n' \
                 f'<b>{clearance}</b> 205 мм\n' \
                 f'<b>{weight}</b> 1226 кг\n' \
                 f'<b>{trunk}</b> 475 л\n' \
                 f'<b>{transmission}</b> Механическая\n' \
                 f'<b>{drive_unit}</b> Передний\n' \
                 f'<b>{front_suspension}</b> Независимая - McPherson\n' \
                 f'<b>{rear_suspension}</b> Независимая - многорычажная\n' \
                 f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
                 f'<b>{rear_brakes}</b> Дисковые\n' \
                 f'<b>{production}</b> Москва\n' \
                 f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Nissan Qashqai
Nissan_Qashqai = f'<b>Nissan Qashqai</b>\n<b>{type_engine}</b> {petrol}\n' \
                 f'<b>{engine_location}</b> {transverse}\n' \
                 f'<b>{fuel_brand}</b> {AI}\n' \
                 f'<b>{number_of_cylinders}</b> 4\n' \
                 f'<b>{cylinder_arrangement}</b> Рядное\n' \
                 f'<b>{engine_power_system}</b> С непосредственным впрыском\n' \
                 f'<b>{boost_type}</b> Турбонаддув\n' \
                 f'<b>{engine_capacity}</b> 1197\n' \
                 f'<b>{power}</b> 115 л.с\n' \
                 f'<b>{km_h100}</b> 10.0 с\n' \
                 f'<b>{max_speed}</b> 185 км/ч\n' \
                 f'<b>{consumption_city}</b> 7.0/100км\n' \
                 f'<b>{extra_urban_consumption}</b> 5.0/100км\n' \
                 f'<b>{combined_consumption}</b> 6.0/100км\n' \
                 f'<b>{fuel_tank}</b> 60 л\n' \
                 f'<b>{length}</b> 4377 мм\n' \
                 f'<b>{width}</b> 1837 мм\n' \
                 f'<b>{height}</b> 1595 мм\n' \
                 f'<b>{wheelbase}</b> 2646 мм\n' \
                 f'<b>{clearance}</b> 200 мм\n' \
                 f'<b>{weight}</b> 1373 кг\n' \
                 f'<b>{trunk}</b> 430 л\n' \
                 f'<b>{transmission}</b> Механическая\n' \
                 f'<b>{drive_unit}</b> Передний\n' \
                 f'<b>{front_suspension}</b> Независимая - McPherson\n' \
                 f'<b>{rear_suspension}</b> Независимая - многорычажная\n' \
                 f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
                 f'<b>{rear_brakes}</b> Дисковые\n' \
                 f'<b>{production}</b> Санкт-Петербург\n' \
                 f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Nissan X-Trail
Nissan_XTrail = f'<b>Nissan X-Trail</b>\n<b>{type_engine}</b> {petrol}\n' \
                f'<b>{engine_location}</b> {transverse}\n' \
                f'<b>{fuel_brand}</b> {AI}\n' \
                f'<b>{number_of_cylinders}</b> 4\n' \
                f'<b>{cylinder_arrangement}</b> Рядное\n' \
                f'<b>{engine_power_system}</b> С непосредственным впрыском\n' \
                f'<b>{boost_type}</b> -\n' \
                f'<b>{engine_capacity}</b> 1997\n' \
                f'<b>{power}</b> 144 л.с\n' \
                f'<b>{km_h100}</b> 11.0 с\n' \
                f'<b>{max_speed}</b> 183 км/ч\n' \
                f'<b>{consumption_city}</b> 11.0/100км\n' \
                f'<b>{extra_urban_consumption}</b> 6.0/100км\n' \
                f'<b>{combined_consumption}</b> 8.0/100км\n' \
                f'<b>{fuel_tank}</b> 60 л\n' \
                f'<b>{length}</b> 4640 мм\n' \
                f'<b>{width}</b> 1820 мм\n' \
                f'<b>{height}</b> 1715 мм\n' \
                f'<b>{wheelbase}</b> 2705 мм\n' \
                f'<b>{clearance}</b> 210 мм\n' \
                f'<b>{weight}</b> 1675 кг\n' \
                f'<b>{trunk}</b> 497 л\n' \
                f'<b>{transmission}</b> Механическая\n' \
                f'<b>{drive_unit}</b> Передний\n' \
                f'<b>{front_suspension}</b> Независимая - McPherson\n' \
                f'<b>{rear_suspension}</b> Независимая - многорычажная\n' \
                f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
                f'<b>{rear_brakes}</b> Дисковые\n' \
                f'<b>{production}</b> Санкт-Петербург\n' \
                f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Nissan Murano
Nissan_Murano = f'<b>Nissan Murano</b>\n<b>{type_engine}</b> {petrol}\n' \
                f'<b>{engine_location}</b> {transverse}\n' \
                f'<b>{fuel_brand}</b> {AI}\n' \
                f'<b>{number_of_cylinders}</b> 6\n' \
                f'<b>{cylinder_arrangement}</b> V-образное\n' \
                f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
                f'<b>{boost_type}</b> -\n' \
                f'<b>{engine_capacity}</b> 3498\n' \
                f'<b>{power}</b> 249 л.с\n' \
                f'<b>{km_h100}</b> 7.0 с\n' \
                f'<b>{max_speed}</b> 210 км/ч\n' \
                f'<b>{consumption_city}</b> -\n' \
                f'<b>{extra_urban_consumption}</b> -\n' \
                f'<b>{combined_consumption}</b> 9.0/100км\n' \
                f'<b>{fuel_tank}</b> 72 л\n' \
                f'<b>{length}</b> 4898 мм\n' \
                f'<b>{width}</b> 1975 мм\n' \
                f'<b>{height}</b> 1691 мм\n' \
                f'<b>{wheelbase}</b> 2824 мм\n' \
                f'<b>{clearance}</b> 194 мм\n' \
                f'<b>{weight}</b> 1737 кг\n' \
                f'<b>{trunk}</b> 454 л\n' \
                f'<b>{transmission}</b> Вариатор\n' \
                f'<b>{drive_unit}</b> Передний\n' \
                f'<b>{front_suspension}</b> независимая, пружинная\n' \
                f'<b>{rear_suspension}</b> независимая, пружинная\n' \
                f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
                f'<b>{rear_brakes}</b> Дисковые\n' \
                f'<b>{production}</b> Санкт-Петербург\n' \
                f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Mazda 6 Седан
Mazda6_Sedan = f'<b>Mazda 6 Седан</b>\n<b>{type_engine}</b> {petrol}\n' \
               f'<b>{engine_location}</b> {transverse}\n' \
               f'<b>{fuel_brand}</b> {AI}\n' \
               f'<b>{number_of_cylinders}</b> 4\n' \
               f'<b>{cylinder_arrangement}</b> Рядное\n' \
               f'<b>{engine_power_system}</b> С непосредственным впрыском\n' \
               f'<b>{boost_type}</b> -\n' \
               f'<b>{engine_capacity}</b> 1998\n' \
               f'<b>{power}</b> 150 л.с\n' \
               f'<b>{km_h100}</b> 9.0 с\n' \
               f'<b>{max_speed}</b> 208 км/ч\n' \
               f'<b>{consumption_city}</b> 8.0/100км\n' \
               f'<b>{extra_urban_consumption}</b> 4.0/100км\n' \
               f'<b>{combined_consumption}</b> 6.0/100км\n' \
               f'<b>{fuel_tank}</b> 62 л\n' \
               f'<b>{length}</b> 4870 мм\n' \
               f'<b>{width}</b> 1840 мм\n' \
               f'<b>{height}</b> 1450 мм\n' \
               f'<b>{wheelbase}</b> 2830 мм\n' \
               f'<b>{clearance}</b> 165 мм\n' \
               f'<b>{weight}</b> 1340 кг\n' \
               f'<b>{trunk}</b> 483 л\n' \
               f'<b>{transmission}</b> Механическая\n' \
               f'<b>{drive_unit}</b> Передний\n' \
               f'<b>{front_suspension}</b> Независимая - McPherson\n' \
               f'<b>{rear_suspension}</b> Независимая - многорычажная\n' \
               f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
               f'<b>{rear_brakes}</b> Дисковые\n' \
               f'<b>{production}</b> Владивосток\n' \
               f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Mazda CX-9
Mazda9_CX = f'<b>Mazda CX-9</b>\n<b>{type_engine}</b> {petrol}\n' \
            f'<b>{engine_location}</b> {transverse}\n' \
            f'<b>{fuel_brand}</b> {AI}\n' \
            f'<b>{number_of_cylinders}</b> 4\n' \
            f'<b>{cylinder_arrangement}</b> Рядное\n' \
            f'<b>{engine_power_system}</b> С непосредственным впрыском\n' \
            f'<b>{boost_type}</b> Турбонаддув\n' \
            f'<b>{engine_capacity}</b> 2488\n' \
            f'<b>{power}</b> 231 л.с\n' \
            f'<b>{km_h100}</b> 8.0 с\n' \
            f'<b>{max_speed}</b> 210 км/ч\n' \
            f'<b>{consumption_city}</b> 12.0/100км\n' \
            f'<b>{extra_urban_consumption}</b> 7.0/100км\n' \
            f'<b>{combined_consumption}</b> 9.0/100км\n' \
            f'<b>{fuel_tank}</b> 74 л\n' \
            f'<b>{length}</b> 5075 мм\n' \
            f'<b>{width}</b> 1969 мм\n' \
            f'<b>{height}</b> 1747 мм\n' \
            f'<b>{wheelbase}</b> 2930 мм\n' \
            f'<b>{clearance}</b> 220 мм\n' \
            f'<b>{weight}</b> 2500 кг\n' \
            f'<b>{trunk}</b> 230 л\n' \
            f'<b>{transmission}</b> Автоматическая\n' \
            f'<b>{drive_unit}</b> Полный\n' \
            f'<b>{front_suspension}</b> Независимая, со стойками Мак-Ферсон\n' \
            f'<b>{rear_suspension}</b> Многорычажная\n' \
            f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
            f'<b>{rear_brakes}</b> Дисковые вентилируемые\n' \
            f'<b>{production}</b> Япония\n' \
            f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# Mazda CX-5
Mazda5_CX = f'<b>Mazda CX-5</b>\n<b>{type_engine}</b> {petrol}\n' \
            f'<b>{engine_location}</b> {transverse}\n' \
            f'<b>{fuel_brand}</b> {AI}\n' \
            f'<b>{number_of_cylinders}</b> 4\n' \
            f'<b>{cylinder_arrangement}</b> Рядное\n' \
            f'<b>{engine_power_system}</b> С непосредственным впрыском\n' \
            f'<b>{boost_type}</b> -\n' \
            f'<b>{engine_capacity}</b> 1998\n' \
            f'<b>{power}</b> 150 л.с\n' \
            f'<b>{km_h100}</b> 10.0 с\n' \
            f'<b>{max_speed}</b> 199 км/ч\n' \
            f'<b>{consumption_city}</b> 8.0/100км\n' \
            f'<b>{extra_urban_consumption}</b> 5.0/100км\n' \
            f'<b>{combined_consumption}</b> 6.0/100км\n' \
            f'<b>{fuel_tank}</b> 56 л\n' \
            f'<b>{length}</b> 4550 мм\n' \
            f'<b>{width}</b> 1840 мм\n' \
            f'<b>{height}</b> 1680 мм\n' \
            f'<b>{wheelbase}</b> 2700 мм\n' \
            f'<b>{clearance}</b> 192 мм\n' \
            f'<b>{weight}</b> 1451 кг\n' \
            f'<b>{trunk}</b> 442 л\n' \
            f'<b>{transmission}</b> Механическая\n' \
            f'<b>{drive_unit}</b> Передний\n' \
            f'<b>{front_suspension}</b> Независимая - McPherson\n' \
            f'<b>{rear_suspension}</b> Независимая - многорычажная\n' \
            f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
            f'<b>{rear_brakes}</b> Дисковые\n' \
            f'<b>{production}</b> Владивосток\n' \
            f'<b>{warranty}</b> 3 года или 100 000 км пробега\n'
# KIA Picanto
KIA_Picanto = f'<b>KIA Picanto</b>\n<b>{type_engine}</b> {petrol}\n' \
              f'<b>{engine_location}</b> {transverse}\n' \
              f'<b>{fuel_brand}</b> {AI}\n' \
              f'<b>{number_of_cylinders}</b> 3\n' \
              f'<b>{cylinder_arrangement}</b> Рядное\n' \
              f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
              f'<b>{boost_type}</b> -\n' \
              f'<b>{engine_capacity}</b> 998\n' \
              f'<b>{power}</b> 67 л.с\n' \
              f'<b>{km_h100}</b> 14.1 с\n' \
              f'<b>{max_speed}</b> 155 км/ч\n' \
              f'<b>{consumption_city}</b> 6.8/100км\n' \
              f'<b>{extra_urban_consumption}</b> 4.1/100км\n' \
              f'<b>{combined_consumption}</b> 5.1/100км\n' \
              f'<b>{fuel_tank}</b> 35 л\n' \
              f'<b>{length}</b> 3595 мм\n' \
              f'<b>{width}</b> 1595 мм\n' \
              f'<b>{height}</b> 1495 мм\n' \
              f'<b>{wheelbase}</b> 2400 мм\n' \
              f'<b>{clearance}</b> 161 мм\n' \
              f'<b>{weight}</b> -\n' \
              f'<b>{trunk}</b> 255 л\n' \
              f'<b>{transmission}</b> Механическая\n' \
              f'<b>{drive_unit}</b> Передний\n' \
              f'<b>{front_suspension}</b> Независимая, пружинная, типа McPherson\n' \
              f'<b>{rear_suspension}</b> Полузависимая, пружинная, с амортизаторами\n' \
              f'<b>{front_brakes}</b> Дисковые\n' \
              f'<b>{rear_brakes}</b> Барабанные\n' \
              f'<b>{production}</b> Южная Корея\n' \
              f'<b>{warranty}</b> 5 лет или 150000 км\n'
# KIA Rio
KIA_Rio = f'<b>KIA Rio</b>\n<b>{type_engine}</b> {petrol}\n' \
          f'<b>{engine_location}</b> {transverse}\n' \
          f'<b>{fuel_brand}</b> АИ - 92\n' \
          f'<b>{number_of_cylinders}</b> 4\n' \
          f'<b>{cylinder_arrangement}</b> Рядное\n' \
          f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
          f'<b>{boost_type}</b> -\n' \
          f'<b>{engine_capacity}</b> 1396\n' \
          f'<b>{power}</b> 100 л.с\n' \
          f'<b>{km_h100}</b> 12.0 с\n' \
          f'<b>{max_speed}</b> 185 км/ч\n' \
          f'<b>{consumption_city}</b> 7.0/100км\n' \
          f'<b>{extra_urban_consumption}</b> 4.0/100км\n' \
          f'<b>{combined_consumption}</b> 5.0/100км\n' \
          f'<b>{fuel_tank}</b> 50 л\n' \
          f'<b>{length}</b> 4400 мм\n' \
          f'<b>{width}</b> 1740 мм\n' \
          f'<b>{height}</b> 1470 мм\n' \
          f'<b>{wheelbase}</b> 2600 мм\n' \
          f'<b>{clearance}</b> 160 мм\n' \
          f'<b>{weight}</b> 1150 кг\n' \
          f'<b>{trunk}</b> 480 л\n' \
          f'<b>{transmission}</b> Механическая\n' \
          f'<b>{drive_unit}</b> Передний\n' \
          f'<b>{front_suspension}</b> Независимая - McPherson\n' \
          f'<b>{rear_suspension}</b> Полузависимая - торсионная балка\n' \
          f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
          f'<b>{rear_brakes}</b> Барабанные\n' \
          f'<b>{production}</b> Санкт-Петербург\n' \
          f'<b>{warranty}</b> 5 лет или 150000 км\n'
# KIA Cerato 2021
KIA_Cerato21 = f'<b>KIA Cerato 2021</b>\n<b>{type_engine}</b> {petrol}\n' \
               f'<b>{engine_location}</b> -\n' \
               f'<b>{fuel_brand}</b> АИ - 92, АИ - 95\n' \
               f'<b>{number_of_cylinders}</b> 4\n' \
               f'<b>{cylinder_arrangement}</b> -\n' \
               f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
               f'<b>{boost_type}</b> -\n' \
               f'<b>{engine_capacity}</b> 1999\n' \
               f'<b>{power}</b> 150 л.с\n' \
               f'<b>{km_h100}</b> 9.8 с\n' \
               f'<b>{max_speed}</b> 203 км/ч\n' \
               f'<b>{consumption_city}</b> 10.2/100км\n' \
               f'<b>{extra_urban_consumption}</b> 5.7/100км\n' \
               f'<b>{combined_consumption}</b> 7.4/100км\n' \
               f'<b>{fuel_tank}</b> 50 л\n' \
               f'<b>{length}</b> 4640 мм\n' \
               f'<b>{width}</b> 1800 мм\n' \
               f'<b>{height}</b> 1450 мм\n' \
               f'<b>{wheelbase}</b> 2700 мм\n' \
               f'<b>{clearance}</b> 150 мм\n' \
               f'<b>{weight}</b> 1330 кг\n' \
               f'<b>{trunk}</b> 502 л\n' \
               f'<b>{transmission}</b> Автоматическая\n' \
               f'<b>{drive_unit}</b> Передний\n' \
               f'<b>{front_suspension}</b> Независимая, типа Макферсон\n' \
               f'<b>{rear_suspension}</b> Полузависимая, пружинная, с телескопическими\nамортизаторами\n' \
               f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
               f'<b>{rear_brakes}</b> Дисковые\n' \
               f'<b>{production}</b> Корея\n' \
               f'<b>{warranty}</b> 5 лет или 150000 км\n'
# Kia Rio Х 2021
Kia_Rio_X21 = f'<b>Kia Rio Х 2021</b>\n<b>{type_engine}</b> {petrol}\n' \
              f'<b>{engine_location}</b> {transverse}\n' \
              f'<b>{fuel_brand}</b> АИ - 92\n' \
              f'<b>{number_of_cylinders}</b> 4\n' \
              f'<b>{cylinder_arrangement}</b> Рядное\n' \
              f'<b>{engine_power_system}</b> Распределенный впрыск\n' \
              f'<b>{boost_type}</b> -\n' \
              f'<b>{engine_capacity}</b> 1368\n' \
              f'<b>{power}</b> 100 л.с\n' \
              f'<b>{km_h100}</b> 13.0 с\n' \
              f'<b>{max_speed}</b> 173 км/ч\n' \
              f'<b>{consumption_city}</b> -\n' \
              f'<b>{extra_urban_consumption}</b> -\n' \
              f'<b>{combined_consumption}</b> 6.0/100км\n' \
              f'<b>{fuel_tank}</b> 50 л\n' \
              f'<b>{length}</b> 4275 мм\n' \
              f'<b>{width}</b> 1750 мм\n' \
              f'<b>{height}</b> 1535 мм\n' \
              f'<b>{wheelbase}</b> 2600 мм\n' \
              f'<b>{clearance}</b> 190 мм\n' \
              f'<b>{weight}</b> 1610 кг\n' \
              f'<b>{trunk}</b> 390 л\n' \
              f'<b>{transmission}</b> Автоматическая\n' \
              f'<b>{drive_unit}</b> Передний\n' \
              f'<b>{front_suspension}</b> Независимая пружинная\n' \
              f'<b>{rear_suspension}</b> Полунезависимая пружинная\n' \
              f'<b>{front_brakes}</b> Дисковые вентилируемые\n' \
              f'<b>{rear_brakes}</b> Барабанные\n' \
              f'<b>{production}</b> Россия\n' \
              f'<b>{warranty}</b> 5 лет или 150000 км\n'
