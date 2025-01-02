from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from spl.token.async_client import AsyncToken
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import initialize_mint, create_account, mint_to
import asyncio

# Define token metadata
TOKEN_NAME = "I Created A Token"
SYMBOL = "Necluei"
DESCRIPTION = "A token created by Necluei to celebrate its journey of learning and innovation."
WEBSITE = "https://github.com/Zhao-Tianyu-S/Necluei-Swarm-Node"
Twitter = "https://x.com/necluei"
Token_IMG = ".\necluei.img"
# Solana cluster RPC endpoint
SOLANA_CLUSTER_URL = "https://api.devnet.solana.com"

# Replace with your private key (JSON array format) to authorize token creation
PRIVATE_KEY = "[Your Private Key Here]"

# Main function to create the token
async def create_pump_fun_token():
    async with AsyncClient(SOLANA_CLUSTER_URL) as client:
        # Load private key and derive wallet address
        from solana.keypair import Keypair
        keypair = Keypair.from_secret_key(bytes(eval(PRIVATE_KEY)))
        wallet_address = keypair.public_key

        print(f"Creating token with wallet: {wallet_address}")

        # Create mint account
        mint_account = Keypair()
        print(f"Mint account: {mint_account.public_key}")

        # Create instructions for token initialization
        transaction = Transaction()

        # Allocate mint account space and initialize
        transaction.add(
            await initialize_mint(
                program_id=TOKEN_PROGRAM_ID,
                mint=mint_account.public_key,
                decimals=DECIMALS,
                mint_authority=wallet_address,
                freeze_authority=wallet_address,
            )
        )

        # Create associated token account for wallet
        associated_token_account = await AsyncToken.create_associated_token_account(
            payer=keypair,
            owner=wallet_address,
            mint=mint_account.public_key
        )

        # Add instruction to mint tokens
        transaction.add(
            mint_to(
                mint=mint_account.public_key,
                dest=associated_token_account,
                mint_authority=wallet_address,
                amount=TOTAL_SUPPLY,
                program_id=TOKEN_PROGRAM_ID
            )
        )

        # Send transaction
        response = await client.send_transaction(transaction, keypair, opts=TxOpts(skip_preflight=True))
        print("Transaction response:", response)

        print("Token successfully created!")
        print(f"Token Name: {TOKEN_NAME}")
        print(f"Symbol: {SYMBOL}")
        print(f"Description: {DESCRIPTION}")
        print(f"Decimals: {DECIMALS}")
        print(f"Total Supply: {TOTAL_SUPPLY}")
        print(f"Mint Address: {mint_account.public_key}")

if __name__ == "__main__":
    asyncio.run(create_pump_fun_token())
