print("Number")
print("type(12) = ", type(12))
print("isinstance(12, int) = ", isinstance(12, int))
print("type(1/3) = ", type(1/3))
print("isinstance(1/3, int) = ", isinstance(1/3, int))
print("type(1.0) = ", type(1.0))
print("isinstance(1.0, float) = ", isinstance(1.0, float))
print("5 + 1.0 = ", 5 + 1.0)
print("int(5 + 1.0) = ", int(5 + 1.0))
print("float(\"Inf\") = ", float("Inf"))
print("float(\"-Inf\") = ", float("-Inf"))
print("float(\"NaN\") = ", float("NaN"))
print("Boolean")
print("type(True), type(False) = ", type(True), type(False))
print("isinstance(True, bool) = ", isinstance(True, bool))
print("20 > 10, type(20 > 10) = ", 20 > 10, type(20 > 10))
print("20 == 10, type(20 == 10) = ", 20 == 10, type(20 == 10))
print("20.0 == 20, type(20.0 == 20) = ", 20.0 == 20, type(20.0 == 20))
print("20.0 != 20, type(20.0 != 20) = ", 20.0 != 20, type(20.0 != 20))
print("not False, bool(1), bool(0) = ", not False, bool(1), bool(0))
print("String")
print("type(\"cat\") = ", type("cat"))
print("type(\"1\") = ", type("1"))
print("type(\"\") = ", type(""))
print("None")
print("type(None) = ", type(None))
def function(x):
    print(x)
print("function(\"hello\") == None", function("hello") == None)