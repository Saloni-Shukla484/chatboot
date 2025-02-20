import csv

csv_file = "Financials.csv"

# CSV file open karke data read karna
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = [col.strip() for col in reader.fieldnames]  # Column names ko strip karna

    # User se column choose karne ka kehna
    print("\nAvailable columns to search:")
    for index, field in enumerate(fieldnames, 1):
        print(f"{index}. {field}")
    
    choice = int(input("\nEnter the number of the column you want to search in: "))
    if choice < 1 or choice > len(fieldnames):
        print("\n❌ Invalid choice. Please run again and select a valid number.")
        exit()
    
    search_column = fieldnames[choice - 1]  # User ka chosen column
    search_value = input(f"Enter the value to search in '{search_column}': ").strip().lower()

    found = False
    print("\n🔹 Matching Records 🔹")
    for row in reader:
        row = {key.strip(): value.strip() for key, value in row.items()}  # Strip spaces
        
        if row.get(search_column, "").lower() == search_value:
            found = True
            print("\n---------------------------------")
            for key, value in row.items():
                print(f"{key}: {value}")
    
    if not found:
        print("\n❌ No matching records found.")