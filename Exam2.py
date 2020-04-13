#Yanira Manzano
#4/13/2020
#Exam2

import random
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge_sort
from Search_Methods import quick_sort

list = []

run = True
run2 = True

menu = 0

while menu != 6:
    print("Welcome")
    print("1.Bubble Sort")
    print("2.Selection Sort")
    print("3.Insertion Sort")
    print("4.Merge Sort")
    print("5.Quick Sort")
    print("6.Quit
    menu = int(input(">"))
    
    if menu == 1:
        print("Bubble Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"Done. Your list is {list}")
        y = Search_Methods.bubble_sort(x)
        menu = input("(Input anything to go back to menu)")
        list.clear()
        run = True
        
    if menu == 2:
       print("Selection Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"Done. Your list is {list}")
        y = Search_Methods.selection_sort(x)
        menu = input("(Input anything to go back to menu)")
        list.clear()
        run = True
        
    if menu == 3:
       print("You have selected the Insertion Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"Done. Your list is {list}")
        y = Search_Methods.insertion_sort(x)
        menu = input("(Input anything to go back to menu)")
        list.clear()
        run = True
        
    if menu == 4:
       print("You have selected the Merge Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"Done. Your list is {list}")
        y = Search_Methods.merge_sort(x)
        menu = input("(Input anything to go back to menu)")
        list.clear()
        run = True
        
    if menu == 5:
       print("You have selected the Quick Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"Done. Your list is {list}")
        y = Search_Methods.quick_sort(x)
        menu = input("(Input anything to go back to menu)")
        list.clear()
        run = True
         
    if menu == 6: 
       print("Bye.")
        sys.exit()
        
