import pandas as pd

def find_decreasing_peaks(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    last=0
    current=0
    future=0
    framesSinceLast=0
    amps=""
    # Iterate over each row in the DataFrame
    for row in df.iterrows():
        future=row[1]
        if current>future and current>last:
            amps+=(str(framesSinceLast)+","+str(current)+"\n")
            framesSinceLast=0
        last=current
        current=future
        framesSinceLast+=1
    return(amps)

# Provide the path to the "C0019Output.csv" file
csv_file_path = 'C0019Output.csv'
outputFile = open("outputFile.csv", "w")
# Call the function with the CSV file path
outputFile.write(find_decreasing_peaks(csv_file_path))
outputFile.close()
