import argparse
from api import check_weather
import json
import sys
import csv


def main():
    parser = argparse.ArgumentParser(
        description="CLI donde se obtienen datos del clima"
    )  # Inicializa parser
    parser.add_argument("city", help="Indica el nombre de la ciudad")
    parser.add_argument(
        "format", choices=["json", "csv"], help="Elige el formato de salida json o cvs"
    )

    args = parser.parse_args()  # Trae de parser la informacion de args

    city = args.city
    format = args.format

    print(f"Obtener el clima de {city} en formato {format}.")

    try:
        weather = check_weather(city)
        if format == "json":
            print(json.dumps(weather, indent=2))

        else:
            # Abrir el archivo en modo escritura
            # with open(f"{city}weather.csv", mode='w', newline='') as narchivo_csv:
            writer = csv.DictWriter(sys.stdout, fieldnames=weather.keys())
            writer.writeheader()
            writer.writerow(weather)

    except Exception as e:
        print(f"Err: {e}")


if __name__ == "__main__":
    main()
