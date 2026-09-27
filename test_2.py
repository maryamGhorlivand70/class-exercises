print ("start")

def test():
    print(1/0)

try:
    a = []
    file = open("A","rt")

except ValueError:
    print("خگز رز مقرای")
except ZeroDivisionError:
    print("نام تعریف نشره")

except IndexError:
    print("انربس غیر مجار")

except:
    print("سایر خگاها_ تماس با ارمین")

print("finish")
