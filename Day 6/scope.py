# a=10


# def number():
#     global a
#     a=11
#     print(a)


# number()
# print(a)


x=9
def outer():
    x=10
    def inner():
        x=11
        print(f"inner sees x as {x}")
    inner()
    print(f"outer sses x as {x}")


outer()
print(f"globel sees x as {x}")