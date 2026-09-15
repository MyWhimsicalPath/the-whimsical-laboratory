specimen_name = input("Name:")
location_found = input("Location:")
danger_level = int(input("Danger Level:"))
max_danger_level = 10
remaining_danger = max_danger_level - danger_level


print("SPECIMEN INTAKE")
print("Name:", specimen_name)
print("Location:", location_found)
print("Danger Level", danger_level)
print("Remaining Danger Capacity:", remaining_danger)

print("ARCHIVE LABEL:")
print(f"{specimen_name} - {location_found} - Danger {danger_level}")
