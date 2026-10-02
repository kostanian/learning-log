def main():
    inp=input("What time is it? ")
    if 7<=convert(inp)<=8:
        print("breakfast time")
    elif 12<=convert(inp)<=13:
        print("lunch time")
    elif 18<=convert(inp)<=19:
        print("dinner time")

def convert(time):
    hours,mins=time.split(":")
    min_chaanged=int(mins)/60
    final_time=int(hours)+min_chaanged
    return final_time

if __name__ == "__main__":
    
    
    main()

