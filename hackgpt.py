 import redis
    import psycopg2
    import sqlalchemy
    from celery import Celery
    import docker
    import kubernetes
    import consul
    import jwt
    import bcrypt
    from ldap3 import Server, Connection, ALL
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.cluster import DBSCAN
    from sklearn.ensemble import IsolationForest
    import websockets
    import aiohttp
except ImportError as e:
    print(f"Missing required package: {e}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

# Import our custom modules
# Import our custom modules with feature flags
# Database
try:
    from database import get_db_manager, PentestSession, Vulnerability, User, AuditLog
    DB_AVAILABLE = True
except ImportError as e:
    print(f"Warning: database module not available: {e}")
    DB_AVAILABLE = False
    get_db_manager = PentestSession = Vulnerability = User = AuditLog = None

# AI Engine
try:
    from ai_engine import get_advanced_ai_engine
    AI_AVAILABLE = True
except ImportError as e:
    print(f"Warning: AI engine module not available: {e}")
    AI_AVAILABLE = False
    get_advanced_ai_engine = None

# Security
try:
    from security import EnterpriseAuth, ComplianceFrameworkMapper
    SECURITY_AVAILABLE = True
except ImportError as e:
    print(f"Warning: security module not available: {e}")
    SECURITY_AVAILABLE = False
    EnterpriseAuth = ComplianceFrameworkMapper = None

# Exploitation
try:
    from exploitation import AdvancedExploitationEngine, ZeroDayDetector
    EXPLOITATION_AVAILABLE = True
except ImportError as e:
    print(f"Warning: exploitation module not available: {e}")
    EXPLOITATION_AVAILABLE = False
    AdvancedExploitationEngine = ZeroDayDetector = None

# Reporting
try:
    from reporting import DynamicReportGenerator, get_realtime_dashboard
    REPORTING_AVAILABLE = True
except ImportError as e:
    print(f"Warning: reporting module not available: {e}")
    REPORTING_AVAILABLE = False
    DynamicReportGenerator = get_realtime_dashboard = None

# Cloud management
try:
    from cloud import DockerManager, KubernetesManager, ServiceRegistry
    CLOUD_AVAILABLE = True
except ImportError as e:
    print(f"Warning: cloud module not available: {e}")
    CLOUD_AVAILABLE = False
    DockerManager = KubernetesManager = ServiceRegistry = None

# Performance optimizations
try:
    from performance import get_cache_manager, get_parallel_processor
    PERFORMANCE_AVAILABLE = True
except ImportError as e:
    print(f"Missing HackGPT modules: {e}")
    print("Please ensure all modules are properly installed")
    sys.exit(1)
    print(f"Warning: performance module not available: {e}")
    PERFORMANCE_AVAILABLE = False
    get_cache_manager = get_parallel_processor = None

# Initialize Rich Console
console = Console()

# Configuration
class Config:
    """Application configuration"""
    
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
