print("start")
def test():
    print(1/0)
try:
    print(1)
    test()
    print(2)
except:
    print("Error")

print("finish")
