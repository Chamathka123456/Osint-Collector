#!/bin/bash

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║         OSINT COLLECTOR - INSTALLATION SCRIPT            ║
echo "║               For Educational Research                   ║
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}[1/5]${NC} Checking system requirements..."
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Installing Python3...${NC}"
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
fi

echo -e "${BLUE}[2/5]${NC} Creating virtual environment..."
python3 -m venv venv

echo -e "${BLUE}[3/5]${NC} Installing Python packages..."
source venv/bin/activate
pip install phonenumbers requests dnspython

echo -e "${BLUE}[4/5]${NC} Setting up scripts..."
chmod +x osint_collector.py email_hunter.py

echo -e "${BLUE}[5/5]${NC} Creating directories..."
mkdir -p reports logs

echo ""
echo "══════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ INSTALLATION COMPLETE!${NC}"
echo "══════════════════════════════════════════════════════════"
echo ""
echo -e "${BLUE}To run OSINT Collector:${NC}"
echo "  source venv/bin/activate"
echo "  python osint_collector.py"
echo ""
echo -e "${BLUE}To run Email Hunter:${NC}"
echo "  source venv/bin/activate"
echo "  python email_hunter.py"
echo ""
echo -e "${YELLOW}⚠️  CRITICAL LEGAL NOTICE:${NC}"
echo "• FOR EDUCATIONAL AND AUTHORIZED RESEARCH ONLY"
echo "• Use only for yourself or with EXPLICIT PERMISSION"
echo "• Respect all privacy laws (GDPR, CCPA, etc.)"
echo "• Do NOT use for harassment, doxxing, or illegal activities"
echo "• You are responsible for ethical and legal use"
echo ""
echo -e "${GREEN}📊 Sample searches:${NC}"
echo "• Email: user@example.com"
echo "• Phone: +94701234567"
echo "• Name: John Smith"
echo "══════════════════════════════════════════════════════════"
echo ""
