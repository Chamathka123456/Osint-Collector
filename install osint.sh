#!/bin/bash
# setup.sh - OSINT Collector Installation Script

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║         OSINT COLLECTOR - COMPLETE INSTALLATION          ║
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    echo -e "${RED}❌ Do not run as root/sudo${NC}"
    echo "Run as normal user and use virtual environment"
    exit 1
fi

# Step 1: Check Python
echo -e "${BLUE}[1/6]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Installing Python3...${NC}"
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
fi
echo -e "${GREEN}✓ Python3: $(python3 --version)${NC}"

# Step 2: Create virtual environment
echo -e "${BLUE}[2/6]${NC} Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}✓ Virtual environment already exists${NC}"
fi

# Step 3: Activate and upgrade pip
echo -e "${BLUE}[3/6]${NC} Activating virtual environment..."
source venv/bin/activate
pip install --upgrade pip setuptools wheel

# Step 4: Install requirements
echo -e "${BLUE}[4/6]${NC} Installing dependencies..."
if [ -f "requirements.txt" ]; then
    echo "Installing from requirements.txt..."
    pip install -r requirements.txt
else
    echo -e "${YELLOW}⚠️ requirements.txt not found, installing core packages${NC}"
    pip install phonenumbers requests dnspython beautifulsoup4 lxml cryptography python-dotenv
fi

# Step 5: Create directories
echo -e "${BLUE}[5/6]${NC} Creating directory structure..."
mkdir -p {reports,logs,cache,exports,tmp,backups}
echo -e "${GREEN}✓ Directories created${NC}"

# Step 6: Set permissions
echo -e "${BLUE}[6/6]${NC} Setting permissions..."
chmod +x osint_collector.py
chmod +x setup.sh
find . -name "*.py" -exec chmod +x {} \;
echo -e "${GREEN}✓ Permissions set${NC}"

echo ""
echo "══════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ INSTALLATION COMPLETE!${NC}"
echo "══════════════════════════════════════════════════════════"
echo ""
echo -e "${BLUE}TO START THE TOOL:${NC}"
echo "  source venv/bin/activate"
echo "  python osint_collector.py"
echo ""
echo -e "${BLUE}QUICK START:${NC}"
echo "  ./setup.sh  # Run this script"
echo "  source venv/bin/activate"
echo "  python osint_collector.py"
echo ""
echo -e "${YELLOW}⚠️  IMPORTANT NOTES:${NC}"
echo "1. First run will create necessary directories"
echo "2. All searches are logged in 'logs/' directory"
echo "3. Reports are saved in 'reports/' directory"
echo "4. Use responsibly and ethically"
echo ""
echo -e "${GREEN}📞 TEST WITH:${NC}"
echo "• Phone: +94701234567"
echo "• Email: test@example.com"
echo "• Username: testuser"
echo "══════════════════════════════════════════════════════════"
echo ""
