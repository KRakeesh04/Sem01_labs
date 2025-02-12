from cs1033_evaluator import evaluate_lab8
# Please do not edit anything above this line.
################################################################################
# Your code should be included here. 
# You should define and use the analyseSeriesCircuit(), analyseParallelCircuit() functions in your solution.



import math as m 

#function to read the details on a file and add them in a 2-D list
def read_file(name :str) :
    file = open(name, 'r')
    file_data = file.readlines()
    file.close()

    input_data_list = [ ]
    for data in file_data :
        data = data.replace("\n", '')
        input_data_list.append(data.split())
    return input_data_list
    


#functions for unit conversions
def millihenries_to_henries(induct_value :int) :
    final_value = induct_value / (10**3)
    return final_value
    
def microfarads_to_farads(cap_value :int) :
    final_value = cap_value / (10**6)
    return final_value



#function to calculate the angular frequncy of the RLC circuit
def angular_Frequency(frequency :int) :
    omega = 2 * m.pi * frequency
    return omega



#funtion to calculate the inductor impedance of the circuit 
def inductor_magnitudeOfImpedance(inductance :int, omega :float) :
    ZL = omega * inductance
    return ZL



#function to calculate the capacitor impedance of the circuit 
def capacitor_magnitudeOfImpedance(capacitance :int, omega :float) :
    ZC = 1 / (omega * capacitance)
    return ZC    
    


#function to calculate the total current of the RCL circuit
def circuit_current(voltage :int, Z_total :float) :
    I = voltage / Z_total
    current = round(I, 1)
    return current



#function for phasor angle
#function to calculate the phasor angle for RCL series
def angle_series_connection(Resistor :int, ZL :float, ZC :float) :
    alpha = m.atan((ZL - ZC) / Resistor)
    return alpha
    
#function to calculate the phasor angle for RCL parallel
def angle_parallel_connection(Resistor :int, ZL :float, ZC :float) :
    alpha = m.atan(((1/ZL) - (1/ZC)) * Resistor)
    return alpha



#Function for total impedance
#function to calculate the total impedance for RCL series connection
def Imp_series_Connection(Resistor :int, ZL :float, ZC :float) :
    total_Z = m.sqrt((Resistor ** 2) + ((ZL - ZC) ** 2))
    return total_Z
    
#function to calculate the total impedance for RCL parallel connection
def Imp_parallel_Connection(Resistor :int, ZL :float, ZC :float) :
    total_Z = 1 / (m.sqrt((1 /(Resistor ** 2)) + (((1/ZL) - (1/ZC)) ** 2)))
    return total_Z



#functions to analyzing connections
#function to analyzing series connection of R-L-C circuits
def analyseSeriesCircuit(data_list :list) :
    Resistor = int(data_list[1])
    inductance = millihenries_to_henries(int(data_list[2]))
    capacitance = microfarads_to_farads(int(data_list[3]))
    voltage = int(data_list[4])
    frequency = int(data_list[5])
    omega = angular_Frequency(frequency)
    Z_L = inductor_magnitudeOfImpedance(inductance, omega)
    Z_c = capacitor_magnitudeOfImpedance(capacitance, omega)
    Z_total = Imp_series_Connection(Resistor, Z_L, Z_c)
    I = circuit_current(voltage, Z_total)
    theeta = m.degrees(angle_series_connection(Resistor, Z_L, Z_c))
    return round(Z_L, 1), round(Z_c, 1), round(Z_total, 1), I , round(theeta, 1)

#function to analyzing parallel connection of R-L-C circuits
def analyseParallelCircuit(data_list :list) :
    Resistor = int(data_list[1])
    inductance = millihenries_to_henries(int(data_list[2]))
    capacitance = microfarads_to_farads(int(data_list[3]))
    voltage = int(data_list[4])
    frequency = int(data_list[5])
    omega = angular_Frequency(frequency)
    Z_L = inductor_magnitudeOfImpedance(inductance, omega)
    Z_c = capacitor_magnitudeOfImpedance(capacitance, omega)
    Z_total = Imp_parallel_Connection(Resistor, Z_L, Z_c)
    I = circuit_current(voltage, Z_total)
    theeta = m.degrees(angle_parallel_connection(Resistor, Z_L, Z_c))
    return round(Z_L, 1), round(Z_c, 1), round(Z_total, 1), I , round(theeta, 1)



#function to write outputs on the output file
def write_outputs(data_list :list) :
    file = open("result.txt",'w')
    for data in data_list :
        if data[0] == "series" :
            Z_L, Z_c, Z_total, I, theeta = analyseSeriesCircuit(data)
            value = str(Z_L) + ' ' + str(Z_c) + ' ' + str(Z_total) + ' ' + str(I) + ' ' + str(theeta) + '\n'
            file.write(value)
        elif data[0] == "parallel" :
            Z_L, Z_c, Z_total, I, theeta = analyseParallelCircuit(data)
            value = str(Z_L) + ' ' + str(Z_c) + ' ' + str(Z_total) + ' ' + str(I) + ' ' + str(theeta) + '\n'
            file.write(value)
            
    file.close()
    




#main programme
file_name = input()
input_data = read_file(file_name)
write_outputs(input_data)

################################################################################
# Please do not edit anything below this line.
evaluate_lab8()

##################### End of the programme #####################################