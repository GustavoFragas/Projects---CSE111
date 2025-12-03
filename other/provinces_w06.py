def main ():
    
    provinces_list, alberta_count = read_province_list("provinces.txt")

    print (provinces_list)
    print(f"Alberta occurs {alberta_count} times in the modified list.")

def read_province_list(filename):
    
    provinces_list = []
    count = 0
    alberta_count = 0
    
    with open(filename, "rt") as province_file:
        
        for line in province_file:
            clean_line = line.strip()
            if clean_line == "AB":
                clean_line = "Alberta"
            provinces_list.append(clean_line)
            if count == 0:
                provinces_list.pop(0)
            if count == 71:
                provinces_list.pop(70)
            
            count += 1
        
        for gline in provinces_list:
            if gline == "Alberta":
                alberta_count += 1    

        return provinces_list, alberta_count

if __name__ == "__main__":
    main()