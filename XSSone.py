#!/usr/bin/env python3

import os
import subprocess
import re
import concurrent.futures
import requests
import argparse
import sys

# ================= FILES =================
SUBFINDER_OUT = "subfinder.txt"
ACTIVE_OUT = "active.txt"
PARAM_FILE = "param.txt"
SINGLE_PARAM = "singleparam.txt"
NOFUZZ = "withoutfuzz.txt"
DALFOX_OUT = "XSS.txt"
FINAL_OUT = "XSSfinal.txt"

THREADS = 30
TIMEOUT = 6

HEADERS = {"User-Agent": "Mozilla/5.0"}
ACTIVE_CODES = {200,201,202,204,301,302,307,308,401,403}


# ================= DOMAIN INPUT =================
def get_domain():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", "--domain", help="Target domain")

    args, unknown = parser.parse_known_args()

    # ✅ If argument diya hai
    if args.domain:
        return args.domain

    # ❌ Agar argument nahi diya → input lo
    try:
        domain = input("Enter target domain (example.com): ").strip()
        if domain:
            return domain
    except:
        pass

    # 🔥 FINAL fallback (no crash)
    print("[!] No input support. Using default domain: test.com")
    return "test.com"


# ================= SAFE SUBPROCESS =================
def safe_run(cmd):
    try:
        subprocess.run(cmd, check=True)
    except OSError:
        print("[!] Subprocess not supported in this environment")
    except Exception as e:
        print(f"[X] Error running command: {e}")


# ================= STEP 1 =================
def run_subfinder(domain):
    print(f"[*] Running subfinder for {domain}...")
    safe_run(["subfinder", "-d", domain, "-o", SUBFINDER_OUT])


# ================= STEP 2 =================
def normalize_domain(line):
    d = line.strip()
    if not d:
        return None
    d = d.replace("http://", "").replace("https://", "")
    d = d.split("/")[0]
    d = d.split(":")[0]
    return d


def is_active(domain):
    for scheme in ["https", "http"]:
        try:
            r = requests.get(f"{scheme}://{domain}", timeout=TIMEOUT, headers=HEADERS)
            if r.status_code in ACTIVE_CODES or (200 <= r.status_code < 600):
                return True
        except:
            pass
    return False


def check_active():
    print("[*] Checking active domains...")

    if not os.path.exists(SUBFINDER_OUT):
        print("[X] subfinder.txt not found!")
        return

    with open(SUBFINDER_OUT) as f:
        domains = list(set(filter(None, [normalize_domain(l) for l in f])))

    active = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = executor.map(lambda d: d if is_active(d) else None, domains)

    for r in results:
        if r:
            print("[ACTIVE]", r)
            active.append(r)

    with open(ACTIVE_OUT, "w") as f:
        f.write("\n".join(active))


# ================= STEP 3 =================
def run_paramspider():
    print("[*] Running paramspider...")
    safe_run(["paramspider", "-l", ACTIVE_OUT])

    if os.path.exists("results"):
        with open(PARAM_FILE, "w") as outfile:
            for file in os.listdir("results"):
                with open(os.path.join("results", file)) as infile:
                    outfile.write(infile.read())


# ================= STEP 4 =================
def filter_single():
    print("[*] Filtering single params...")

    if not os.path.exists(PARAM_FILE):
        print("[X] param.txt missing")
        return

    with open(PARAM_FILE) as f:
        lines = f.readlines()

    out = []
    for line in lines:
        if "?" in line:
            parts = line.split("?", 1)
            if len(parts) > 1 and "&" not in parts[1]:
                out.append(line.strip())

    with open(SINGLE_PARAM, "w") as f:
        f.write("\n".join(out))


# ================= STEP 5 =================
def clean_fuzz():
    print("[*] Cleaning FUZZ...")

    if not os.path.exists(SINGLE_PARAM):
        print("[X] singleparam.txt missing")
        return

    with open(SINGLE_PARAM) as f:
        lines = f.readlines()

    out = []
    for line in lines:
        line = re.sub(r'[Ff][Uu][Zz][Zz]', '', line)
        line = re.sub(r'=[^&]*', '=123', line)
        out.append(line.strip())

    with open(NOFUZZ, "w") as f:
        f.write("\n".join(out))


# ================= STEP 6 =================
def run_dalfox():
    print("[*] Running dalfox...")
    os.system(f"proxychains dalfox file {NOFUZZ} --worker 10 --delay 300 --timeout 20 --output-all --skip-headless -o {DALFOX_OUT}")


# ================= STEP 7 =================
def extract_xss():
    print("[*] Extracting XSS...")

    if not os.path.exists(DALFOX_OUT):
        print("[!] No Dalfox output found")
        return

    with open(DALFOX_OUT) as f:
        lines = f.readlines()

    poc = [l for l in lines if "poc" in l.lower()]

    with open(FINAL_OUT, "w") as f:
        f.writelines(poc)

    print(f"[+] Found {len(poc)} XSS URLs → {FINAL_OUT}")


# ================= MAIN =================
def main():
    print(r"""
██╗  ██╗███████╗███████╗    ██████╗ ███╗   ██╗███████╗
╚██╗██╔╝██╔════╝██╔════╝    ██╔═══██╗████╗  ██║██╔════╝
 ╚███╔╝ ███████╗███████╗    ██║   ██║██╔██╗ ██║█████╗  
 ██╔██╗ ╚════██║╚════██║    ██║   ██║██║╚██╗██║██╔══╝  
██╔╝ ██╗███████║███████║     ██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝

            XSS.one Tool
""")

    domain = get_domain()

    print(f"\n🎯 Target: {domain}\n")

    run_subfinder(domain)
    check_active()
    run_paramspider()
    filter_single()
    clean_fuzz()
    run_dalfox()
    extract_xss()


if __name__ == "__main__":
    main()


