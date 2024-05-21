# This function removes duplicates from a list of numbers
# Define the function
def remove_dups(vals):
    
    # create a blank list
    uniques_vals = []
    
    # create a for loop that will iterate over each value in the list 'unique_vals'
    for num in vals:
        if num not in uniques_vals:
            uniques_vals.append(num)
    return uniques_vals

# example
vals = [22, 44, 44, 13, 82, 2, 82]
unique_vals = remove_dups(vals)
print(unique_vals)

# Output expected: []