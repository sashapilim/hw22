# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, field, x, y, direction, fly: bool, crawl: bool):
        """Функция реализует перемещение юнита по полю.
        :param field: поле по которому перемещается юнит
        :param x: x-координата юнита
        :param y: у- координата юнита
        :param direction: направление перемещения
        :param fly: летит ли юнит
        :param crawl: крадется ли юнит
        :param speed: базовый параметр скорости
        """
        # Проверка чтобы герой одновременно не летел и не полз:
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if direction == 'UP':
            new_y = y + self.get_speed()  # увеличим Y на текущую скорость
            new_x = x  # Х без изменений
        elif direction == 'DOWN':
            new_y = y - self.get_speed()  # уменьшим Y на текущую скорость
            new_x = x  # Х без изменений
        elif direction == 'LEFT':
            new_y = y  # Y без изменений
            new_x = x - self.get_speed()  # уменьшим Х на текущую скорость
        elif direction == 'RIGHT':
            new_y = y  # Y без изменений
            new_x = x + self.get_speed()  # увеличим Х на текущую скорость

        return field.set_unit(x=new_x, y=new_y, unit=self)

    def get_speed(self, speed=1):
        """Функция реализует расчет скорости в зависимости от движения - летит/ползет."""
        if self.fly:
            return speed * 2
        elif self.crawl:
            return speed * 0.5
        raise ValueError('Герои могут только летать или ползать!')

#     ...
