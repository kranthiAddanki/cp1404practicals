

COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}
colour_name = input("Enter Colour name: ").lower()
# while colour_name != '':
#     if colour_name in COLOUR_CODES:
#         print( "colour_code is", COLOUR_CODES[colour_name] )
#     else:
#         print( "Enter a valid colour name" )
#     colour_name = input("Enter Colour name: ").lower()

# version_2
while colour_name != '':
# using get method for program not to crash when an invalid entry is given as input
# if the key is not found, get method returns none
    print( f"colour_code is: {COLOUR_CODES.get(colour_name)}" )
    colour_name = input("Enter Colour name: ").lower()