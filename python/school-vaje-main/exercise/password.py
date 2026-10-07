def validate_password(password: str) -> str:
    password = password.strip()

    checks = [
        (len(password) < 8, "password is too short"),
        (len(password) > 15, "password is too long"),
        (not any(ch.isupper() for ch in password), "no uppercase letter"),
        (not any(ch.islower() for ch in password), "no lowercase letter"),
        (not any(ch.isdigit() for ch in password), "no number"),
        (not any(not ch.isalnum() for ch in password), "no special character"),
    ]

    for condition, message in checks:
        if condition:
            return message

    return "password is okay"


def main() -> None:
    print("welcome to password game")
    print("Rules: 8–15 characters, at least one uppercase, lowercase, digit, special.")
    password = input("Enter your password: ")
    print(validate_password(password))


if __name__ == "__main__":
    main()


