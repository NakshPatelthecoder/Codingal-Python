country_code = {"India": "0091",
                "Austrailia":"0025",
                "Nepal": "00977"}

# Search dictionary for country code of India
print("The Country Code for India is :")
print(country_code.get("India",))

#Search dictionary for country code of Japan
print("Country code for Japn is :")
print(country_code.get("Japan", "Not Found"))