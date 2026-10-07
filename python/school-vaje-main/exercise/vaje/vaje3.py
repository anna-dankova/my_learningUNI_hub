def validate_password(password: str) -> str:
    password = password.strip()

    checks = [
        (len(password) < 8, "Пароль слишком короткий"),
        (len(password) > 15, "Пароль слишком длинный"),
        (not any(ch.isupper() for ch in password), "Нужна хотя бы одна заглавная буква"),
        (not any(ch.islower() for ch in password), "Нужна хотя бы одна строчная буква"),
        (not any(ch.isdigit() for ch in password), "Нужна хотя бы одна цифра"),
        (not any(not ch.isalnum() for ch in password), "Нужен хотя бы один специальный символ"),
    ]

    for condition, message in checks:
        if condition:
            return message

    return "Пароль подходит"

def main() -> None:
    print("Правила: 8–15 символов, минимум одна заглавная, строчная, цифра и спецсимвол.")
    password = input("Введите пароль: ")
    print(validate_password(password))

if __name__ == "__main__":
    main()