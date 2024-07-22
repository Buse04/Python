import argparse

def parse(name, lang):
    list = {
        "Turkish": "Merhaba",
        "English": "Hello",
        "German": "Hallo"
    }
    mesagge = f"{list[lang]} {name}"
    print(mesagge)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description= "Provides personal info"
    )

    parser.add_argument(
        "--name" , metavar= "name", required= True, help= "Enter your name"
    )

    parser.add_argument(
        "--lang" , metavar= "language", required=True, choices= ["Turkish", "English", "German"]
    )

    args = parser.parse_args()
    parse(args.name, args.lang)

    