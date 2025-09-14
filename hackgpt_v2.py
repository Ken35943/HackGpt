from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown

# Optional imports
requests = safe_import('requests')
openai = safe_import('openai')
flask = safe_import('flask')
redis = safe_import('redis')
psycopg2 = safe_import('psycopg2')
sqlalchemy = safe_import('sqlalchemy')
docker = safe_import('docker')
consul = safe_import('consul')
jwt = safe_import('jwt')
bcrypt = safe_import('bcrypt')
sr = safe_import('speech_recognition')
pyttsx3 = safe_import('pyttsx3')
numpy = safe_import('numpy')
pandas = safe_import('pandas')

# Import our custom modules
# Import our custom modules with feature flags
try:
    from database import get_db_manager, PentestSession, Vulnerability, User, AuditLog
    DB_AVAILABLE = True
except ImportError as e:
    print(f"Warning: database module not available: {e}")
    DB_AVAILABLE = False
    get_db_manager = PentestSession = Vulnerability = User = AuditLog = None

try:
    from ai_engine import get_advanced_ai_engine
    AI_AVAILABLE = True
except ImportError as e:
    print(f"Warning: AI engine module not available: {e}")
    AI_AVAILABLE = False
    get_advanced_ai_engine = None

try:
    from security import EnterpriseAuth, ComplianceFrameworkMapper
    SECURITY_AVAILABLE = True
except ImportError as e:
    print(f"Warning: security module not available: {e}")
    SECURITY_AVAILABLE = False
    EnterpriseAuth = ComplianceFrameworkMapper = None

try:
    from exploitation import AdvancedExploitationEngine, ZeroDayDetector
    EXPLOITATION_AVAILABLE = True
except ImportError as e:
    print(f"Warning: exploitation module not available: {e}")
    EXPLOITATION_AVAILABLE = False
    AdvancedExploitationEngine = ZeroDayDetector = None

try:
    from reporting import DynamicReportGenerator, get_realtime_dashboard
    REPORTING_AVAILABLE = True
except ImportError as e:
    print(f"Warning: reporting module not available: {e}")
    REPORTING_AVAILABLE = False
    DynamicReportGenerator = get_realtime_dashboard = None

try:
    from cloud import DockerManager, KubernetesManager, ServiceRegistry
    CLOUD_AVAILABLE = True
except ImportError as e:
    print(f"Warning: cloud module not available: {e}")
    CLOUD_AVAILABLE = False
    DockerManager = KubernetesManager = ServiceRegistry = None

try:
    from performance import get_cache_manager, get_parallel_processor
    MODULES_AVAILABLE = True
    PERFORMANCE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some modules not available: {e}")
    MODULES_AVAILABLE = False
    print(f"Warning: performance module not available: {e}")
    PERFORMANCE_AVAILABLE = False
    get_cache_manager = get_parallel_processor = None

# Initialize Rich Console
console = Console()

# Configuration
class Config:
    """Application configuration manager"""
    
    def __init__(self, config_file: str = "config.ini"):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.load_config()
        
        # Environment variables override config file
        self.DATABASE_URL = os.getenv("DATABASE_URL", self.config.get("database", "url", fallback="postgresql://hackgpt:hackgpt123@localhost:5432/hackgpt"))
        self.REDIS_URL = os.getenv("REDIS_URL", self.config.get("cache", "redis_url", fallback="redis://localhost:6379/0"))
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", self.config.get("ai", "openai_api_key", fallback=""))
        self.SECRET_KEY = os.getenv("SECRET_KEY", self.config.get("security", "secret_key", fallback=str(uuid.uuid4())))
        self.LDAP_SERVER = os.getenv("LDAP_SERVER", self.config.get("ldap", "server", fallback=""))
        self.LDAP_BIND_DN = os.getenv("LDAP_BIND_DN", self.config.get("ldap", "bind_dn", fallback=""))
        self.LDAP_BIND_PASSWORD = os.getenv("LDAP_BIND_PASSWORD", self.config.get("ldap", "bind_password", fallback=""))
        
        # Application settings
        self.DEBUG = self.config.getboolean("app", "debug", fallback=False)
        self.LOG_LEVEL = self.config.get("app", "log_level", fallback="INFO")
@@ -186,161 +229,161 @@ BANNER = """
[bold green]        Production-Ready | Cloud-Native | AI-Enhanced[/bold green]
[dim]                    Advanced Security Assessment Platform[/dim]
"""

