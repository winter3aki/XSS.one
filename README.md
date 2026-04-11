# 🔥 XSSone - Ultimate XSS Scanner

**XSSone** is an automated bug bounty tool designed to find **Reflected XSS vulnerabilities** using a complete pipeline:

> Subdomain → Active → Parameters → Filter → Dalfox → XSS

---

## 🚀 Features

* 🔍 Subdomain discovery using **subfinder**
* 🌐 Active domain filtering (multi-threaded)
* 🧠 Parameter collection using **paramspider**
* 🎯 Single parameter filtering (high XSS probability)
* 🧹 FUZZ cleaning & payload preparation
* ⚡ XSS detection using **dalfox**
* 🌍 Internet auto-check & retry
* 🖥️ Clean CLI + Banner
* 💾 Auto-saves results

---
<img width="1024" height="1024" alt="dd255264-4b49-4021-a29b-468d1ea94a09" src="https://github.com/user-attachments/assets/adb7fb4d-d329-4333-97fa-d4dd6cb99d4c" />
## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/winter3aki/XSS.one.git
cd XSS.one
```

---

## ⚙️ Requirements

Make sure these tools are installed:

### 1. Subfinder

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

### 2. ParamSpider

```bash
pip install paramspider
```

### 3. Dalfox

```bash
sudo apt update
sudo apt install build-essential procps curl file git
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
brew doctor
brew install dalfox
```

### 4. Python Modules

```bash
pip install requests
```

---

## ▶️ Usage

Run the tool:

```bash
python3 XSSone.py
```

You will be prompted:

```bash
[?] Enter target domain (example.com):
```

---

## 🔄 Workflow

```
Domain Input
   ↓
Subfinder (subdomains)
   ↓
Active Check
   ↓
ParamSpider (parameters)
   ↓
Filter Single Params
   ↓
Clean FUZZ
   ↓
Dalfox Scan
   ↓
Extract XSS (POC)
```

---

## 📁 Output Files

| File              | Description               |
| ----------------- | ------------------------- |
| `subdomains.txt`  | All discovered subdomains |
| `active.txt`      | Active domains            |
| `parameters.txt`  | All collected URLs        |
| `singleparam.txt` | Single parameter URLs     |
| `nofuzz.txt`      | Cleaned URLs              |
| `scan.txt`        | Dalfox full scan          |
| `vulnerable.txt`  | 🎯 Final XSS results      |

---

## 📌 Example Output

```
[POC][GET] https://target.com/page.php?q=<script>alert(1)</script>
```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing only**.

❌ Do NOT scan targets without permission
❌ You are responsible for your actions

---

## 👨‍💻 Author

**Winter AKI**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🛠️ Contribute

---

## 🔗 Repository

👉 https://github.com/winter3aki/XSS.one.git

---
