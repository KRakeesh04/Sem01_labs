N = int(input("Number displayed N: ").strip())
N_str = str(N)
prefixes_list = []
if 3 <= len(N_str) <= 16 :
    for i in range(1, len(N_str)) :
        if int(N_str[:i]) % 4 == 0 :
            prefixes_list.append(N_str[:i])
        else :
            continue

else :
    print("check the 'N' value")
    exit()

print("Possible prefixes: ", end='')
for num in prefixes_list[:0:-1] :
    print(num, end=', ')
print(prefixes_list[0])




