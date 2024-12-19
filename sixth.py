import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Nastala chyba, http code: {response.status_code}")

    html_text = response.text
    pattern = re.compile(r'<a\s+[^>]*href=["\'](.*?)["\']', re.IGNORECASE)
    matches = pattern.findall(html_text)
    hrefs.extend(matches)



    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        print (all_hrefs)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
    except requests.exceptions.ConnectionError:
        print(f"Nastala chyba, nepodařilo se připojit na {url}")
    
