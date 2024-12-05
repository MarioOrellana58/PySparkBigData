def fetch_bananas_from_cloud(api_key):
    print(f"Authenticating to BananaCloud with API key: {api_key[:4]}***")
    if api_key == "1234":
        print("Access Denied: Too predictable!")
        return None
    bananas = ["🍌" for _ in range(5)]
    print(f"Fetched {len(bananas)} bananas.")
    return bananas

def process_bananas(bananas):
    if not bananas:
        print("No bananas to process. What are we even doing here?")
        return []
    print("Peeling bananas...")
    peeled = [banana.strip("🍌") + "🥳" for banana in bananas]
    print(f"Bananas processed into: {peeled}")
    return peeled

def deploy_bananas_to_prod(bananas):
    if "🥳" not in "".join(bananas):
        print("ERROR: These bananas are not party-ready!")
        return False
    print("Deploying bananas to production...")
    print("...Bananas successfully served with ice cream 🍨!")
    return True

# Main function (because everyone loves a main)
if __name__ == "__main__":
    print("🚀 Launching the Banana Pipeline!")
    api_key = input("Enter your super secure API key: ")
    bananas = fetch_bananas_from_cloud(api_key)
    party_bananas = process_bananas(bananas)
    success = deploy_bananas_to_prod(party_bananas)

    if success:
        print("🎉 All systems go. Banana pipeline is live!")
    else:
        print("💥 Pipeline failure. No ice cream today. 🍦")
