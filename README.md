
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

______________________________________________________________________________________________________________________________________________________
