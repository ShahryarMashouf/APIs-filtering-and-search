from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    score = 'ten'