class EnterpriseHackGPT:
    """Main HackGPT Enterprise Application"""
    
    def __init__(self):
        self.config = config
        self.console = Console()
        self.logger = logging.getLogger('hackgpt.main')
        
        # Initialize components
        self.initialize_components()
        
        # Initialize services
        self.initialize_services()
        
        # Setup signal handlers
        self.setup_signal_handlers()
        
    def initialize_components(self):
        """Initialize core components"""
        try:
            # Database
            if MODULES_AVAILABLE:
            if DB_AVAILABLE:
                self.db = get_db_manager()
                self.console.print("[green]✓[/green] Database connection initialized")
            else:
                self.db = None
                self.console.print("[yellow]⚠[/yellow] Database not available")
            

            # AI Engine
            if MODULES_AVAILABLE and (config.OPENAI_API_KEY or self.check_local_llm()):
            if AI_AVAILABLE and (config.OPENAI_API_KEY or self.check_local_llm()):
                self.ai_engine = get_advanced_ai_engine()
                self.console.print("[green]✓[/green] Advanced AI Engine initialized")
            else:
                self.ai_engine = self.create_fallback_ai()
                self.console.print("[yellow]⚠[/yellow] Using fallback AI engine")
            

            # Authentication
            if MODULES_AVAILABLE:
            if SECURITY_AVAILABLE:
                self.auth = EnterpriseAuth()
                self.console.print("[green]✓[/green] Enterprise authentication initialized")
            else:
                self.auth = None
                self.console.print("[yellow]⚠[/yellow] Authentication not available")
            

            # Cache Manager
            if MODULES_AVAILABLE:
            if PERFORMANCE_AVAILABLE:
                self.cache = get_cache_manager()
                self.console.print("[green]✓[/green] Cache manager initialized")
            else:
                self.cache = None
                self.console.print("[yellow]⚠[/yellow] Cache not available")
            

            # Parallel Processor
            if MODULES_AVAILABLE:
            if PERFORMANCE_AVAILABLE:
                self.processor = get_parallel_processor()
                self.console.print("[green]✓[/green] Parallel processor initialized")
            else:
                self.processor = None
                self.console.print("[yellow]⚠[/yellow] Parallel processing not available")
            
            # Tool Manager
            self.tool_manager = EnterpriseToolManager()
            self.console.print("[green]✓[/green] Enterprise tool manager initialized")
            
            # Compliance Framework
            if MODULES_AVAILABLE:
            if SECURITY_AVAILABLE:
                self.compliance = ComplianceFrameworkMapper()
                self.console.print("[green]✓[/green] Compliance framework initialized")
            else:
                self.compliance = None
                self.console.print("[yellow]⚠[/yellow] Compliance framework not available")
            

            # Exploitation Engine
            if MODULES_AVAILABLE:
            if EXPLOITATION_AVAILABLE:
                self.exploitation = AdvancedExploitationEngine()
                self.zero_day_detector = ZeroDayDetector()
                self.console.print("[green]✓[/green] Advanced exploitation engine initialized")
            else:
                self.exploitation = None
                self.zero_day_detector = None
                self.console.print("[yellow]⚠[/yellow] Advanced exploitation not available")
            

            # Reporting
            if MODULES_AVAILABLE:
            if REPORTING_AVAILABLE:
                self.report_generator = DynamicReportGenerator()
                self.console.print("[green]✓[/green] Dynamic report generator initialized")
            else:
                self.report_generator = BasicReportGenerator()
                self.console.print("[yellow]⚠[/yellow] Using basic report generator")
            
        except Exception as e:
            self.logger.error(f"Error initializing components: {e}")
            self.console.print(f"[red]Error initializing components: {e}[/red]")
    
    def initialize_services(self):
        """Initialize enterprise services"""
        try:
            # Cloud services
            if MODULES_AVAILABLE and docker:
            if CLOUD_AVAILABLE and docker:
                self.docker_manager = DockerManager()
                self.console.print("[green]✓[/green] Docker manager initialized")
            else:
                self.docker_manager = None
                self.console.print("[yellow]⚠[/yellow] Docker not available")
            
            if MODULES_AVAILABLE:

            if CLOUD_AVAILABLE:
                self.k8s_manager = KubernetesManager()
                self.service_registry = ServiceRegistry(backend=config.SERVICE_REGISTRY_BACKEND)
                self.console.print("[green]✓[/green] Cloud services initialized")
            else:
                self.k8s_manager = None
                self.service_registry = None
                self.console.print("[yellow]⚠[/yellow] Cloud services not available")
            
            # Voice interface
            if config.ENABLE_VOICE and sr and pyttsx3:
                self.voice_interface = EnterpriseVoiceInterface()
                self.console.print("[green]✓[/green] Voice interface initialized")
            else:
                self.voice_interface = None
                self.console.print("[yellow]⚠[/yellow] Voice interface not available")
            
            # Web dashboard
            if config.ENABLE_WEB_DASHBOARD and flask:
                self.web_dashboard = EnterpriseWebDashboard(self)
                self.console.print("[green]✓[/green] Web dashboard initialized")
            else:
                self.web_dashboard = None
                self.console.print("[yellow]⚠[/yellow] Web dashboard not available")
            
            # Real-time dashboard
            if config.ENABLE_REALTIME_DASHBOARD and MODULES_AVAILABLE:
            if config.ENABLE_REALTIME_DASHBOARD and REPORTING_AVAILABLE:
                self.realtime_dashboard = get_realtime_dashboard()
                self.console.print("[green]✓[/green] Real-time dashboard initialized")
            else:
                self.realtime_dashboard = None
                self.console.print("[yellow]⚠[/yellow] Real-time dashboard not available")
            
        except Exception as e:
            self.logger.error(f"Error initializing services: {e}")
            self.console.print(f"[red]Error initializing services: {e}[/red]")
    
    def check_local_llm(self):
        """Check if local LLM is available"""
        try:
            result = subprocess.run(['which', 'ollama'], capture_output=True, text=True)
            return result.returncode == 0
        except:
            return False
    
    def create_fallback_ai(self):
        """Create fallback AI engine"""
        class FallbackAI:
            def __init__(self):
                self.console = Console()
            
            def analyze(self, context, data, phase="general"):
