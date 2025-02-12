import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7


#taking 3 user input for the file names which has the collection of data 
MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.



# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    file = open(file_name, 'r')     
    details = file.read().split()
    file.close()
    for i in range(1, len(details), 2) :
        speed.append(int(details[i]))
################## YOUR CODE ENDS HERE. ########################################     
    return speed



# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    speed_ms_list = []
    speed_list = get_speed(filename)
    for val in speed_list :
       value = (val * 5) / 18
       speed_ms_list.append(value)
    
    return speed_ms_list
################## YOUR CODE ENDS HERE. ########################################



# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.    
    for j in range(len(speeds)-1) :
        val = round(((speeds[j+1] - speeds[j]) / 0.1 ), 2)
        acceleration.append(val)
################## YOUR CODE ENDS HERE. ########################################
    return acceleration



######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files

#calling the created functions to calculate the acceleration list
acceleration_01 = get_acceleration(convert_kmph_to_ms(MODEL_1_INPUT_FILE))
acceleration_02 = get_acceleration(convert_kmph_to_ms(MODEL_2_INPUT_FILE))
acceleration_03 = get_acceleration(convert_kmph_to_ms(MODEL_3_INPUT_FILE))

#list with time for plotting the graph 
time_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      


#plotting lines for the graph of the given data sets
plt.plot(time_list, acceleration_01 , label='model_1')
    
plt.plot(time_list, acceleration_02 , label='model_2')

plt.plot(time_list, acceleration_03 , label='model_3')



        
# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()

#function to find the maximum value of list
def maximum(list) :
    max = list[0]
    for val in range(1,len(list)) :
        if max < list[val] :
            max = list[val]
    return max


#create a new file for printing the outputs
output_file = open("max_acceleration.txt", 'w')

#finding maximum value from list using "maximum()" function
max_value_01 = maximum(acceleration_01)
max_value_02 = maximum(acceleration_02)
max_value_03 = maximum(acceleration_03)
max_list = [max_value_01, max_value_02, max_value_03]
#write the values to the output file
for k in range(len(max_list)) :
    value = 'model' + str(k+1) + ' ' + str(max_list[k]) + '\n'
    output_file.write(value)

output_file.close()


################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################



