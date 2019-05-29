import webbrowser, sys 
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)
    webbrowser.open('https://www.premierinn.com/gb/en/search.html?searchModel.searchTerm=' + address )
else:
    # Get address from clipboard.
    print("Usage:", sys.argv[0],"ADDRESS")
    exit 

