# function for adding a new patient
def adding_patient(patients):
    name = input("Input patient's name: ")
    age = input("Input patient's age: ")
    illness = input("Input patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print(f"Patient {name} added successfully!")

#function to display patients
def display_patients(patients):
    if not patients:
        print("No patients to display.")
    else:
        for i, patient in enumerate(patients, start=1):
            print(f"Patient {i}:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Illness: {patient['illness']}")

#function to search patient by name
def search_patient(patients):
    name = input("Enter the name of the patient to search: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Illness: {patient['illness']}")
            return
    print(f"No patient found with the name {name}.")

#function to delete a patient
def delete_patient(patients):
    name = input("Enter the name of the patient to delete: ")
    for i, patient in enumerate(patients):
        if patient['name'].lower() == name.lower():
            del patients[i]
            print(f"Patient {name} deleted successfully!")
            return
    print(f"No patient found with the name {name}.")

#loop to keep the program running
def main():
    patients = []
    while True:
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Delete a patient by name")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            adding_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            delete_patient(patients)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
