import argparse
import sqlite3
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime

# Path to your copy of the Firefox places.sqlite database
DB_PATH = '/home/adam/.librewolf/fqinuves.default-default/places.sqlite'

def is_link_alive(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except (ConnectionError, Timeout, TooManyRedirects):
        return False

def mark_dead_links(conn, dry_run=False):
    cursor = conn.cursor()
    cursor.execute("SELECT id, url FROM moz_places WHERE url LIKE 'http%' AND title NOT LIKE '[DEAD LINK]%'")

    dead_links = 0
    for row in cursor.fetchall():
        place_id, url = row
        if not is_link_alive(url):
            print(f"Identified dead link: {url}")
            if not dry_run:
                dead_link_title = "[DEAD LINK] " + str(datetime.now())
                cursor.execute("UPDATE moz_places SET title=? WHERE id=?", (dead_link_title, place_id))
            dead_links += 1

    if dead_links > 0 and not dry_run:
        conn.commit()
    print(f"Finished checking. Identified {dead_links} dead links{' (dry run)' if dry_run else ''}.")

def main():
    parser = argparse.ArgumentParser(description='Mark dead links in Firefox bookmarks.')
    parser.add_argument('--dry-run', action='store_true', help='Run the script without making any changes to the database.')
    args = parser.parse_args()

    with sqlite3.connect(DB_PATH) as conn:
        mark_dead_links(conn, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

