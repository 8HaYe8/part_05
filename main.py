c = int(input())
print("%4.0f" % c)
print("{0:4.0f}".format(c))
print(f"{c:4.0f}")

z_float_1 = float(input())
print("%8f" % z_float_1)
print("{0:8f}".format(z_float_1))
print(f"{z_float_1:8f}")

x_float_2 = float(input())
print("%6.3f" % x_float_2)
print("{0:6.3f}".format(x_float_2))
print(f"{x_float_2:6.3f}")

str = input()
print("{0:.2}".format(str))
print(f"{str:.2}")
