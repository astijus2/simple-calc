import os
from supabase import create_client
from alive_progress import alive_bar
import time
from datetime import date as dt


url = "https://iofzhihjlsdldolbgzwz.supabase.co"
key = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvZnpoaWhqbHNkbGRvbGJnend6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1NjU0MzQsImV4cCI6MjA4ODE0MTQzNH0.4cSK-JBDl9mfw2Cr3O5gg6kWgS_XKo8sJ3clYhWk9Wg")
supabase = create_client(url, key)

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
RESET   = "\033[0m"

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{RED}Iveskite skaiciu!{RESET}")

def get_str(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print(f"{RED}Negali buti tuscias!{RESET}")

def loading():
    with alive_bar(150, title = "Grabbing data...") as bar:
        for i in range(150):
            time.sleep(0.02)
            if i == 20:
                bar.title("Getting location...")
            elif i == 50:
                bar.title("Installing keylogger...")
            elif i == 100:
                bar.title("Getting IP...")
            bar()

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}Iveskite sveika skaiciu!{RESET}")




os.system("clear")
print("================================")
print("       Ismok skaiciuot              ")
print("================================\n")

username = get_str("Iveskite savo varda: ")

loading()

while True:
    os.system("clear")
    print("================================")
    print("           Ismok skaiciuot              ")
    print("================================\n")
    print("Pasirinkite veiksma:\n")
    print("1. Apskaiciuoti sekancio signalo dydi")
    print("2. Irasyti trade'a i istorija")
    print("3. Paziureti savo istorija")
    print("4. Iseit nahui\n")

    choice = input("Pasirinkite veiksma: ").strip()
    print()

    if choice == "1":
        os.system("clear")
        balancas = get_float("Iveskite savo balanca: ")
        naujas_input = balancas / (100 / 15)
        print(f"\nDek ant sekancio signalo - {RED}{naujas_input:.2f}{RESET}")
        while True:
            pasilikti = input("Ar dar kazka veiksi? Y/n: ")
            if pasilikti.lower() == "y":
                break
            elif pasilikti.lower() == "n":
                print("Iki sekancio...")
                exit()
            else:
                print(f"{RED}Debilas? ar skaityt nemoki{RESET}")
                continue

    elif choice == "2":
        os.system("clear")
        print("================================================")
        valiuta = get_str("Kokia valiuta pirkote? - ")
        proc    = get_float("Kiek procentu padarete? - ")
        pinigai = get_float("Kiek pinigu investavote? - ")
        leverage = get_int("Koks leverage? - ")
        print("================================================")
        print()

        proc_str = f"{proc:.2f}%"
        padded   = f"{proc_str:>11}"
        Cproc    = f"{GREEN}{padded}{RESET}" if proc >= 0 else f"{RED}{padded}{RESET}"

        header = (f"{'Valiuta':<10} | {'Pozicijos verte':>20} | {'(%) proc':>11} | {'Leverage':>11} | {'Data':>10} |")
        separator = ("-" * len(header))
        print(header)
        print(separator)
        print(f"{valiuta:<10} | {pinigai:>20.2f} | {Cproc} | {leverage:>11.2f} | {str(dt.today()):>10} |")

        supabase.table("Istorija").insert({
            "valiuta": valiuta,
            "proc": proc,
            "pinigai": pinigai,
            "username": username,
            "leverage": leverage
        }).execute()
        print()
        print(f"{GREEN}Issaugota! ✅ {RESET}")
        print()
        while True:
            pasilikti = input("Ar dar kazka veiksi? Y/n: ")
            if pasilikti.lower() == "y":
                break
            elif pasilikti.lower() == "n":
                print("Iki sekancio...")
                os.system("clear")
                exit()
            else:
                print(f"{RED}Debilas? ar skaityt nemoki{RESET}")
                continue

    elif choice == "3":
        os.system("clear")
        data = supabase.table("Istorija").select("*").eq("username", username).execute()

        if not data.data:
            print()
            print("Istorija dar tuscia!")
            input("\nPress any key to main menu...")
        else:
            
            header = (f"| {'#':^5} | {'Valiuta':<10} | {'Pozicijos verte':>20} | {'(%) proc':>11} | {'Leverage':>12} | {'Data':>10} |")
            separator = ("-" * len(header))
            print(separator)
            print(header)
            print(separator)
            for i, row in enumerate(data.data, 1):
                proc    = float(row["proc"])   # type: ignore
                valiuta = str(row["valiuta"])  # type: ignore
                proc_str = f"{proc:.2f}%"
                padded   = f"{proc_str:>11}"
                Cproc    = f"{GREEN}{padded}{RESET}" if proc >= 0 else f"{RED}{padded}{RESET}"
                date = str(row["created_at"])[:10] # type: ignore
                print(f"| {i:^5} | {valiuta:<10} | {row['pinigai']:>20.2f} | {Cproc} | {row['leverage']:>11}x | {date:>10} |") # type: ignore
            print(separator)
            print()
            print("\n1. Istrinti irasa | Enter - atgal")
            action = input("Pasirinkite: ").strip().lower()

            if action == "1":
                nr = input("Kurio numerio irasa istrinti? ")
                try:
                    row_id = data.data[int(nr) - 1]["id"] # type: ignore
                    supabase.table("Istorija").delete().eq("id", row_id).execute()
                    print(f"{GREEN}Istrinta!{RESET}")
                    input("\nPress any key to continue...")
                except (IndexError, ValueError):
                    print(f"{RED}Neteisingas numeris!{RESET}")
                    input("\nPress any key to main menu...")

    elif choice == "4":
        os.system("clear")
        print("Iki sekancio...")
        exit()
    else:
        print(f"{RED}Debilas? ar skaityt nemoki{RESET}")