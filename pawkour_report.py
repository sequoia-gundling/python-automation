"""
Princess Pawkour Crystal Tracker

Reads crystal collection data
and generates a royal report.
"""

# -------------------------
# FUNCTION
# -------------------------

def load_crystals(filename):

    crystal_data = {}

    try:

        with open(filename, "r") as file:

            for line in file:

                cat_name, crystals = line.strip().split(",")

                crystal_data[cat_name] = int(crystals)

    except FileNotFoundError:

        print("⚠️ Crystal registry not found.")

    return crystal_data


# -------------------------
# LOAD FILE
# -------------------------

records = load_crystals("yarn_crystals.txt")

total_crystals = sum(records.values())

print("\n🐱 PRINCESS PAWKOUR REPORT 🐱")
print("--------------------------------")

for cat, crystals in records.items():

    print(
        f"{cat} collected {crystals} Yarn Crystals."
    )


print("--------------------------------")
print(f"Total Crystals Collected: {total_crystals}")


# -------------------------
# SAVE REPORT
# -------------------------

with open("royal_report.txt", "w") as report:

    report.write("Princess Pawkour Crystal Report\n")
    report.write("===============================\n\n")

    for cat, crystals in records.items():

        report.write(
            f"{cat}: {crystals} crystals\n"
        )

    report.write(
        f"\nTotal Crystals: {total_crystals}"
    )


print("\n✅ Royal report generated.")
