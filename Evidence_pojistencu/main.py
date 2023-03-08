from client_administration import add_person, print_people, find_person


# Print the header
print("╔════════════════════════════════════════╗")
print("║     Vítejte v evidenci pojištění       ║")
print("╠════════════════════════════════════════╣")

# Print the menu options
print("║  1. Přidat klienty                     ║")
print("║  2. Zobrazit všechny klienty           ║")
print("║  3. Vyhledání podle jména a příjmení   ║")
print("║  4. Ukončit                            ║")
# Print the footer
print("╚════════════════════════════════════════╝")

# Loop until the user quits
while True:
    # Get the user's choice
    choice = input("Vyberte operaci: ")

    # Process the user's choice
    if choice == "1":
        add_person()
    elif choice == "2":
        print_people()
    elif choice == "3":
        find_person()
    elif choice == "4":
        break
    else:
        print("Neznám tenhle příkaz, zkus to znovu")


    # Wait for the user to continue
    input("Pokračujte libovolnou klávesou")