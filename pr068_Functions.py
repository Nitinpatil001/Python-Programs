#string functions
st="computer network"
print(st)
print(st.capitalize())
print(st.casefold())
st1="ram09"
print(st1)
print(st1.center(10,'*'))
print(st.count('o'))
print(st.count("work"))
print(st.count("o",3))
print(st.count("o",3,9))
print(st.endswith("work"))
print(st.startswith("comp"))
print(st.find("o"))
print(st.find("z"))#if not available displays -1
print(st.find("put"))
print(st.index("o"))
print(st.index("z"))#throw error msg
print(st.isalnum())
print(st1.isalnum())
print(st1.isalpha())
print(st1.isascii())
print(st1.isdecimal())
print(st1.isdigit())
print(st1.isidentifier())
print(st.isidentifier())
print(st1.islower())
print(st1.isupper())
print(st1.isnumeric())
print(st1.isprintable())
print(st1.isspace())
print(st.isspace())
st2="Computer Network"
print(st.istitle())
print(st2.istitle())
print(st.upper())
st3="RAM"
print(st3.lower())
print(st.replace("o","z"))
print(st.replace("put","get"))




