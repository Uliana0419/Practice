import decimal

def calculate_pi(n): # Установка точности
    decimal.getcontext().prec = n + 2   # Задаём точность

    pi = decimal.Decimal(0) # Формула 
    k = 0
    while k < 100:  
        pi += (decimal.Decimal(1) / decimal.Decimal(16) ** k) * (
            decimal.Decimal(4) / (8 * k + 1) -
            decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) -
            decimal.Decimal(1) / (8 * k + 6)
        )
        k += 1
        
    return str(pi)[:n + 2]  # +2 для учёта '3.' # Округляем до нужного количества знаков

n = int(input("Введите количество знаков после запятой: "))
pi_value = calculate_pi(n)

print(f"Число π до {n} знака(ов) после запятой: {pi_value}")
