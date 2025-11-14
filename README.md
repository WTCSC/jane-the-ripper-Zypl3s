# Jane-the-Ripper

- reads a file of MD5 hashes
- tries each word from a provided wordlist
- computes the MD5 of each word and compares it to each target hash
- prints cracked results and reports any hashes it couldn't crack

### Usage

Run the script and provide the paths when prompted:

```bash
python3 jane-the-ripper.py
```

Expected output examples:

- `✅ Cracked: <md5hash> -> password` for matches
- `❌ Could not crack: <md5hash>` when no match found

### How it works (flowchart)

```mermaid
flowchart TD
  Start([Start]) --> ReadHashes["Read hashes file"]
  ReadHashes --> ForEachHash["Every hash in file"]
  ForEachHash --> OpenWordlist["Open wordlist"]
  OpenWordlist --> ForEachWord["Every word in wordlist"]
  ForEachWord --> ComputeMD5["Compute MD5(word)"]
  ComputeMD5 --> Compare{"MD5 == target hash?"}
  Compare -- Yes --> Cracked["Print cracked (hash -> word)"]
  Cracked --> CheckNextHash["Check next hash"]
  Compare -- No --> EndWordlistCheck["Try next word"]
  EndWordlistCheck --> ComputeMD5
  ForEachWord --> NotCracked["Print could not crack"]
  NotCracked --> CheckNextHash
  CheckNextHash --> NextHash["hashes left?"]
  NextHash -- Yes --> ForEachHash
  NextHash -- No --> End([End])
```