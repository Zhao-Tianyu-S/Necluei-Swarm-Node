from solana.keypair import Keypair
import os

# File to save the wallet details
WALLET_FILE = "necluei_wallet.json"

# Function to create a new Solana wallet
def create_wallet():
    # Generate a new Keypair
    keypair = Keypair()
    
    # Extract the public and private keys
    public_key = str(keypair.public_key)
    private_key = list(keypair.secret_key)

    # Save wallet details to a JSON file
    wallet_data = {
        "public_key": public_key,
        "private_key": private_key
    }

    with open(WALLET_FILE, "w") as f:
        import json
        json.dump(wallet_data, f, indent=4)

    print(f"New Solana wallet created and saved to {WALLET_FILE}")
    print(f"Public Key: {public_key}")
    print("Keep the private key secure and do not share it!")

# Function to load an existing wallet
def load_wallet():
    if not os.path.exists(WALLET_FILE):
        print(f"Wallet file {WALLET_FILE} not found. Please create a wallet first.")
        return None

    with open(WALLET_FILE, "r") as f:
        import json
        wallet_data = json.load(f)

    print("Wallet loaded successfully.")
    print(f"Public Key: {wallet_data['public_key']}")
    return wallet_data

# Main execution
def main():
    print("1. Create a new wallet")
    print("2. Load an existing wallet")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        create_wallet()
    elif choice == "2":
        wallet_data = load_wallet()
        if wallet_data:
            print("Wallet is ready for use.")
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
