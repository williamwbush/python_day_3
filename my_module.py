def house_area():
    floors = list(range(int(input('How many floors does your house have?: '))))
    area = 0

    for floor in floors:
        if floors.index(floor) == 0:
            length = input(f'What is the length of floor #{floors.index(floor) + 1}? \nPlease use the same unit of length for all measurements.\n')
        else:
            length = input(f'What is the length of floor #{floors.index(floor) + 1}?: ')
        width = input(f'What is the width of floor #{floors.index(floor) + 1}?: ')

        length_words = length.split()
        for word in length_words:
            if word.isdigit() == True:
                length_num = int(word)      
            if word.isdigit() == False:
                unit_of_length = word   
        
        width_words = width.split()
        for word in width_words:
            if word.isdigit() == True:
                width_num = int(word)
        
        area += length_num * width_num
    
    print(f'The area of your house is {area} {unit_of_length}\u00b2.')

def circle_circum():
    from math import pi

    r = int(input('What is the radius of the circle?: '))
    circum = 2 * pi * r
    print(f'The area of the circle is {circum}.')




