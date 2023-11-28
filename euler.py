## If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
def sum_of_multiples(mutiple1, multiple2, lower_limit, higher_limit):
    sum = 0

    #Iterate from 1 to 1000

    for i in range (lower_limit, higher_limit):
        
        #add if multiple of 3 or 5
        if (i % mutiple1 == 0 or i % multiple2 ==0):
            sum += i 

    return(sum)

print(sum_of_multiples(3, 5, 1, 1000))

print(sum_of_multiples(3, 8, 1, 1000))
