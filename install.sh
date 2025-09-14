#!/bin/bash
# HackGPT Installation Script for Kali Linux

echo "🔥 HackGPT Installation Script 🔥"
echo "=================================="

# Update system
echo "[+] Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
echo "[+] Installing Python dependencies..."
pip3 install -r requirements.txt

# Install system tools that may not be present
echo "[+] Installing pentesting tools..."
sudo apt install -y \
    nmap \
    masscan \
    nikto \
    gobuster \
    sqlmap \
    hydra \
    theharvester \
    enum4linux \
    whatweb \
    wpscan \
    dnsenum \
    whois \
    exploitdb \
    metasploit-framework \
    netcat-traditional \
    curl \
    wget \
    git

# Install ollama for local AI
echo "[+] Installing ollama for local AI support..."
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a lightweight model
echo "[+] Downloading local AI model..."
ollama pull llama2:7b

# Create reports directory
echo "[+] Creating reports directory..."
sudo mkdir -p /reports
sudo chown -R $USER:$USER /reports

#!/bin/bash

# HackGPT Enterprise Installation Script
# Installs all dependencies for enterprise penetration testing platform
# Version: 2.0.0 (Production-Ready)

set -e  # Exit on any error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1"
}

info() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')] INFO:${NC} $1"
}

# Exit on any command failure
trap 'error "Installation failed. Exiting."' ERR

# Banner
echo -e "${PURPLE}"
echo "██╗  ██╗ █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ ████████╗"
echo "██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗╚══██╔══╝"
echo "███████║███████║██║     █████╔╝ ██║  ███╗██████╔╝   ██║   "
echo "██╔══██║██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝    ██║   "
echo "██║  ██║██║  ██║╚██████╗██║  ██╗╚██████╔╝██║        ██║   "
echo "╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   "
echo -e "${NC}"
echo -e "${CYAN}Enterprise AI-Powered Penetration Testing Platform v2.0${NC}"
echo -e "${GREEN}Production-Ready | Cloud-Native | AI-Enhanced${NC}"
echo

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    warn "Running as root. Some installations may behave differently."
fi

# Detect OS
OS="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f /etc/debian_version ]; then
        OS="Debian/Ubuntu"
    elif [ -f /etc/redhat-release ]; then
        OS="RedHat/CentOS"
    elif [ -f /etc/arch-release ]; then
        OS="Arch"
    else
        OS="Linux"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
    OS="Windows"
fi

log "Detected OS: $OS"

# Check Python version
check_python() {
    log "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        log "Found Python $PYTHON_VERSION"
        
        # Check if version is 3.8 or higher
        if python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
            log "Python version is compatible"
            PYTHON_CMD="python3"
        else
            error "Python 3.8 or higher is required. Found: $PYTHON_VERSION"
            exit 1
        fi
    else
        error "Python 3 is not installed"
        exit 1
    fi
}

# Install system dependencies
install_system_deps() {
    log "Installing system dependencies..."
    
    case $OS in
        "Debian/Ubuntu")
            sudo apt update
            sudo apt install -y 
                python3-dev python3-pip python3-venv 
                build-essential libssl-dev libffi-dev 
                libjpeg-dev zlib1g-dev 
                libpq-dev 
                redis-server 
                postgresql postgresql-contrib 
                docker.io docker-compose 
@@ -248,85 +201,87 @@ setup_postgresql() {
# Setup Redis
setup_redis() {
    log "Setting up Redis cache server..."
    
    case $OS in
        "Debian/Ubuntu"|"Linux")
            sudo systemctl start redis-server
            sudo systemctl enable redis-server
            ;;
        "macOS")
            brew services start redis
            ;;
    esac
    
    log "Redis setup completed"
}

# Setup Docker
setup_docker() {
    log "Setting up Docker..."
    
    case $OS in
        "Debian/Ubuntu"|"Linux")
            sudo systemctl start docker
            sudo systemctl enable docker
            sudo usermod -aG docker $USER
            sudo usermod -aG docker "$USER"
            ;;
        "macOS")
            log "Please start Docker Desktop manually"
            ;;
    esac
    
    log "Docker setup completed"
}

# Create Python virtual environment
create_venv() {
    log "Creating Python virtual environment..."
    
    if [ ! -d "venv" ]; then
        $PYTHON_CMD -m venv venv
        python3 -m venv venv
        log "Virtual environment created"
    else
        log "Virtual environment already exists"
    fi
    

    # Activate virtual environment
    # shellcheck source=/dev/null
    source venv/bin/activate
    

    # Upgrade pip
    pip install --upgrade pip
    log "Virtual environment activated and pip upgraded"
}

# Install Python dependencies
install_python_deps() {
    log "Installing Python dependencies..."
    
    # Make sure we're in virtual environment
    if [[ "$VIRTUAL_ENV" == "" ]]; then
        # shellcheck source=/dev/null
        source venv/bin/activate
    fi
    
    # Install requirements
    pip install -r requirements.txt
    
    # Install additional security tools via pip
    pip install 
        bandit 
        safety 
        semgrep 
        truffleHog 
        gitpython
    
    log "Python dependencies installed"
}

# Install additional penetration testing tools
install_pentest_tools() {
    log "Installing additional penetration testing tools..."
    
    # Create tools directory
    mkdir -p tools
    cd tools
    
@@ -367,50 +322,77 @@ setup_kubernetes() {
            curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
            chmod +x kubectl
            sudo mv kubectl /usr/local/bin/
            ;;
        "macOS")
            brew install kubectl
            ;;
    esac
    
    # Install Helm
    case $OS in
        "Debian/Ubuntu"|"Linux")
            curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
            echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
            sudo apt-get update
            sudo apt-get install helm
            ;;
        "macOS")
            brew install helm
            ;;
    esac
    
    log "Kubernetes tools installed"
}

