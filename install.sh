#!/bin/bash
# ============================================
# XSS one - Auto Installer
# Usage: chmod +x install.sh && ./install.sh
# ============================================

GREEN="\033[92m"
CYAN="\033[96m"
RED="\033[91m"
RESET="\033[0m"

echo -e "${CYAN}"
echo "============================================"
echo "        XSS one - Auto Installer           "
echo "         Created by winter            "
echo "============================================"
echo -e "${RESET}"

# Python dependencies
echo -e "${CYAN}[*]${RESET} Installing Python dependencies..."
pip install requests
echo -e "${GREEN}[+]${RESET} requests installed!"

# ParamSpider
echo -e "${CYAN}[*]${RESET} Installing ParamSpider..."
pip install paramspider --break-system-packages
echo -e "${GREEN}[+]${RESET} ParamSpider installed!"

# Subfinder
echo -e "${CYAN}[*]${RESET} Installing Subfinder..."
sudo apt install subfinder
echo -e "${GREEN}[+]${RESET} Subfinder installed!"

# Dalfox
echo -e "${CYAN}[*]${RESET} Installing Dalfox..."
sudo apt update
sudo apt install build-essential procps curl file git
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
brew doctor
brew install dalfox
echo -e "${GREEN}[+]${RESET} Dalfox installed!"

echo ""
echo -e "${GREEN}============================================${RESET}"
echo -e "${GREEN}   All tools installed successfully! 🎯    ${RESET}"
echo -e "${GREEN}   Run: python3 xssone.py -d target.com ${RESET}"
echo -e "${GREEN}============================================${RESET}"
