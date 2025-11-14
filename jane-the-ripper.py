import hashlib

def crack_passwords(hash_file_path, wordlist_path):
    cracked = []
    with open(hash_file_path, 'r') as hashes:
        for line in hashes:
            hash_value = line.strip()
            cracked.append(hash_value)
            with open(wordlist_path, 'r') as wordlist:
                for word in wordlist:
                    word = word.strip()
                    encoded = hashlib.md5(word.encode())
                    encoded_hex = encoded.hexdigest()
                    if encoded_hex == hash_value:
                        print(f"✅ Cracked: {hash_value} -> {word}")
                        cracked.remove(hash_value)
            if hash_value in cracked:
                print(f"❌ Could not crack: {hash_value}")

def main():
    hash_file = input("Enter path to hash file: ")
    wordlist_file = input("Enter path to wordlist file: ")

    crack_passwords(hash_file, wordlist_file)

main()