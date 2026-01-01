from queue import Queue
import time

# Глобальна черга заявок
requests_queue = Queue()
request_id = 0  # Лічильник для унікальних ID

def generate_request():
    """Створює нову заявку і додає її до черги."""
    global request_id
    request_id += 1
    request = f"Request #{request_id}"
    requests_queue.put(request)  # Додати в чергу
    print(f"Згенеровано та додано до черги: {request}")

def process_request():
    """Обробляє одну заявку з черги."""
    if not requests_queue.empty():  # Перевірка, чи черга не порожня
        request = requests_queue.get()  # Забрати з черги
        print(f"Обробка: {request}")
        # Тут могла б бути реальна логіка обробки
        time.sleep(0.5)
        print(f"Заявку оброблено: {request}")
    else:
        print("Черга порожня, немає заявок для обробки.")

def main():
    print("Симуляція сервісного центру. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Імітуємо надходження 1–2 нових заявок
            generate_request()
            time.sleep(0.3)
            generate_request()
            # Обробляємо одну заявку з черги
            process_request()
            print("-" * 40)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nРоботу програми завершено.")

if __name__ == "__main__":
    main()