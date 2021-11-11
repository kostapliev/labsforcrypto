
def tsesar():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    step = 5
    text = input("Input anything").upper()
    result = ''
    for i in text:
        ind = letters.find(i)
        newind = ind + step
        if i in letters:
            result += letters[newind]
        else:
            result += i
    print(result)

def tsesar_deshifr():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smeshenie = 5
    text = input("Input anything").upper()
    result = ''

    for i in text:
        ind = letters.find(i)
        newind = ind - smeshenie
        if i in letters:
            result += letters[newind]
        else:
            result += i
    print(result)

def atbash():
    letters = [chr(x) for x in range(65, 91)]
    letters_r = [x for x in letters]
    letters_r.reverse()

    text = input("Input anything").upper()
    result = ""
    for i in text:
        for j,l in enumerate(letters):
            if i == l:
                result += letters_r[j]
    print(result)

def atbash_desh():
    letters = [chr(x) for x in range(65, 91)]
    letters_r = [x for x in letters]
    letters_r.reverse()

    text = input("Input anything").upper()
    result = ""
    for i in text:
        for j, l in enumerate(letters_r):
            if i == l:
                result += letters[j]
    print(result)

def main():
    while True:
        try:
            command = int(input("Choose the function: 1 - Tsesar; 2 -Tsesar decrypt; 3 - atbash; 4 - atbash decrypt "))
            if(command==1):
                tsesar()
            elif command==2:
                tsesar_deshifr()
            elif command==3:
                atbash()
            elif command==4:
                atbash_desh()
            else:
                print("I cant understand your command =(")
        except:
            print("ERROR!")



if __name__ == "__main__":
    main()
