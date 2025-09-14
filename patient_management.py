def search_patients_by_disease(patients, disease):
    matching_patients = []
    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            matching_patients.append(patient["Name"])
    return matching_patients

num_patients = int(input("Enter number of patients: "))
patients = []

for i in range(num_patients):
    print(f"\nEnter details for Patient {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    patients.append({
        "Name": name,
        "Age": age,
        "Disease": disease
    })

search_disease = input("\nEnter disease to search: ")
result = search_patients_by_disease(patients, search_disease)

if result:
    print(f"\nPatients with {search_disease}: {result}")
else:
    print(f"\nNo patients found with {search_disease}")