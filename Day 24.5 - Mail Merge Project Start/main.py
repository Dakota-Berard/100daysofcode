#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()

print(names)

for name in names:
    with open(f"Output/ReadyToSend/{name}_letter.txt", mode="w") as file:
        file.write(f'''Dear {name},
        
You are invited to my birthday this Saturday.
        
Hope you can make it!
        
Angela''')

