# 3.5.3 The bubble sort – interactive version

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

```
Output
How many elements do you want to sort: 3
Enter a list element: 42
Enter a list element: 21
Enter a list element: 98

Sorted:
[21.0, 42.0, 98.0]
```
--- 
> Python, however, has its own sorting mechanisms.

> If you want Python to sort your list, you can do it like this:

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)



