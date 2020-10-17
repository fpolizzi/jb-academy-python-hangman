values = list()
input_string = input()

while input_string != ".":
    float_val = float(input_string)
    values.append(float_val)
    input_string = input()

values.sort()
print(values[0])
