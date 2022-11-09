"""MEAN  MODE  MEDIAN  RANGE"""

#create an empty list to collect list of numbers form user
list1=[]
# collect data with while loop until user entered nothing
def User_Data():
    while True:
        number=input("Enter number: ")
        #exception handling to avoid Error from user input 
        try:
            if number =="":
                break
            else:
                number=float(number)
                list1.append(number)
        except:
            print("Oops..! Inalid input")        

def mean():
    #mean_x for sum of numbers
    mean_x=0
    #mean_y for no of numbers
    mean_y=len(list1)
    for i in list1:
        mean_x+=i 
    print("\n\nMEAN : Sum of Numbers divided by No.of Numbers.")
    #conclude with mean formulae
    print("MEAN= ",mean_x/mean_y)

def mode():
    #empty dictionary to collect no of appeared Numbers as keys and values
    mode_x={}
    #count No.of appeared numbers & add to dictionary using for loop
    for j in list1:
        count=0
        for k in list1:
            if j==k:
                count+=1
        #update dictionary 
        mode_x[j]=count
    #get max value in dictionary values
    mode_y=max(mode_x.values())
    #get key with max value in dictinary by using for loop
    for l,m in mode_x.items():
        if m==mode_y:
            result=l
    #to know if all entered numbers are different
    mode_z=len(list1)  #know length
    same_or_not=0
    for p in mode_x.values():    #to check if number is repeated 
        for q in mode_x.values(): 
            if p==q:          # Checking all values same or not
                same_or_not+=1
    mode_check=mode_z **2
    #if user enterd all different values
    if mode_check==same_or_not:
        print("\nMODE : The number that appears mostly.\n(You entered all different numbers,So all Numbers are considered as Mode numbers)")
        print("MODE=",list1)
    #if user enterd numbers by appearing again
    else:
        print("\nMODE : The number that appears mostly.")
        print("MODE=",result)

def median():
    #arrange list in assending order
    list1.sort()
    # know length of list
    median_x=len(list1)
    print("\nMEDIAN : The number which is in the middle or middle value after sorted.")
    # for even no.of Numbers
    if median_x%2 == 0:
        #getting middle value by indexing in list
        median_y=list1[median_x//2]
        median_z=list1[(median_x//2)-1]
        print("MEDIAN=",median_y,",",median_z)
    #for odd no.of Numbers
    else:
        median_y=list1[median_x//2]
        print("MEDIAN=",median_y)

def range():
    #after sorting get min value in list
    range_x=list1[0]
    #max value in list
    range_y=list1[-1]
    #diff b/w min and max
    range_z=range_y-range_x
    print("\nRANGE : The difference between the largest and smallest number.")
    print("RANGE=",range_z)

#call the functions
User_Data()
mean()
mode()
median()
range()