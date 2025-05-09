import sys
import antigravity

if len(sys.argv) != 5:
    print("Usage: python3 script.py <date> <dow> <latitude> <longitude>")
    sys.exit(1)

try:
    date = sys.argv[1]
    dow = sys.argv[2]
    lat = float(sys.argv[3])
    lon = float(sys.argv[4])
    datedow = f"{date}-{dow}".encode()  # 🟢 ENCODAGE ICI

    antigravity.geohash(lat, lon, datedow)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
