n = int(input())
# for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print("")    


# for i in range(1,n+1):

    # for j in range(n-i):
    #     print(end=" ")
    # for j in range(2*i-1):
    #     print("*",end="")    
    # for j in range(n-i):
    #     print(end=" ")
    # print("")        
    # for j in range(i):
    #     print(end=" ")
    # for j in range(2*(n-i)+1):
    #     print("*",end="")
    # for j in range(i):
    #     print(end=" ")    
    # print("")    


# for i in range(1,2*n+1):
#     if i > (2*n)//2:
#         for j in range(2*n - i):
#             print("*",end="")
#         print(""    )
#     else:     
#         for j in range(i):
#             print("*",end="")
#         print("")
       


# for i in range(1,n+1):
#     if i % 2==0:
#         flag=0
#     else:
#         flag=1
#     for j in range(i):
#         print(flag,end="")
#         flag=1-flag
#     print("")               

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(2*(n-i)):
#         print(" ",end="")
#     for j in range(i):
#         print(i-j,end="")
#     print("")

# count =1
# for i in range(1,n+1):
#     for j in range(i):
#         print(count,end=" ")
#         count+=1
#     print("")

# for i in range(1,n+1):
#     for ch in range(ord('A'), ord('A')+i): #ord() function gives ASCII value of character
#         print(chr(ch),end="")
#     print("")    

# for i in range(n, 0, -1):
#     for cp in range(ord('a'), ord('a') + i):
#         print(chr(cp), end="")
#     print()


# for i in range(n):
#     for cp in range(i+1):
#         print(chr(ord('a')+i), end="")
#     print()


# for i in range(1,n+1):

#     for j in range(n-i):
#         print(end=" ")
#     ch="A"
#     bp= (2*i-1)//2   
#     for j in range(2*i-1):
#         print(ch,end="")
#         if j <bp:
#             ch=chr(ord(ch)+1)
#         else:
#             ch=chr(ord(ch)-1) 
#     for j in range(n-i):
#         print(end=" ")
#     print("")      

# for i in range(n):
#     for ch in range(ord('E')-i,ord('E')+1): #ord() function gives ASCII value of character
#         print(chr(ch),end="")
#     print("") 