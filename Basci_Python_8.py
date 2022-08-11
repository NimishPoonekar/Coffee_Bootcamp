#Write a Python program to create a histogram from a given list of integers.

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([7,5,2,4])
