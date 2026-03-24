
                                      🚀 XSS Automation Pipeline
___________________________________________________________________________________________________________________________________________________
An automated Python-based pipeline for discovering Cross-Site Scripting (XSS) vulnerabilities using popular reconnaissance and fuzzing tools.

_____________________________________________________________________________________________________________________________________________________

🔥 Features
.🔍 Subdomain Enumeration (subfinder)
.🌐 Active Domain Detection (HTTP/HTTPS)
.🔗 Parameter Discovery (paramspider)
.🧹 URL Filtering (single parameter only)
.🧪 Payload Normalization & Cleaning
.💣 Automated XSS Scanning (dalfox)
.✅ Extracts Valid PoC (Proof of Concept) URLs
.⚡ Multi-threaded for speed

______________________________________________________________________________________________________________________________________________________

🧰 Tech Stack
🐍 Python Library
.requests → for HTTP requests & active host detection

🛠️ External Tools
.subfinder → subdomain enumeration
.paramspider → parameter mining
.dalfox → XSS scanner
.proxychains → (optional) anonymity

______________________________________________________________________________________________________________________________________________________

📁 Output Files
| File              | Description           |
| ----------------- | --------------------- |
| `subfinder.txt`   | Discovered subdomains |
| `active.txt`      | Live domains          |
| `param.txt`       | All parameters        |
| `singleparam.txt` | Single parameter URLs |
| `withoutfuzz.txt` | Cleaned URLs          |
| `XSS.txt`         | Raw dalfox output     |
| `XSSfinal.txt`    | Final XSS PoC URLs    |

__________________________________________________________________________________________________________________________________________________

⚙️ Installation

1️⃣ Clone Repository

    </> Bash

      git clone https://github.com/winter3aki/XSS.one.git
      cd xss-automation

__________________________________________________________________________________________________________________________________________________

2️⃣ Install Python Dependencies

    </> Bash

     pip install -r requirements.txt

__________________________________________________________________________________________________________________________________________________

3️⃣ Install Required Tools

Make sure these are installed and added to PATH:

    </> Bash

    subfinder
    paramspider
    dalfox

_________________________________________________________________________________________________________________________________________________

Optional:

    </> Basah

    proxychains

_________________________________________________________________________________________________________________________________________________

▶️ Usage

✅ Run with domain argument

    </> Bash
    
    python3 script.py -d example.com

    
