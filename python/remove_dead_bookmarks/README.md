## Requirements

- Python 3
- 'requests' library

## Setup

1. Ensure Python 3 is installed on your system.
2. Install the 'requests' library using pip:

```
pip install requests
```

3. Locate your Firefox `places.sqlite` file and create a backup.

## Usage

1. Close Firefox to prevent database locking issues.
2. Copy your `places.sqlite` file to a safe location and note the path.
3. Run the script with the path to your database file:

```
python bookmark_cleanup_deadlink.py --db-path /path/to/your/places_copy.sqlite
```
