"""
A natural number in a given number base is a p-Kaprekar number if the
representation of its square in that base can be split into two parts,
where the second part is to the right of the first part, that add up to
the original number.
"""

# check if the split sum of any permutation is equal to the square
def split_sum(num):
    
    num_sum = 0
    num_squared = str(num**2)

    for x in range(0,len(num_squared)):        
        first_split = num_squared[0:x+1]        
        second_split = num_squared[x+1:len(num_squared)]

        try:
            num_sum = int(first_split.lstrip("0")) + int(second_split.lstrip("0"))
        except:
            return False
        
        if num == num_sum:
            return True
        
    return False

# generate list of kaprekar numbers
def generate_kaprekar_list(size):
    kaprekar_list = []

    for i in range(1,size):
        if split_sum(i) == True:
            kaprekar_list.append(i)
            
    return kaprekar_list
