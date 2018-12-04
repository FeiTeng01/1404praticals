def main():
    color_code = {'azure1':'#f0ffff','azure4':'#838b8b','brown1':'#ff4040','CadetBlue1':'#98f5ff'}

    color = str(input("Please enter the name of color"))
    if color in color_code:
        print("The code of color is", color_code[color])
    else:
        print("invalid color name")

main()