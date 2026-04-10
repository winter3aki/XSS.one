#!/usr/bin/env python3
"""
XSSone - Ultimate Scanner
"""

import os
import subprocess
import sys
import re
import shutil
import concurrent.futures
import requests
import argparse
import time
import signal
from pathlib import Path

# ================= CONFIG =================
THREADS = 20
TIMEOUT = 6

SUBS_FILE = "subdomains.txt"
ACTIVE_FILE = "active.txt"
PARAM_FILE = "parameters.txt"
SINGLE_FILE = "singleparam.txt"
NOFUZZ_FILE = "nofuzz.txt"
DALFOX_OUT = "scan.txt"
FINAL_OUT = "vulnerable.txt"

HEADERS = {"User-Agent": "Mozilla/5.0"}

# ================= COLORS =================
RED="\033[91m"; GREEN="\033[92m"; YELLOW="\033[93m"
CYAN="\033[96m"; BOLD="\033[1m"; RESET="\033[0m"

def info(x): print(f"{CYAN}[*]{RESET} {x}")
def ok(x): print(f"{GREEN}[+]{RESET} {x}")
def warn(x): print(f"{YELLOW}[!]{RESET} {x}")
def err(x): print(f"{RED}[X]{RESET} {x}")

# ================= BANNER =================
def banner():
    print(f"""{CYAN}{BOLD}
██╗  ██╗███████╗███████╗ ██████╗ ██████╗ ███╗   ██╗███████╗
╚██╗██╔╝██╔════╝██╔════╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝
 ╚███╔╝ ███████╗███████╗██║   ██║██████╔╝██╔██╗ ██║█████╗  
 ██╔██╗ ╚════██║╚════██║██║   ██║██╔═══╝ ██║╚██╗██║██╔══╝  
██╔╝ ██╗███████║███████║╚██████╔╝██║     ██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═══╝╚══════╝

        🔥 XSSone - Ultimate Scanner 🔥
{RESET}
""")

# ================= DOMAIN INPUT =================
def get_domain():
    try:
        domain = input(f"{CYAN}[?]{RESET} Enter target domain (example.com): ").strip()
        if domain:
            return domain
    except:
        pass

    warn("No input detected. Using default: test.com")
    return "test.com"

# ================= INTERNET =================
def check_internet():
    import socket
    for host in ["8.8.8.8","1.1.1.1"]:
        try:
            socket.create_connection((host,53),2)
            return True
        except:
            pass
    return False

def wait_net():
    if check_internet(): return
    warn("No internet. Waiting...")
    while not check_internet():
        time.sleep(2)
    ok("Internet restored")

# ================= CTRL+C =================
def handler(sig, frame):
    warn("Stopped by user. Progress saved.")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

# ================= STEP 1 =================
def subfinder(domain):
    info("Running subfinder...")
    if not shutil.which("subfinder"):
        err("Install subfinder")
        sys.exit(1)

    subprocess.run(["subfinder","-d",domain,"-silent","-o",SUBS_FILE])
    return SUBS_FILE

# ================= STEP 2 =================
def is_active(domain):
    try:
        r = requests.get("http://" + domain, timeout=TIMEOUT)
        return r.status_code < 500
    except:
        return False

def active_check(file):
    info("Checking active domains...")

    with open(file) as f:
        domains = list(set([x.strip() for x in f if x.strip()]))

    active=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as ex:
        results = ex.map(lambda d: d if is_active(d) else None, domains)

    for r in results:
        if r:
            print("[ACTIVE]", r)
            active.append(r)

    with open(ACTIVE_FILE,"w") as f:
        f.write("\n".join(active))

    ok(f"{len(active)} active domains")
    return ACTIVE_FILE

# ================= STEP 3 =================
def paramspider(domain, active_file):
    info("Running paramspider...")

    if not shutil.which("paramspider"):
        err("pip install paramspider")
        sys.exit(1)

    wait_net()

    if os.path.exists(active_file):
        subprocess.run(["paramspider","-l",active_file])
    else:
        subprocess.run(["paramspider","-d",domain])

    results = Path("results")
    if not results.exists():
        err("No results folder")
        sys.exit(1)

    with open(PARAM_FILE,"w") as out:
        for f in results.glob("*.txt"):
            out.write(open(f).read())

    ok("Parameters collected")
    return PARAM_FILE

# ================= STEP 4 =================
def filter_single(file):
    info("Filtering single params...")

    out=[]
    with open(file) as f:
        for line in f:
            if "?" in line and "&" not in line.split("?")[1]:
                out.append(line.strip())

    with open(SINGLE_FILE,"w") as f:
        f.write("\n".join(out))

    ok(f"{len(out)} single params")
    return SINGLE_FILE

# ================= STEP 5 =================
def clean(file):
    info("Cleaning FUZZ...")

    out=[]
    for l in open(file):
        l = re.sub(r'FUZZ','123',l,flags=re.I)
        l = re.sub(r'=[^&]*','=123',l)
        out.append(l.strip())

    with open(NOFUZZ_FILE,"w") as f:
        f.write("\n".join(set(out)))

    return NOFUZZ_FILE

# ================= STEP 6 =================
def dalfox(file):
    info("Running Dalfox...")

    if not shutil.which("dalfox"):
        err("Install dalfox")
        sys.exit(1)

    wait_net()

    subprocess.run([
        "dalfox","file",file,
        "--skip-bav",
        "--waf-evasion",
        "--output-all",
        "-o",DALFOX_OUT
    ])

    return DALFOX_OUT

# ================= STEP 7 =================
def extract(file):
    info("Extracting XSS...")

    if not os.path.exists(file):
        warn("No output file")
        return

    vulns=[]
    for l in open(file):
        if "[POC]" in l or "[W]" in l:
            vulns.append(l)

    with open(FINAL_OUT,"w") as f:
        f.writelines(vulns)

    ok(f"{len(vulns)} XSS found")
    print("\n".join(vulns))

# ================= MAIN =================
def main():
    banner()  # 🔥 logo

    domain = get_domain()  # ❓ ask domain
    print(f"\n{BOLD}Target:{RESET} {domain}\n")

    wait_net()

    subs = subfinder(domain)
    active = active_check(subs)
    params = paramspider(domain, active)
    single = filter_single(params)
    nofuzz = clean(single)
    scan = dalfox(nofuzz)
    extract(scan)

    ok("DONE 🎯")

if __name__ == "__main__":
    main()
