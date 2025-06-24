import base64
import gzip
from io import BytesIO
#For OffSec's PG Compromised Machine

def main():
    decoded = encoded()
    decode(decoded)

#Decode with Base64
def encoded():
    encoded = input("String: ").strip()
    decoded = base64.b64decode(encoded)
    return decoded

#Decompress the Compressed Blob
def decode(decoded):
    with gzip.GzipFile(fileobj=BytesIO(decoded)) as f:
        decomp_str = f.read()
    decomp_data = decomp_str.decode('utf-8', errors='replace')
    print(decomp_data)

if __name__ == "__main__":
    main()
