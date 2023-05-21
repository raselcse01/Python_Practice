def student(*details):
    print(details)


student(101,'rasel')
student(101,'rasel', 3.75)


def add(*numbers):
    print(numbers)


add(101,'rasel')
add(101,'rasel', 3.75)

def stu(**details):
    print(details['name'])

stu(id=101, name='Rasel')