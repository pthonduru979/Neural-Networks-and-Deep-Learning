# Student ID: 700747587
#       CRN :23476


#Question 1A

S = list(input("Enter the string 'Python': "))

if len(S) >= 2:
    del S[:2]
    # Reverse the resultant string
    reversed_string = S[::-1]
    print("Reversed String:", ''.join(reversed_string))

    


