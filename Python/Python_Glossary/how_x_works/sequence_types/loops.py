x = [1,2,3,4,5]
y = ["one","two","three","four","five"]
z = [[5], [5, 10], [10,20], [20,40], [40,80]]





x.remove(4)
print(x)
for i in x:
    print(i)

re = [1,1,2,3,3,4,5,5]
def test(list1):
    dict = {}
    for i in list1:
        #check if the element in list1 already exists in the dictionary
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

        print(dict)

test(re)
    
#chat gpt answer
'''
def count_common_elements(list1, list2):
    # Create two dictionaries to store the element counts for each list
    count_dict1 = {}
    count_dict2 = {}

    # Initialize counts for list1
    for element in list1:
        if element in count_dict1:
            count_dict1[element] += 1
        else:
            count_dict1[element] = 1

    # Initialize counts for list2
    for element in list2:
        if element in count_dict2:
            count_dict2[element] += 1
        else:
            count_dict2[element] = 1

    # Initialize a variable to keep track of the common elements count
    common_count = 0

    # Iterate through the keys in count_dict1 and check if they also exist in count_dict2
    for key in count_dict1:
        if key in count_dict2:
            # Increment common_count with the minimum count of the element in both lists
            common_count += min(count_dict1[key], count_dict2[key])

    return common_count

# Example usage
list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 2, 3, 4, 4, 5, 5, 6]

common_elements_count = count_common_elements(list1, list2)
print("Number of common elements:", common_elements_count)
'''