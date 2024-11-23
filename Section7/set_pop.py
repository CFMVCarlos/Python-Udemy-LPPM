from Section7.set_remove import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    #! pop() removes and returns an arbitrary element from the set
    patient = trial_patients.pop()
    presciption = patients[patient]
    print(f"Patient: {patient:^8} | Prescription: {presciption}")
