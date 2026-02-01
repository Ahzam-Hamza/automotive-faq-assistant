with open("data/car_manual.txt", "r") as file:
    manual_text = file.read().lower()

manual_sections = {
    "engine oil": "Engine oil should be changed every 10,000 km or 6 months using SAE 5W-30 oil.",
    "tire pressure": "Recommended tire pressure is 32 PSI for front tires and 30 PSI for rear tires.",
    "battery": "The car battery typically lasts between 3 to 5 years under normal usage.",
    "warranty": "The vehicle comes with a warranty of 3 years or 100,000 km."
}

question = input("Ask a question about your car: ").lower()

def retrieve_section(question, sections):
    for key in sections:
        if key in question:
            return key, sections[key]
    return None, None

section, answer = retrieve_section(question, manual_sections)

print("\nAnswer:")
if answer:
    print(answer)
    print(f"Source: {section.title()} section")
else:
    print("Information not available in the manual.")

