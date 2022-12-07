number_Of_Rows=int(input("Enter the row :"))
number_Of_Columns=int(input("Enter the column :"))
for i in range(0,number_Of_Rows):
    for j in range(0,number_Of_Columns):
        if(i==0 and j==0):
            print(1, end=" ")
        elif(i==(number_Of_Rows-1)and j==(number_Of_Columns-1)):
            print(number_Of_Rows*number_Of_Columns, end=" ")
        else:
            print((i*2)+(j*3), end=" ")
    print(" ")

