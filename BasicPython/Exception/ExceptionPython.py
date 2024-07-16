ItemInCart = 2
if ItemInCart !=2:
    #raise Exception("Products carts count not mathcing")
    pass
assert(ItemInCart == 2)

## try, catch

try:
    with open('test1.txt', 'r') as reader:
        reader.read()
except:
    print("there is no file available and we can contiue")



try:
    with open('test1.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resources")


