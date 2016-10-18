import sys
import string


# Setup a dictionary containing 2 tuples -thanks to zip() function- with the required mapping.
# The 26 chars alphabet split into two (2x13).
# This is a nice way to SHIFT letters by the required 13 places.
# Added additional character conversion: ' ' to '_' and vice versa.
CHAR_MAP = dict(zip(
 	string.ascii_lowercase+' '+'_',
    string.ascii_lowercase[13:26] + string.ascii_lowercase[0:13]+'_'+' '
    )
)

# A function to return the pair-character from CHAR_MAP.
def rotate13_letter(letter):
    """
    Return the 13-char rotation of a letter.
    """

    do_upper = False                    # Reset Flag
    if letter.isupper():                # Set Flag if letter is in UpperCase
        do_upper = True                 
    letter = letter.lower()             # Set letter to LowerCase
    if letter not in CHAR_MAP:          # Return 'as-is' if letter is outside the 26 alphabet
            return letter
    else:
       letter = CHAR_MAP[letter]        # Return the pair-character from dict
       if do_upper:                     # Check Flag and convert back to UpperCase if required
           letter = letter.upper()
    return letter
if __name__ == '__main__':
    for char in sys.argv[1]:
        sys.stdout.write(rotate13_letter(char))
    sys.stdout.write('\n')

# The CHAR_MAP dict look-up process is done in LowerCase mode
# However, Flag (whether uppercase) is checked and convert to uppercase accordingly as necessary