def ex1():
    numbers=[1,3,10,7,5,11,6,4]
    print("Array:",numbers)
    odd_numbers=[]
    for number in numbers:
        if number % 2 !=0:
            odd_numbers.append(number)
    print("Odd numbers in array", odd_numbers)
def ex2():
   numbers=[]
   n =int(input("Enter the number of elements:"))
   for i in range(n):
       num=int(input(f"Numbers {i+1}:"))
       numbers.append(num)
   print("Array: ",numbers)
def ex3():
    numbers=[]
    n=int(input("Enter the number of elements "))
    for i in range(n):
        num =int(input(f"Numbers {i+1} :"))
        numbers.append(num)
    #Sum even
    total_even=0
    for number in numbers:
        if number % 2 ==0:
            total_even+=number
    #Sum odd
    total_odd=0
    for number in numbers:
        if number % 2 !=0:
            total_odd+=number
    print("Total Elements in the Array:",len(numbers)) 
    print("The largest number in the array :",max(numbers))
    print("The smallest number in the array :",min(numbers))
    print("Sum Even:",total_even)
    print("Sum odd :",total_odd)
def ex4():
    numbers1=[]
    numbers2=[]
    n1=int(input("Enter the number of elements for array 1: "))
    for i in range(n1):
        num=int(input(f"Enter element {i+1} of array 1 :"))
        numbers1.append(num)
    n2=int(input("Enter the number of elements for array 2:"))
    for i in range(n2):
        num=int(input(f"Enter  elements {i+1} of array 2:"))
        numbers2.append(num)
    #Max,min    
    max_values=max(max(numbers1),max(numbers2))
    print("The largest number in both arrays is",max_values)
    min_values=min(min(numbers1),min(numbers2))
    print("The smallest number in both arrays is ",min_values)
    #những số chung
    common_numbers=list(set(numbers1)&set(numbers2))
    print("The common numbers in both arrays are:", common_numbers)

    unique1=list(set(numbers1)-set(numbers2))
    print("The unique numbers in array 1 not found in arrat 2 are",unique1)
    unique2=list(set(numbers2)-set(numbers1))
    print("The unique numbers in array 2 not found in arrat 1 are ,", unique2)
def menu():
    while True:
        choice=int(input("\nEnter a choice: "))
        if choice == 1:
            ex1()
        if choice == 2:
            ex2()
        if choice == 3:
            ex3()
        if choice == 4:
            ex4()
if __name__ == "__main__":
    menu()