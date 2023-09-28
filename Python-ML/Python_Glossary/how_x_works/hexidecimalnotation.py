'''
Design a service like TinyURL, a URL shortening service, 
a web service that provides short aliases for redirection of long URLs.
'''

#convert a long URL/string to short
def encode():
    pass

#convert short URL/string to long
def decode():
    pass

#convert the representation of a number to a hexidecimal
    #by doing integer division and remainder operations in the source base
def simpleBaseConversion(digit):
    rep_hex = digit % 16
    if digit - rep_hex == 0:
        print(str(rep_hex))
        return 1
    return simpleBaseConversion((digit - rep_hex)/16) + charConversion(rep_hex)

def charConversion(ch):
    alpha = '123'
    return alpha[ch]
    
    
#simpleBaseConversion(6)

def convertNumtoBinary(num):
    binary_list = []
    mod = num%2
    if num < 2:
        print(binary_list)
        return 1
    return convertNumtoBinary(binary_list.append(num%2)) #this does not work because .append() does not return a value

#convertNumtoBinary(12)



#Recursivity revisited
def generate_numbers(start, end):
    # Base case: If start is greater than end, return an empty list
    print("start1", start)
    

    if start > end:
        return []
    # Recursive case: Generate the numbers from start to end
    else:
        print("start2", start)
        numbers = generate_numbers(start + 1, end) # 0+1, 10
        print("first", numbers)
        #insert start var at index 0. easier than append since it will result in an ascending list whereas .append() will result in a descending list
        print("start3", start)
        numbers.insert(0, start) #
        print("second", numbers) 
        return numbers

# Call the function to generate numbers from 0 to 10
#numbers_list = generate_numbers(0, 10)

def new_approach(start, end):
    #base case
    if start > end:
        return []
    else:
        new_list =  new_approach(start+1, end)
        new_list.insert(0, start)
        return new_list

answer = new_approach(0, 10)
print(answer)
    
    
# Print the result
#print(numbers_list)

'''
--Binary Representation--

to convert a number to binary:
1. n / 2 = quotient + remainder
2. repeat until at base where n modulo can no longer be done
3. take the remainder of each iteration and reverse order, that's its binary representation


d = number to represent hex
h1...hn = series of hex digits

splitting number B3AD to decimal:
B: (11_10) 3 (3_10) A (10_10) D (13_10)
a hexidecimal multiplication table

  1   2   3    4   5   6   7    8    9    A    B    C    D    E    F    10
1 1                                       
2     4   6    8   A   C   E    10   12   14   16   18   1A   1C   1E   20
3         9                                   
4              10                                 
5                  19                               
6                      24                             
7                          31                           
8                               40                        
9                                    51                      
A                                         64                  
B                                              79               
C                                                   90            
D                                                        A9         
E                                                             C4       
F                                                                  E1   
10                                                                 F0   100
'''