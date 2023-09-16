class CSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # 设置 X-Frame-Options 头部
        response['X-Frame-Options'] = 'SAMEORIGIN'
        
        # 设置 Content-Security-Policy 头部
        response['Content-Security-Policy'] = "frame-ancestors 'self';"
        
        return response
