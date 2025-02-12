subjects = ["I", "We"]
verbs = ["play", "watch"]
objects = input().split()       #split and add the input into a list 

for i in subjects :             #to keep 1st subject same for first 4 outputs and 2nd subject same for last 4 outputs 
    for j in verbs :            #
        for k in objects :      #to keep same object for odd line outputs
            print(i,j,k, end='.\n' )        #keep the output orderly (subject-verb-object) and add '.' lastly