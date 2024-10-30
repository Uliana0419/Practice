def get_float_number():
    """Запрашивает у пользователя ввод числа с плавающей запятой."""
    while True:
        try:
            # Ввод числа от пользователя
            number = float(input("Введите число с плавающей запятой: "))
            return number
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, попробуйте снова.")

def get_decimal_places():
    """Запрашивает у пользователя количество знаков после запятой, до которого нужно округлить."""
    while True:
        try:
            # Ввод количества знаков после запятой
            decimal_places = int(input("Введите количество знаков после запятой для округления: "))
            if decimal_places < 0:
                # Проверка на неотрицательность
                print("Количество знаков должно быть неотрицательным. Пожалуйста, попробуйте снова.")
                continue
            return decimal_places
        except ValueError:
            print("Ошибка: введено не целое число. Пожалуйста, попробуйте снова.")

def round_number(number, decimal_places):
    """Округляет число до заданного количества знаков после запятой."""
    rounded_number = round(number, decimal_places)
    return rounded_number

def main():
    """Основная функция программы."""
    print("Это программа для округления числа до заданного количества знаков после запятой.")
    
    # Получение числа от пользователя
    number = get_float_number()
    
    # Получение количества знаков после запятой
    decimal_places = get_decimal_places()
    
    # Округление числа
    rounded_result = round_number(number, decimal_places)
    
    # Вывод результата
    print(f"Округленное число {number} до {decimal_places} знаков после запятой: {rounded_result}")

if __name__ == "__main__":
    main()
