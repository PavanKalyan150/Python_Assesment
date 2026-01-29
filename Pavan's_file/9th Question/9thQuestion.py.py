import requests
def fetch_pet_inventory():
    url = "https://petstore.swagger.io/v2/store/inventory"
    print("Fetching pet store inventory...")
    response = requests.get(url)
    if response.status_code == 200:
        inventory = response.json()
        print("\nPet Store Inventory:")
        for status, count in inventory.items():
            print(f"{status.capitalize()}: {count} pets")
    else:
        print("Failed to fetch inventory data")
if __name__ == "__main__":
    fetch_pet_inventory()