

def line(katz_deli):
    if len(katz_deli) >= 1:
        new_list = ["The line is currently:"]
        for index, person in enumerate(katz_deli):
            sentence = f"{index + 1}. {person}"
            new_list.append(sentence)
        print(" ".join(new_list))
    else:
        print("The line is currently empty.")    
    

def take_a_number(list, name):
    list.append(name)
    if len(list) == 1:
        print(f"Welcome, {name}. You are number 1 in line.")
    else:
        print(f"Welcome, {name}. You are number {len(list)} in line.")
    

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {list[0]}.")
        del list[0]
    

