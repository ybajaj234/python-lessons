with open ("name.txt") as f:
    my_name= f.read()
with open('output/hello.txt', 'w+') as f:
    f.write('hello, hello my name is')
    f.write(my_name)