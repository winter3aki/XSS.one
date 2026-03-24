# XSS.one
Automated Reflected XSS Scanner for Bug Bounty Hunters Built with Subfinder, ParamSpider &amp; Dalfox

🚀 XSS Automation Pipeline

An automated Python script to discover and extract XSS (Cross-Site Scripting) vulnerabilities by chaining popular recon and fuzzing tools.

🔥 Overview

This tool performs a complete pipeline:

🔍 Subdomain enumeration
🌐 Live host detection
🔗 Parameter discovery
🧹 URL filtering & cleaning
💣 Automated XSS scanning
✅ Extracts valid PoC results
🧰 Tools Used
subfinder → Subdomain discovery
paramspider → Parameter mining
dalfox → XSS scanner
proxychains → (optional) anonymity
📁 Output Files
File Name	Description
subfinder.txt	All discovered subdomains
active.txt	Live domains
param.txt	All parameters collected
singleparam.txt	URLs with single parameters
withoutfuzz.txt	Clean URLs for scanning
XSS.txt	Raw scan results
XSSfinal.txt	Extracted XSS PoC URLs
⚙️ Requirements
🐍 Python
Python 3.x
📦 Python Libraries
pip install requests
🛠️ External Tools (Required)

Make sure these are installed and in PATH:

subfinder
paramspider
dalfox

Optional:

proxychains
📥 Installation
git clone https://github.com/yourusername/xss-automation.git
cd xss-automation
chmod +x script.py
▶️ Usage
✅ With domain argument
python3 script.py -d example.com
✅ Without argument (interactive)
python3 script.py

Then enter:

example.com
⚡ Workflow Explained
1. Subdomain Enumeration

Runs:

subfinder -d target -o subfinder.txt
2. Active Domain Check
Uses multithreading (30 threads)
Sends HTTP/HTTPS requests
Filters live hosts
3. Parameter Collection

Runs:

paramspider -l active.txt
4. Single Parameter Filtering
Keeps only URLs with one parameter
Removes complex multi-param URLs
5. Payload Cleaning
Removes FUZZ
Normalizes values → =123
6. XSS Scanning

Runs:

dalfox file withoutfuzz.txt

(through proxychains if enabled)

7. PoC Extraction
Filters only lines containing "poc"
Saves final vulnerable URLs
🧠 Key Features
⚡ Fast (multithreaded active checking)
🛡️ Safe subprocess handling
🔄 Fully automated pipeline
🧩 Modular steps (easy to extend)
🧪 Focused on high-quality XSS targets
⚠️ Disclaimer

This tool is for educational purposes and authorized testing only.
Do NOT scan targets without permission.

💡 Future Improvements
Add multi-parameter fuzzing
Integrate Wayback/GAU URLs
JSON/HTML report export
Add CLI flags for each step
Better error handling & logging
⭐ Contribute

Pull requests are welcome!
If you find bugs or want features, open an issue.

👨‍💻 Author

Made with ❤️ for Bug Bounty Hunters

If you want next level upgrade, I can:

add auto recon + nuclei integration
convert this into a full bug bounty framework
or build a GUI version
