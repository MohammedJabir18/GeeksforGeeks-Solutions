#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i = 1
    # Loop to jump in powers of 2
    while (i * i <= x):
        ##Your code here
        print (i * i , end = " ")
        
        ##Your code here
        i += 1

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
# } Driver Code Ends