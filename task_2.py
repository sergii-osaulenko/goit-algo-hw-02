from collections import deque

def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Ігнорує регістр і пробіли (можна легко розширити до ігнорування пунктуації).
    """
    # Нормалізація: лише алфанумеричні символи, нижній регістр
    normalized = []
    for ch in text:
        if ch.isalnum():      # ігнорувати пробіли та пунктуацію
            normalized.append(ch.lower())

    char_deque = deque(normalized)  # додати всі символи до deque

    # Порівняння символів з обох кінців
    while len(char_deque) > 1:
        left = char_deque.popleft()  # зліва
        right = char_deque.pop()     # справа
        if left != right:
            return False

    return True  # якщо всі пари однакові

if __name__ == "__main__":
    s = input("Введіть рядок: ")
    if is_palindrome(s):
        print("Це паліндром.")
    else:
        print("Це не паліндром.")