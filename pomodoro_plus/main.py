import time
import json
from datetime import date

DATA_FILE = "data.json"
SETTINGS_FILE = "settings.json"


# -------------------- TIMER --------------------
def countdown(minutes, label):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins = total_seconds // 60
        secs = total_seconds % 60
        print(f"{label} ⏳ {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(f"\n{label} tamamlandı!")


# -------------------- DATA (STATS) --------------------
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def update_stats(minutes):
    today = str(date.today())
    data = load_data()

    if today not in data:
        data[today] = {"pomodoro": 0, "minutes": 0}

    data[today]["pomodoro"] += 1
    data[today]["minutes"] += minutes

    save_data(data)


def show_stats():
    today = str(date.today())
    data = load_data()

    print("\n Günlük İstatistikler")

    if today in data:
        print(f"Pomodoro sayısı: {data[today]['pomodoro']}")
        print(f"Toplam çalışma süresi: {data[today]['minutes']} dakika")
    else:
        print("Bugün için kayıt yok.")


# -------------------- SETTINGS --------------------
def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "work_minutes": 25,
            "short_break": 5,
            "long_break": 15
        }


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def settings_menu():
    settings = load_settings()

    while True:
        print("\n Ayarlar")
        print(f"1. Çalışma süresi (dk): {settings['work_minutes']}")
        print(f"2. Kısa mola süresi (dk): {settings['short_break']}")
        print(f"3. Uzun mola süresi (dk): {settings['long_break']}")
        print("4. Geri dön")

        choice = input("Seçiminizi girin (1-4): ")

        if choice == "1":
            settings["work_minutes"] = int(input("Yeni çalışma süresi (dk): "))
        elif choice == "2":
            settings["short_break"] = int(input("Yeni kısa mola süresi (dk): "))
        elif choice == "3":
            settings["long_break"] = int(input("Yeni uzun mola süresi (dk): "))
        elif choice == "4":
            save_settings(settings)
            break
        else:
            print("Geçersiz seçim.")


# -------------------- MENU --------------------
def show_menu():
    print("\n Pomodoro Plus")
    print("1. Pomodoro Başlat")
    print("2. Günlük İstatistikleri Gör")
    print("3. Ayarları Değiştir")
    print("4. Çıkış")


# -------------------- MAIN --------------------
def main():
    pomodoro_count = 0

    while True:
        show_menu()
        choice = input("Seçiminizi girin (1-4): ")

        if choice == "1":
            settings = load_settings()
            pomodoro_count += 1

            print(f"\n Pomodoro #{pomodoro_count} başladı!")
            countdown(settings["work_minutes"], "Çalışma")
            update_stats(settings["work_minutes"])

            if pomodoro_count % 4 == 0:
                print("Uzun mola zamanı!")
                countdown(settings["long_break"], "Uzun Mola")
            else:
                print(" Kısa mola zamanı!")
                countdown(settings["short_break"], "Kısa Mola")

        elif choice == "2":
            show_stats()

        elif choice == "3":
            settings_menu()

        elif choice == "4":
            print("Programdan çıkılıyor. İyi çalışmalar!")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")


main()
