def is_palindrome(num :int) :
    if str(num) == str(num)[::-1] :
        return True
    else :
        return False

def binary_val(num :int) :
    binary = str(bin(num))[2:]
    bin_val = int(binary)
    return bin_val


while True :
    num_input = int(input("Enter a number: "))
    if num_input == -1 :
        break
    elif 1 <= num_input <= 100000 :
        if is_palindrome(num_input) == True and is_palindrome(binary_val(num_input)) == True :
            print("YES")
        else :
            print("NO")
    else :
        print("Range should be 1 to 100000")
        continue



