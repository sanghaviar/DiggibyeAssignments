def list_operations(N):
    # Number of operations that user wish to perform
    # N = int(input())
    # Initiating empty list
    mylist = []
    # For loop iterates to perform number of operations
    for i in range(N):
    #   # storing the values in variable command, converting to lower case, and splitting the values
        command = input().lower().split()
        # matching the command
        match (command[0]):
            # inserting the values at specified index
            case 'insert':
                mylist.insert(int(command[1]), int(command[2]))
            # Appending the value at the end of the list
            case 'append':
                mylist.append(int(command[1]))
            # pop out the last element of the list
            case 'pop':
                mylist.pop()
            # sorting the elements of list in ascending order
            case 'sort':
                mylist.sort()
            # Display(print) the list
            case 'print':
                print(mylist)

            # Removing the specific element from the list
            case 'remove':
                mylist.remove(int(command[1]))
            # Reversing the elements of list
            case 'reverse':
                mylist.reverse()
    return mylist