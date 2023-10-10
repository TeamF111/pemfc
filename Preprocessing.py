import pandas as pd
import matplotlib.pyplot as plt

# Load data
A1 = pd.read_csv('D:/E/Sheffield/Spring/ITP/data/FC2_Ageing_part1.csv')
A2 = pd.read_csv('D:/E/Sheffield/Spring/ITP/data/FC2_Ageing_part2.csv')
data = pd.concat([A1, A2], ignore_index=True)

# Data condense for every 9 min
data_c = [data.iloc[0]]
last_time = data_c[0]['Time']
for i, row in data.iterrows():
    if row['Time'] - last_time >= 0.1:
        data_c.append(row)
        last_time = row['Time']

data_c = pd.DataFrame(data_c)

# Plotting
plt.figure()
plt.plot(data['Time'], data['Utot'], 'b', label='original data')
plt.plot(data_c['Time'], data_c['Utot'], 'r', label='condensed data')
plt.xlabel('Time(h)')
plt.ylabel('Stack Voltage(V)')
plt.title('quasi-Dynamic Dataset')
plt.legend()
plt.show()

# Select Features
variables = data_c[['Time', 'TinH2', 'TinAIR', 'ToutH2', 'TinWAT', 'I', 'PoutAIR', 'HrAIRFC', 'ToutAIR']]

# Moving average filter
windowSize = 10
output = variables.copy()
for column in variables.columns:
    output[column] = variables[column].rolling(window=windowSize).mean()

# Plotting after Moving Average Filter (MAF)
plt.figure()
plt.plot(variables['Time'], variables['I'], 'b', label='original data')
plt.plot(output['Time'], output['I'], 'r', linewidth=1.5, label='MAF data')
plt.xlabel('Time(h)')
plt.ylabel('Stack Voltage(V)')
plt.title('Quasi-Dynamic MAF')
plt.legend()
plt.show()

# Uncomment the following line to save the output as a csv
# output.to_csv('quasi_1000_MAF_data.csv', index=False)
