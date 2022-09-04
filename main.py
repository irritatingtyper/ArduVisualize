import functions

print("Welcome to the ArduVisualize data collecting procedure.\n\nPlease enter the session name.")
sessionName = input("> ")
print("\nDescribe this project session:")
description = input("> ")
print("\nHow many data are you tring to collect in a single line? (Max is 3 data types for now)")
dataNum = int(input("> "))
print ("\nHow many lines would you like to collect?")
frequency = int(input("> "))
frequency += 1 #frequency = frequency + 1
print("\nWhat type of graph would you like to use?")
graph = input("> ")
print("\nEnter the port of your device.")
port = input("> ")
print("\nEnter the baudrate of your device.")
bRate = int(input("> "))

print("Now beginning data collecting procedure.")
functions.dataCollection(port, bRate, frequency)
confirmation = input("Press any button if you have checked the CSV file.")
functions.prepareData(graph, sessionName)
print("Data collection procedure completed. Please open index.html to view it. Thank you.")