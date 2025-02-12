#function to calculate the beam deflection using the given parameters (P, L, I, E)
def beam_deflection(Length :float, youngsModulus :float, momentOfInertia :float, Load :float) :
    Dmax = round( ((Load * 1000 * (Length**3)) / (48 * youngsModulus * (10**9) * momentOfInertia)) , 6)
    return Dmax


#function to calculate the bending stress of the beam using the given parameters (P, L, I)
def bending_stress(Length :float, momentOfInertia :float, Load :float) :
    Smax = round( (((Load * 1000) * Length) / (4 * momentOfInertia)) , 2)
    return Smax


#taking input of the file name which has the data collection and read the file and close it.
file_name = input()
file = open(file_name, "r")
file_details = file.readlines()
file.close()

#creating 2-D list to add all the data to the list after changing the element type into float
input_values = [ ]
for j in file_details :
    j = j.replace("\n", '')
    input_values.append(list(map(float, j.split())))


    
#calling the stress and deflection functions to calculate the maximum values and print the values in order
for val in range(len(input_values)) :
    maximum_Deflection = beam_deflection(Length=input_values[val][0], youngsModulus=input_values[val][1], momentOfInertia=input_values[val][2], Load=input_values[val][3])
    maximum_Stress = bending_stress(Length=input_values[val][0], momentOfInertia=input_values[val][2], Load=input_values[val][3])
    print("Beam", str(val + 1)+': Length:', input_values[val][0], 'm,', "Max Deflection:","{:.6f}".format(maximum_Deflection), "m, Max Bending Stress:", "{:.2f}".format(maximum_Stress), 'Pa')
    
    
