arr=[
    [2,0,1],
    [1,1,0],
    [2,0,3]
]


# position value matrix
for row in range(0,3):
    for col in range(0,3):
        val=row +col-arr[row][col]
        print(val,end="\t")
    print()