# -*- coding: utf-8 -*-
import Image
import urllib2 as urllib
from io import BytesIO
from time import clock


DRK_TO_LGT = \
           ['M',
            'Q',
            'E',
            'Z',
            'G',
            '0',
            "C",
            '¢',
            'n',
            'º',
            "ï",
            "r",
            'i',
            '=',
            "‡",
            "+",
            "»",
            ":",
            "-",
            "¬",
            "·",
            "‹",
            " "]

#                                                                TESTING
# compare two characters
def compare_chars():

    while True:

        char1 = raw_input("Enter first character: ")
        char2 = raw_input("Enter second character: ")

        for i in range(20):
            if i < 3 or i > 15:
                print char1*30
            elif i < 6 or i > 12:
                print (char1*5)+(char2*20)+(char1*5)
            else:
                print (char1*5)+(char2*5)+(char1*10)+(char2*5)+(char1*5)

        print

        again = raw_input("Again? Enter 'n' to stop. ")
        if again.lower() == 'n':
            break

        print

# compare two characters as squares
def squares():

    while True:
        print

        char1 = raw_input("First square: ")
        char2 = raw_input("Second square: ")

        for i in range(20):
            print char1*30+"\t"+char2*30

        print

        again = raw_input("Again? Enter 'n' to stop. ")
        if again.lower() == 'n':
            break

# view the current spectrum
def spectrum():
    for c in DRK_TO_LGT:
        print c*20
#
#                                                           END TESTING

# take a url and return it as an Image
def query_and_fetch():

    choice = raw_input("Enter a valid image URI: ")
    print

    if choice.lower() == 'q':
        return False

    try:
        data = urllib.urlopen(choice)
        f = BytesIO(data.read())
        img = Image.open(f)
        return img

    except:

        try:
            print "trying to open as path"
            img = Image.open(choice)
            return img

        except:
            print "something went wrong"
            return False

# convert img data into an easier to use format
def get_pixels(img, width, height):
    
    data = list(img.getdata())
    
    return [data[i * width:(i + 1) * width] for i in xrange(height)]

# home for the ascii image
def make_ascii_frame(width, height, zoom):
    
    asc_width  = int(width/zoom)
    asc_height = int(height/zoom)
    
    return [[0 for i in xrange(asc_width)] for j in xrange(asc_height)]

# converts RGB into grayscale
#   it so happens that the "gray" version of a color is not
#   simple their average.
#   green carries much more weight than red, which in turn carries more
#   weight than blue, hence the factors.
def grayscale(pixel):
    return (pixel[0] * 0.299) + (pixel[1] * 0.587) + (pixel[2] * 0.114)

# converts the image to grayscale and maps the values to the ascii array
def gray_mapper(pixels, ascii, asc_width, asc_height, zoom):
    
    for row in xrange(len(pixels)):
        for col in xrange(len(pixels[row])):
            
            if row/zoom < asc_height and col/zoom < asc_width:
                
                gray = grayscale(pixels[row][col])
                ascii[int(row/zoom)][int(col/zoom)] += gray

#
# grayscale formula!
#
# gray == ascii[row][col] * (len(DRK_TO_LGT)-1)
#         -------------------------------------
#                   zoom^2 * 255.0
#
# const == (len(DRK_TO_LGT)-1)
#          -------------------
#            zoom^2 * 255.0
#


# maps the grayscale values in ascii[][] to characters
def ascii_mapper(ascii, zoom):
    const = pow(zoom, -2) * (len(DRK_TO_LGT)-1) / 255.0

    for row in xrange(len(ascii)):
        for col in xrange(len(ascii[row])):
            
            ascii[row][col] = DRK_TO_LGT[int(ascii[row][col] * const)]



def write_image(chars):
    name = str(clock()) + '.txt'
    f = open(name,'w')
    for line in chars:
        f.write(''.join(line))
        f.write('\n')
    f.close()

def main():

    active = True

    while active:

        zoom = 3
        img = query_and_fetch()
        t1 = clock()
        width, height = img.size
        pixels = get_pixels(img, width, height)
        same_image = True

        while same_image:

            ascii = make_ascii_frame(width, height, zoom)
            gray_mapper(pixels, ascii, width/zoom, height/zoom, zoom)
            ascii_mapper(ascii, zoom)
            print "\n".join([''.join(map(str,row)) for row in ascii])

            bad = True
            while bad:
                print clock()-t1
                opt = raw_input("""
'zin'  - zoom in
'zout' - zoom out
'exp'  - export this image
'new'  - new image
'quit' - exit program

>> """)

                print

                if opt == 'zin':
                    if zoom == 1:
                        print "Can't zoom in any more!\n"
                    else:
                        zoom -= 1
                        bad = False

                elif opt == 'zout':
                    zoom += 1
                    bad = False

                elif opt == 'exp':
                    write_image(ascii)
                    print "Done!"

                elif opt == 'new':
                    bad, same_image = False, False

                elif opt == 'quit':
                    print 'Bye\n'
                    bad, same_image, active = False, False, False

                else:
                    print "Huh?\n"

if __name__ == "__main__": main()
