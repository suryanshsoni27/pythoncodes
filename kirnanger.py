import matplotlib.pyplot as plt
import numpy as np
def angry(b):
	if b == 1:
		print("i am sorry")
		t = np.arange(0, 2 * np.pi, 0.1)
		x = 16 * np.sin(t) ** 3
		y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
		plt.plot(x, y)
		plt.show()
	else:
		print("puchi puchi")


print("options:")
print("enter 1 if you fought with kiran")
print("enter 2 if you love kiran")

a = int(input("enter what you did:: "))
print(" ")

if a == 1:
	angry(a)

else:
	angry(a)
	i = 0
	for i in range(5):
		print(u"\u2661" + u"\u2661" + u"\u2661" + u"\u2661")
		t = np.arange(0, 2 * np.pi, 0.1)
		x =16 * np.sin(t) ** 3
		y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
		plt.plot(x, y)
		plt.show()