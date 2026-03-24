
                                      🚀 XSS Automation Pipeline
___________________________________________________________________________________________________________________________________________________
                          Automated Reflected XSS Scanner for Bug Bounty Huntersn

                                          Created by winter#aki

                                         "Hack Smart. Hunt Hard." 🎯

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
      cd xss.one

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

___________________________________________________________________________________________________________________________________________________

✅ Run interactively

    </> Bash
    
     python3 script.py

Then enter:

    example.com
    
___________________________________________________________________________________________________________________________________________________

⚡ Workflow

1. Subdomain Enumeration

       </> Bash
          
       subfinder -d target -o subfinder.txt

__________________________________________________________________________________________________________________________________________________   

2. Active Domain Check
.Sends HTTP/HTTPS requests
.Filters alive domains
.Uses multithreading (30 threads)

____________________________________________________________________________________________________________________________________________________

3. Parameter Extraction

       </> Bash

       paramspider -l active.txt

_____________________________________________________________________________________________________________________________________________________

4. Filter Single Parameters
.Keeps only URLs with one parameter
.Removes complex URLs

____________________________________________________________________________________________________________________________________________________

5. Clean Payloads
.Removes FUZZ
.Replaces values → =123

_____________________________________________________________________________________________________________________________________________________

6. Run XSS Scanner

       </> Bash

       dalfox file withoutfuzz.txt

_____________________________________________________________________________________________________________________________________________________

7. Extract XSS PoC
.Filters only valid PoC lines
.Saves results in XSSfinal.txt

_____________________________________________________________________________________________________________________________________________________

🧠 Key Features
.⚡ Fast & efficient (multi-threaded)
.🛡️ Safe subprocess handling
.🔄 Fully automated pipeline
.🧩 Modular design (easy to modify)
.🎯 Focused on high-quality targets

____________________________________________________________________________________________________________________________________________________

📦 requirements.txt

    # HTTP requests for active domain checking
    requests>=2.28.0

    # External tools (install manually):
    # subfinder
    # paramspider
    # dalfox
    # proxychains (optional)

___________________________________________________________________________________________________________________________________________________

⚠️ Disclaimer

This tool is strictly for educational purposes and authorized penetration testing only.
Do NOT use it on systems without proper permission.

_________________________________________________________________________________________________________________________________________________

💡 Future Improvements
.Multi-parameter fuzzing
.Wayback/GAU integration
.JSON/HTML reporting
.CLI flags for each step
.Logging & progress tracking

_________________________________________________________________________________________________________________________________________________

⭐ Contributing

Pull requests are welcome!
Feel free to open issues for bugs or feature requests.

_________________________________________________________________________________________________________________________________________________

👨‍💻 Author

Made with ❤️ for Bug Bounty Hunters













