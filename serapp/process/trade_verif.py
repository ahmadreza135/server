def verification(request):
    
    sarrafi = request.POST["sarrafi"]
    if sarrafi == "binance":
        pass
    elif sarrafi == "":
        pass
    else:
        return "sarrafi name is not valid"    


    return False
