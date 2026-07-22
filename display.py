def display_dict(prompt,data):
    if not data:
        print("No data available.")
        return
    else:
        print(f"{prompt}\n -------------------------")
        for key, value in data.items():
            
            print(f"{key} : {value}")
