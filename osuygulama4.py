import os
try:
    os.mkdir("elma1")

except FileExistsError:
    print("Aynı isminle dosyan var!")
    