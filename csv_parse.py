def read_csv(csv_file):
    data = {}
    i=0
    file = open(csv_file)
    if FileNotFoundError:
        print(f"File {csv_file} not found.")
        return None
    if not file:
        print(f"File {csv_file} is empty.")
        return None
    if not file.readable():
        print(f"File {csv_file} is not readable.")
        return None
    for line in file:
        stuff = line.strip()       
        data.update({i:stuff})
        i+=1
    return data