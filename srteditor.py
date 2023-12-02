with open ("/Users/orhantalhasmac/Desktop/srt.txt", "r" ) as x:
    str = x.read()

str = str.replace("«", "ç")
str = str.replace ("˝", "ı")
str = str.replace("¸", "ü")
str = str.replace("ˆ", "ö")
str = str.replace("", "ğ")
str = str.replace("˛", "ş")
str = str.replace("÷", "Ö")
str = str.replace("Á" , "ç")
str = str.replace("›", "İ")
str = str.replace("‚", "a")

with open ("/Users/orhantalhasmac/Downloads/srtedited.srt", "w") as x:
    x.write(str)


