import sys

tokens_value={
'.-'      : 'A', #morse table
'-...'    : 'B',
'-.-.'    : 'C',
'-..'     : 'D',
'.'       : 'E',
'..-.'    : 'F',
'--.'     : 'G',
'....'    : 'H',
'..'      : 'I',
'.---'    : 'J',
'-.-'     : 'K',
'.-..'    : 'L',
'--'      : 'M',
'-.'      : 'N',
'---'     : 'O',
'.--.'    : 'P',
'--.-'    : 'Q',
'.-.'     : 'R',
'...'     : 'S',
'-'       : 'T',
'..-'     : 'U',
'...-'    : 'V',
'.--'     : 'W',
'-..-'    : 'X',
'-.--'    : 'Y',
'--..'    : 'Z',

'-----'   : '0', #Numbers
'.----'   : '1',
'..---'   : '2',
'...--'   : '3',
'....-'   : '4',
'.....'   : '5',
'-....'   : '6',
'--...'   : '7',
'---..'   : '8',
'----.'   : '9',

'.-.-.-'  : '.', # Punctuation
'--..--'  : ',',
'..--..'  : '?',
'.----.'  : '\'',
'-.-.--'  : '!',
'-..-.'   : '/',
'-.--.'   : '(',
'-.--.-'  : ')',
'.-...'   : '&',
'---...'  : ':',
'-.-.-.'  : ';',
'-...-'   : '=',
'.-.-.'   : '+',
'-....-'  : '-',
'..--.-'  : '_',
'.-..-.'  : '"',
'...-..'  : '$',
'.--.-.'  : '@',
'..-.-'   : '¿',
'--...-'  : '¡',
' '       : ' ',
}


def convert(line):
    inv_tokens_value = {v: k for k, v in tokens_value.items()}
    morse_line = ""

    for letter in line:
        morse_line += inv_tokens_value[letter.capitalize()] + " "

    return morse_line

def main():

    source = "input.php"
    with open(source) as temp_file:
        lines = [line.rstrip('\n') for line in temp_file]

    morse_out = []
    for line in lines:
        morse_line = convert(line)
        if morse_line != "":
            morse_out.append(morse_line)

    # for out in morse_out:
    #     print(out)



    f = open('input_morse.php','w')
    for out in morse_out:
        print(out, file=f)
    f.close()




if __name__== "__main__":
  main()
