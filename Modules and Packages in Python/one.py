#one.py

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")


if __name__ == '__main__':
	print("ONE.PY IS BEING RUN DIRECTLY")
	func()

else:
	print("ONE.PY IS IMPORTED")