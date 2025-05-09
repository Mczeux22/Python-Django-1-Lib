import sys
import requests
import dewiki
import os

def fetch_summary(search_term):
    try:
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": search_term,
            "prop": "extracts",
            "explaintext": True,
            "redirects": 1
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        pages = data["query"]["pages"]
        page = next(iter(pages.values()))
        
        if "extract" not in page or not page["extract"]:
            raise ValueError("Aucune information trouvée sur Wikipédia.")

        raw_text = page["extract"]
        clean_text = dewiki.from_string(raw_text)

        return clean_text

    except Exception as e:
        print(f"Erreur : {e}")
        return None

def save_to_file(search_term, content):
    filename = search_term.replace(" ", "_") + ".wiki"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage : python3 request_wikipedia.py <recherche>")
        return

    search_term = sys.argv[1]
    result = fetch_summary(search_term)

    if result:
        save_to_file(search_term, result)
        print(f"Résultat enregistré dans : {search_term.replace(' ', '_')}.wiki")
    else:
        print("Échec de la récupération des données.")

if __name__ == "__main__":
    main()
