# def sudoko_solver(arr):
#     sudoko_check(arr)

def sudoko_check(arr):
    #for rows
    for i in range(9):
        c=0
        for j in range(1,10):
            if(arr[i][j-1]==j):
                c+=1
        if(c!=1):
            print(i,j)
            print('invalid')
            # return 

def sudoko_input(n):
    for i in range(0,9):
        print(arr[i])
        
arr = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0] ]  
print("for 3*3 sudoko enter the values row wise")
print("enter '.' for blank spaces")
# for i in range(0,9):
#     row=[]
#     for j in range(0,9):
#         row.append(input())
#     arr.append(row)
sudoko_input(arr)
sudoko_check(arr)
# sudoko_solve(arr)
    