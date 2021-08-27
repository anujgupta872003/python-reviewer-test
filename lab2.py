

def main():
    ask_again = True
	operations_count = 0
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
		operations_count += 1
        result = perform_division(a,b,operations_count)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False			
            print("You performed " + str(operations_count) + " operations, bye!")


def perform_division(a,b,operations_count):    
    try:        
        return int(a)/int(b)
	except ZeroDivisionError as e:
        print('ZeroDivisionError: Not Possible')
    except Exception as e:
        pass


main()