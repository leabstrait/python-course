def filterer(fn_x_b, lox):
    lox_filtered = []
    for x in lox:
        if fn_x_b(x):
            lox_filtered.append(x)
    
    return lox_filtered

above_body_temp = lambda t_c : t_c < 36

temp_readings = [10, 20, 25, 21.4, 36, 39, 40]

temp_filtered = filterer(above_body_temp, temp_readings)

# print(temp_readings)
# print(temp_filtered)

# print(list(filter(above_body_temp, temp_readings)))

double_temp = lambda t: 2*t

print(list(filter(above_body_temp, map(double_temp, filter(above_body_temp, temp_readings)))))


