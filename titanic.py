import json

with open('codio1.json', 'r') as file:
    data = json.load(file)

#list of ships
all_data = data.get("data", [])

def show_help():
    print("Available commands:")
    print("help                  - Show this help message.")
    print("show_countries        - List all unique countries, sorted alphabetically.")
    print("top_countries <num>   - List the top <num> countries with the most ships.")

print("Total number of ships:", len(all_data))

#name of ships

def name_of_ships():
    for ship in all_data:
        print(ship.get("SHIPNAME", "No name available"))

#all the countries of the ships
print("\nCountries of all the ships:")
for ship in all_data:
    print(ship.get("COUNTRY", "No country available"))

#all the countries of the ships without duplicates
print("\nCountries without duplicates:")
countries = {ship.get("COUNTRY", "Unknown") for ship in all_data}
for country in countries:
    print(country)


# Command 3: Show top countries with the most ships
def top_countries(all_data, num_countries):
    country_count = {}
    for ship in all_data:
        country = ship.get("COUNTRY", "Unknown")
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

    # Sort countries based on the count (from highest to lowest)
    sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)

    # Print the top N countries
    print(f"\nTop {num_countries} countries with the most ships:")
    for i in range(min(num_countries, len(sorted_countries))):
        country, count = sorted_countries[i]
        print(f"{country}: {count} ships")


# Main CLI loop
def main():
    all_data = load_data()
    while True:
        command = input("\nEnter command (type 'help' for a list of commands): ").strip()

        if command == "help":
            show_help()
        elif command == "show_countries":
            show_countries(all_data)
        elif command.startswith("top_countries"):
            try:
                _, num_str = command.split()
                num_countries = int(num_str)
                top_countries(all_data, num_countries)
            except ValueError:
                print("Error: You must specify a number after 'top_countries'.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Unknown command. Type 'help' for a list of available commands.")


if __name__ == '__main__':

print("\nNames of all the ships:")