import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from cs1033_evaluator import evaluate_lab9
import matplotlib.pyplot as plt

input_file_name = input()

# Your code should be included here. 
# Avoid using the print function in the code, as it may cause errors



#function to read the input file and add the splitted data to the list, which is from the file and return the list
def read_file(name :str) :
    file = open(name, 'r')
    file_data = file.readlines()
    file.close()

    input_data_list = [ ]
    for data in file_data :
        data = data.replace("\n", '')
        input_data_list.append(list(map(float, data.split(','))))
    return input_data_list

#function to calculate the output voltage using R1 & R2 values
def output_voltage(V_in, R1, R2) :
    V_out = V_in * (R2 / (R1 + R2))
    return V_out

#function to calculate the power
def power_disssipation(V_in, R1, R2) :
    power = (V_in **2) / (R1 + R2)
    return power

#function to write the output to the output list
def write_output(R1, R2) :
    file = open("output.txt", 'w')
    data = str(int(R1)) + ', ' + str(int(R2))
    file.write(data)
    file.close()

#function to find the correct R! and R2 values
def findout_R1_R2(resistors :list) :
    results = { }
    data_list = [ ]
    ordered_list = sorted(resistors)
    for i in ordered_list :
        for j in ordered_list :
            V_out = output_voltage(input_voltage, i, j)
            power = power_disssipation(input_voltage, i, j)
            if V_out >= (desired_output_voltage - tolerance) and V_out <= (desired_output_voltage + tolerance) :
                results['R1'] = i
                results['R2'] = j
                results['V_out'] = V_out
                results['power'] = power
                data_list.append(results)
            results = { }
    minimal_val = data_list[0]['power']
    for k in data_list  :
        if k['power'] < minimal_val :
            minimal_val = k['power']
            correct_dict = k
    return correct_dict['R1'], correct_dict['R2']



#main programme
data = read_file(input_file_name)
input_voltage, desired_output_voltage, tolerance  = data[0]
Resistor_list = data[1]

R1 , R2 = findout_R1_R2(Resistor_list)
write_output(R1, R2)



#calculating data for graph plotting
RL_list = []
Vout_list = []
for R_L in range(10,1001,10) :  #calculating new voltage and add V_new and R_L values to different lists for graph
    R2_RL = (R2*R_L)/(R2 + R_L)
    V_new = (input_voltage*R2_RL)/(R1 + R2_RL) 
    RL_list.append(R_L)
    Vout_list.append(V_new)


plt.plot(RL_list,Vout_list, color='#05CD99')
plt.xlabel("Resistance (ohms)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs Resistance")
plt.xticks([0,200,400,600,800,1000])
plt.yticks([1,2,3,4])
plt.grid(True, which='both', linestyle='--', color='gray', linewidth=0.5)
plt.show()



################################################################################
# Please do not edit anything below this line.
evaluate_lab9()

##################### End of the programme #####################################