# Install Ollama with checksum verification
install_ollama() {
    log "Installing Ollama for local AI support..."

    case $OS in
        "Debian/Ubuntu"|"Linux")
            OLLAMA_VERSION="0.11.10"
            OLLAMA_ARCHIVE="ollama-linux-amd64.tgz"
            curl -L -o "$OLLAMA_ARCHIVE" "https://github.com/ollama/ollama/releases/download/v${OLLAMA_VERSION}/${OLLAMA_ARCHIVE}"
            curl -L -o sha256sum.txt "https://github.com/ollama/ollama/releases/download/v${OLLAMA_VERSION}/sha256sum.txt"
            grep "$OLLAMA_ARCHIVE" sha256sum.txt | sha256sum -c -
            sudo tar -C /usr/local -xzf "$OLLAMA_ARCHIVE"
            rm "$OLLAMA_ARCHIVE" sha256sum.txt
            ;;
        "macOS")
            if command -v brew &> /dev/null; then
                brew install ollama/tap/ollama
            else
                warn "Homebrew not found. Install Ollama manually from https://github.com/ollama/ollama/releases"
            fi
            ;;
        *)
            warn "Automatic Ollama installation not supported on $OS. Please install manually from https://github.com/ollama/ollama/releases"
            ;;
    esac
}

# Create configuration files
create_config_files() {
    log "Creating configuration files..."
    
    # Create config.ini if it doesn't exist
    if [ ! -f "config.ini" ]; then
        cat > config.ini << 'EOF'
[app]
debug = false
log_level = INFO

[database]
url = postgresql://hackgpt:hackgpt123@localhost:5432/hackgpt

[cache]
redis_url = redis://localhost:6379/0

[ai]
openai_api_key = 
local_model = llama2:7b

[security]
secret_key = 
jwt_algorithm = HS256
jwt_expiry = 3600
@@ -566,106 +548,93 @@ download_resources() {
        wget -q https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt -O common-dirs.txt || warn "Failed to download directory list"
    fi
    
    cd ..
    
    # Download AI models if needed
    if command -v ollama &> /dev/null; then
        log "Ollama detected, pulling AI models..."
        ollama pull llama2:7b 2>/dev/null || warn "Failed to pull AI model"
    fi
    
    log "Resource download completed"
}

# Final setup and testing
final_setup() {
    log "Performing final setup and testing..."
    
    # Make scripts executable
    chmod +x hackgpt.py hackgpt_v2.py install.sh usage_examples.sh
    
    # Test installation
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        python3 test_installation.py || warn "Installation test failed"
    fi
    

    # Create global command
    sudo ln -sf "$(pwd)/hackgpt.py" /usr/local/bin/hackgpt || warn "Failed to create global command"

    log "Final setup completed"
}

# Main installation process
main() {
    log "Starting HackGPT Enterprise installation..."
    
    # Check requirements
    check_python
    
    # Install system dependencies
    install_system_deps
    
    # Setup services
    setup_postgresql
    setup_redis
    setup_docker
    
    # Setup Python environment
    create_venv
    install_python_deps
    
    # Install additional tools
    install_pentest_tools
    setup_kubernetes
    
    install_ollama

    # Create configuration
    create_config_files
    setup_database_schema
    

    # Download resources
    download_resources
    
    # Final setup
    final_setup
    
    log "Installation completed successfully!"
    echo
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                    INSTALLATION COMPLETE                     ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo
    echo -e "${CYAN}Next steps:${NC}"
    echo -e "  1. Copy ${YELLOW}.env.example${NC} to ${YELLOW}.env${NC} and configure your API keys"
    echo -e "  2. Edit ${YELLOW}config.ini${NC} to customize settings"
    echo -e "  3. Activate the virtual environment: ${YELLOW}source venv/bin/activate${NC}"
    echo -e "  4. Run HackGPT: ${YELLOW}python3 hackgpt_v2.py${NC}"
    echo -e "  5. Or use the original version: ${YELLOW}python3 hackgpt.py${NC}"
    echo
    echo -e "${BLUE}API Server:${NC} ${YELLOW}python3 hackgpt_v2.py --api${NC}"
    echo -e "${BLUE}Web Dashboard:${NC} ${YELLOW}python3 hackgpt_v2.py --web${NC}"
    echo -e "${BLUE}Direct Assessment:${NC} ${YELLOW}python3 hackgpt_v2.py --target <target> --scope <scope> --auth-key <key>${NC}"
    echo
    echo -e "${PURPLE}For enterprise features, ensure all services are running:${NC}"
    echo -e "  • PostgreSQL: ${YELLOW}sudo systemctl status postgresql${NC}"
    echo -e "  • Redis: ${YELLOW}sudo systemctl status redis${NC}"
    echo -e "  • Docker: ${YELLOW}sudo systemctl status docker${NC}"
    echo
    echo -e "${GREEN}Happy Hacking! 🚀${NC}"
}

# Run main installation
main "$@"

# Create symlink for global access
echo "[+] Creating global command..."
sudo ln -sf $(pwd)/hackgpt.py /usr/local/bin/hackgpt

echo ""
echo "✅ Installation Complete!"
echo ""
echo "Usage:"
echo "  ./hackgpt.py                    # Interactive mode"
echo "  ./hackgpt.py --web             # Web dashboard"
echo "  ./hackgpt.py --voice           # Voice command mode"
echo "  hackgpt                        # Global command (if symlink created)"
echo ""
echo "Set OpenAI API key (optional):"
echo "  export OPENAI_API_KEY='your-api-key-here'"
echo ""
