print('welcome to this Computarized Dichotomous Key, we hope to help you identify your plant.')
print(
    """
     please follow each option to finally reach your prosect plant
     know that each option leads to your prosect planr.
     tanks
    """
)
start = input('where do your plant lives, type LAND for land plants and WATER for aquatic plants').lower()
if start == 'land':
    Two = input('Has green, photosynthetic abilities? Type YES or NO ').upper()
    if Two == 'YES':
        three= input('is an ANIMAL or PLANT? input ANIMAL for animal and PLANT for plant ').upper()
        if three == 'PLANT':
            print('The name of the plant is POISON GRASS ')
        elif three == 'ANIMAL':
            four = input('has long and buck teeth or has Green Fur and Big Ears? Type LBT  for long and buck teeth  or GFBE for Green Fur and Big Ears ').upper()
            if four == 'LBT':
                print('The name of the Identified Animal is \"GREEN-HAIRED RAT\"')
            elif  four == 'GFBE':
                print('The name of the identified animal is \"FUZZY HAMSTERS\"')
    elif Two == 'NO':
        FIVE = input('Has Wing? Type YES or NO ').upper()
        if FIVE == 'YES':
            SIX = input('has a red wing and blue legs or Is brown with wings? Type RWBL for red wing and blue legs or BW for brown with wings ').upper
            if SIX == 'RWBL':
                print('The name of the identified animal is \"PARASITIC MOSQUITO\"')
            elif SIX == 'BW':
                print('The name of the identified animal is \"BUTTER-ROACH\"')
        elif FIVE == 'NO':
            seven = input('Has Ten legs or has four-six legs? type 10 for ten legs or 4-6 for four-six legs ').upper()
            if seven == '10':
                EIGHT = input('is a Brown and has 10 legs? type YES or NO').upper()
                if EIGHT == 'YES':
                    print('The name of the identified animal is \"10 LEGGED FLEA\"')
                elif EIGHT == 'NO':
                    print('The computer can not identified the animal :(')
            elif seven == '4-6':
                nine = input('has four arms and red eyes or is brown with 6 legs? type 4ARE for four arms and red eyes or B6L for brown with 6 legs ').upper()
                if nine == '4ARE':
                    print('The identified animal is \"TERRESTIAL HUMANOID\"')
                elif nine == 'B6L':
                    print('The identified animal is \"COCKROACH\"')
elif start == 'water':
    Ten = input('has plant on it or not? type YES or No').upper()
    if Ten == 'YES':
        Elven = input('has four arms and red eyes or is brown with 6 legs? type 4ARE for four arms and red eyes or B6L for brown with 6 legs ').upper()
        if Elven == '4ARE':
            print('The identified animal is \"TERRESTIAL HUMANOID\"')
        elif Elven == 'B6L':
            print('The identified animal is \"COCKROACH\"')
    elif Ten == 'NO':
        Twelve = input('is an ANIMAL or PLANT? type ANIMAL for animal and PLANT for plant').upper()
        if Twelve == 'ANIMAL':
            Thirteen = input('is large and green or is orange and brown type LG for large and green and OB for orange and brown ').upper()
            if Thirteen == 'LG':
                print('The name of the identified animal is \"PHOTOSYNTHETIC SUN-BASKING SHARK\"')
            elif Thirteen == 'OB':
                print('The name of the animal is \"CHEMOSYNTHETIC GOLDFISH\"')
        elif Twelve == 'PLANT':
            fourteen = input('is a light, red and green, type LRG if yes ').upper()
            if fourteen == 'LRG':
                print('The name of the animal is \"AQUA-WHEAT\"')
            else:
                print('Sorry,  we can\'t identified this animal.')
