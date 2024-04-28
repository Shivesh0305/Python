class Something:
    a="attribute"

    @staticmethod
    def greet(name):
        print("Hello "+name)

obj=Something()
obj.a="jwev"

print(Something.a)
print(obj.a)
obj.greet("shivesh")