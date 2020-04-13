# Yanira Manzano
# 4/13/2020
# Methods


#Bubble Sort: takes in an unsorted list and keeps comparing each element with its right side in order to sort the data.
def bubbleSort(alist):
   for i in range(len(alist)-1,0,-1):
       for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

 return alist

                
#Selection Sort:works best with a small number of elements.
def selectionSort(alist):
   for i in range(len(alist)):
    for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
               
#Insertion Sort: works best with small number of elements.
def insertionSort(alist):
   for i in range(1,len(alist)):
       current = alist[i]
        while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
          alist[i] = current     
          
"""Merge Sort: It will be divided in 2. Merge Sort works both with a large 
and small number of elements making it more efficient than the Other Sorts"""
def mergeSort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       mergeSort(lefthalf)
       mergeSort(righthalf)
       i=0
       j=0
       k=0
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
           
#Quick Sort: Quick Sort works best with small and large number of elements.
def quickSort(alist):

  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

  if first<last:
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark


               
