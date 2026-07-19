# configuration errors
class MissingSecretKey(Exception):pass
class MissingDatabaseURL(Exception):pass
class MissingCorsOrigins(Exception):pass
class MissingJWTSecretKey(Exception):pass

# Database records retrival errors
class StoreNotFoundError(Exception):pass
class ProductNotFoundError(Exception):pass

# Payment errors
class PaymentInitiationError(Exception):pass
class PaymentVerificationError(Exception):pass