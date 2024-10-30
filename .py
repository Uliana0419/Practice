import decimal

# Установка точности
def calculate_pi(n):
    # Задаём точность
    decimal.getcontext().prec = n + 2  # +2 для округления

    # Формула Бэйли-Боруэйна-Азад-Зимана (BBP)
    pi = decimal.Decimal(0)
    k = 0
    while k < 100:  # число итераций, может быть увеличено для большей точности
        pi += (decimal.Decimal(1) / decimal.Decimal(16) ** k) * (
            decimal.Decimal(4) / (8 * k + 1) -
            decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) -
            decimal.Decimal(1) / (8 * k + 6)
        )
        k += 1
        
    # Округляем до нужного количества знаков
    return str(pi)[:n + 2]  # +2 для учёта '3.'

# Ввод количества знаков после запятой
n = int(input("Введите количество знаков после запятой: "))
pi_value = calculate_pi(n)

print(f"Число π до {n} знака(ов) после запятой: {pi_value}")