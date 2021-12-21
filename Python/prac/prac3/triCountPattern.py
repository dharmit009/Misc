"""
QUESTION: 
Create the following pattern: 
1. Using for Loop. 
2. Using while Loop only.

1
2 3
4 5 6
7 8 9 10


"""

rows = int(input("Enter the number of Inputs: ")); 
tempRows = rows;
count = 1; 
currentRow = 1; 

while tempRows!=0: 
    while currentRow!=rows: 
        print(count); 
        count += 1; 
        currentRow += 1;
    tempRows-=1;

    













# print("### 1. First Triangle Pattern using FOR LOOP ###");
# for i, x in enumerate(range(rows)): 
#     for _ in range(i):
#         print(count, end=" "); 
#         count += 1; 
#     print("");
#         
        



