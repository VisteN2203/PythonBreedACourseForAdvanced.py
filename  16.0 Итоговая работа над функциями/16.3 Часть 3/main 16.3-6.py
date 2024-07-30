def call(func, *args, **kwargs):
	return func(*args, **kwargs)

print(call(bool, 0))