#Pascals triangle

#where n is the row

def pascal_line(n):
    return pascal_rec(n)


def pascal_rec(n):
        #Base case
    if n == 0: return [1]

    elif n == 1: return [1, 1]

        #Recursive case

    else:

        pre_row = pascal_rec(n - 1) #previous row
    
        row = [1]
        
        for i in range(1, len(pre_row)): 

            row.append(pre_row[i-1] + pre_row[i])   
        
        row.append(1)

        return row
           

print(pascal_line(3))


