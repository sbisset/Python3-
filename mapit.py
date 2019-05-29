import webbrowser, sys 
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)
else:
    # Get address from clipboard.
    print("Usage:", sys.argv[0],"ADRESS")
    exit

