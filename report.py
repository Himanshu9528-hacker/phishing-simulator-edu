def generate_report():
    with open("logs.txt") as f:
        creds = f.readlines()
    print(f"Total phishing attempts: {len(creds)}")
