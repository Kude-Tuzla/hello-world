def fib_seq(n): #defining a function so it can be reused
    a, b = 0, 1 #assigning variables: a is 0 and b is 1
    while a <= n: #using a variable n to set maximum value to which the sequence will go
        print(a, end=' ') #end=' ' makes the printing on terminal go in one line and separates the sequence with space
        a, b = b, a + b #this is how fibonacci sequence is formed: last entry is the sum of previous two, therefore b, a+b
