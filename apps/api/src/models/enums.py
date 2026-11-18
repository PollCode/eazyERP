from enum import Enum


class BusinessType(str, Enum):
    market = "market"
    store = "store"
    pharmacy = "pharmacy"
    restaurant = "restaurant"
    bakery = "bakery"
    butcher = "butcher"
    other = "other"


class TenantPlan(str, Enum):
    free = "free"
    basic = "basic"
    pro = "pro"
    business = "business"


class TenantStatus(str, Enum):
    trial = "trial"
    active = "active"
    suspended = "suspended"
    cancelled = "cancelled"
    
    
class UserRole(str, Enum):
    owner = "owner"
    admin = "admin"
    manager = "manager"
    cashier = "cashier"
    inventory = "inventory"
    viewer = "viewer"


class UserStatus(str, Enum):
    pending_verification = "pending_verification"
    active = "active"
    inactive = "inactive"
    suspended = "suspended"