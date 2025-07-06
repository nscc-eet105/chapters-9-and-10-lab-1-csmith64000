#Chris smith
#Chapter 9&10 Lab
#07/01/2025

def main():

    name =input("Enter your name: ")

    formatted = ("Invalid name format")


    if ',' in name:
            parts = name.split(",")
            if len(parts) == 2:
                last = parts[0].strip().title()
                first = parts[1].strip().title()
                formatted = f"{last}, {first}"

    else:
            parts = name.strip().split()
            if len(parts) == 2:
                first = parts[0].title()
                last = parts[1].title()
                formatted = f"{last}, {first}"
            

    print(formatted)

    

main()        

            
