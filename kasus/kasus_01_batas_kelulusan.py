
def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


print("Status nilai 75:", status_lulus(75))
print("Status nilai 60:", status_lulus(60))
print("Status nilai 59:", status_lulus(59))
