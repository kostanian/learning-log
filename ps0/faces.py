
def convert(text):
    converted=text.replace(":(", "🙁").replace(":)", "🙂")
    return converted
    
def main():
    inp=convert(input())
    print(inp)

main()