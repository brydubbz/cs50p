def main():
    sadtxt = input("What text needs more personality? ")
    convert(sadtxt)

def convert(sadtxt):
    newtext = sadtxt.replace(":)", "😊").replace(":(", "☹️")
    print(newtext)
main()