@@ -359,51 +402,51 @@ class EnterpriseHackGPT:
    
    def setup_signal_handlers(self):
        """Setup graceful shutdown signal handlers"""
        import signal
        
        def signal_handler(signum, frame):
            self.logger.info(f"Received signal {signum}, shutting down gracefully...")
            self.shutdown()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    def show_banner(self):
        """Display the HackGPT banner with system status"""
        self.console.print(BANNER)
        
        # System status
        status_table = Table(title="System Status", show_header=True)
        status_table.add_column("Component", style="cyan")
        status_table.add_column("Status", style="green")
        status_table.add_column("Version", style="yellow")
        
        components = [
            ("Database", "✓ Connected" if self.db else "⚠ Not Available", "PostgreSQL"),
            ("AI Engine", "✓ Advanced" if MODULES_AVAILABLE else "⚠ Fallback", "ML-Enhanced"),
            ("AI Engine", "✓ Advanced" if AI_AVAILABLE else "⚠ Fallback", "ML-Enhanced"),
            ("Authentication", "✓ Enterprise" if self.auth else "⚠ Basic", "RBAC+LDAP"),
            ("Cache", "✓ Multi-Layer" if self.cache else "⚠ None", "Redis+Memory"),
            ("Parallel Processing", "✓ Available" if self.processor else "⚠ Sequential", f"{config.MAX_WORKERS} workers"),
            ("Cloud Services", "✓ Ready" if self.docker_manager else "⚠ Not Available", "Docker+K8s"),
            ("Compliance", "✓ Integrated" if self.compliance else "⚠ Manual", "OWASP+NIST"),
            ("Real-time Dashboard", "✓ Active" if self.realtime_dashboard else "⚠ Disabled", "WebSocket")
        ]
        
        for name, status, version in components:
            status_table.add_row(name, status, version)
        
        self.console.print(status_table)
    
    def show_main_menu(self):
        """Display enhanced main menu"""
        menu_table = Table(title="HackGPT Enterprise Main Menu", show_header=True)
        menu_table.add_column("Option", style="cyan", width=8)
        menu_table.add_column("Category", style="magenta", width=20)
        menu_table.add_column("Description", style="white")
        
        menu_options = [
            ("1", "Assessment", "Full Enterprise Pentest (All 6 Phases)"),
            ("2", "Assessment", "Run Specific Phase"),
            ("3", "Assessment", "Custom Assessment Workflow"),
            ("4", "Reporting", "View Reports & Analytics"),
