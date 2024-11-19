def simular_clima(temp_inicial, prob_lluvia_inicial, num_dias):
    temperatura = temp_inicial
    prob_lluvia = prob_lluvia_inicial
    lluvia = False
    temp_max_lluvia = float('-inf')
    temp_min_lluvia = float('inf')
    
    for dia in range(1, num_dias + 1):
        if random.random() < 0.1:
            cambio_temp = random.choice([-2, 2])
            temperatura += cambio_temp
        
        if temperatura > 25:
            prob_lluvia += 0.20
        
        if temperatura < 5:
            prob_lluvia -= 0.20
        
        if prob_lluvia >= 1.0:
            prob_lluvia = 1.0
            temperatura -= 1
            lluvia = True
            if temperatura < temp_min_lluvia:
                temp_min_lluvia = temperatura
            if temperatura > temp_max_lluvia:
                temp_max_lluvia = temperatura
        else:
            lluvia = False
            if temperatura < temp_min_lluvia:
                temp_min_lluvia = temperatura
            if temperatura > temp_max_lluvia:
                temp_max_lluvia = temperatura
        print(f"Día {dia}: Temperatura: {temperatura}°C, ¿Lluvia?: {'Sí' if lluvia else 'No'}")
    
    print(f"\nResumen del clima:\n- Temperatura máxima durante lluvia: {temp_max_lluvia}°C\n- Temperatura mínima durante lluvia: {temp_min_lluvia}°C")


def principal():
    temp = int(input("TEMPERATURA: "))
    prob = float(input("PROBABILIDAD DE LLUVIA: "))
    prob = prob / 100
    num = int(input("NÚMERO DE DÍAS: "))
    simular_clima(temp,prob,num)
principal()