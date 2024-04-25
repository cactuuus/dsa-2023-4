input = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
output = ""

for letter in input:
    if letter.isalpha():
        offset = ord("a") if letter.islower() else ord("A")
        letter = chr((ord(letter) + 13 - offset) % 26 + offset)
    output += str(letter)

print(output)