


```
views.py
from django.http import HttpResponse

def my_view(request):
    # The full URL path the user requested
    path = request.path  # e.g., '/hello/'  
    # The full URL including domain
    full_path = request.get_full_path()  # e.g., '/hello/?q=django'
    # HTTP method (GET, POST, etc.)
    method = request.method  # e.g., 'GET'
    # GET parameters (from URL query string)
    get_params = request.GET  # e.g., QueryDict({'q': 'django'})
    # POST parameters (from form submission)
    post_params = request.POST  # e.g., QueryDict({'name': 'Mamun'})
    # HTTP headers
    headers = request.headers  # e.g., {'Host': 'localhost:8000', 'User-Agent': 'Chrome'}
    # Cookies
    cookies = request.COOKIES  # e.g., {'sessionid': 'abc123'}
    # User info (if using Django auth)
    user = request.user  # e.g., <User: admin>
    # META info (all server/environment info)
    meta = request.META  # e.g., {'REMOTE_ADDR': '127.0.0.1', 'HTTP_HOST': 'localhost:8000'}

    # Build a response to see everything
    response_text = f"""
    Path: {path}<br>
    Full Path: {full_path}<br>
    Method: {method}<br>
    GET Params: {get_params}<br>
    POST Params: {post_params}<br>
    Headers: {dict(headers)}<br>
    Cookies: {cookies}<br>
    User: {user}<br>
    META: {dict(list(meta.items())[:10])} ...<br> <!-- show only first 10 for brevity -->
    """

    return HttpResponse(response_text)
```

output
```html
Path: /hello/
Full Path: /hello/?q=django
Method: GET
GET Params: <QueryDict: {'q': ['django']}>
POST Params: <QueryDict: {}>
Headers: {'Host': 'localhost:8000', 'User-Agent': 'Mozilla/5.0 ...', ...}
Cookies: {}
User: <User: AnonymousUser>
META: {'REMOTE_ADDR': '127.0.0.1', 'HTTP_HOST': 'localhost:8000', ...} ...
```


```py
# views.py
from django.http import (
    HttpResponse, 
    HttpResponseBadRequest, 
    HttpResponseForbidden, 
    HttpResponseNotFound, 
    HttpResponseRedirect, 
    HttpResponseServerError
)

def test_responses(request):
    # Get 'type' parameter from URL
    response_type = request.GET.get('type', 'ok')  # default is 'ok'

    if response_type == 'ok':
        return HttpResponse("✅ This is a normal 200 OK response!")

    elif response_type == 'bad':
        return HttpResponseBadRequest("❌ 400 Bad Request! Missing or wrong data.")

    elif response_type == 'forbidden':
        return HttpResponseForbidden("⛔ 403 Forbidden! You cannot access this page.")

    elif response_type == 'notfound':
        return HttpResponseNotFound("❌ 404 Not Found! The page does not exist.")

    elif response_type == 'redirect':
        return HttpResponseRedirect("/another-page/")  # Redirects to another URL

    elif response_type == 'servererror':
        return HttpResponseServerError("💥 500 Internal Server Error! Something went wrong.")

    else:
        return HttpResponse("Unknown response type. Use ?type=ok|bad|forbidden|notfound|redirect|servererror")
```

🔹 Quick Reference 
<h6>

| Response Class            | Status Code | Use Case                |
| ------------------------- | ----------- | ----------------------- |
| `HttpResponse`            | 200         | Successful response     |
| `HttpResponseBadRequest`  | 400         | Client sent bad request |
| `HttpResponseForbidden`   | 403         | Access denied           |
| `HttpResponseNotFound`    | 404         | Resource not found      |
| `HttpResponseRedirect`    | 302         | Redirect to another URL |
| `HttpResponseServerError` | 500         | Server error            |
</h6>




## 2️⃣ Request-Response Cycle in Django

Django’s request-response cycle is the process from the moment the user sends a request to when Django returns a response.

Step by step:
- Browser sends request → User opens http://example.com/home/.
- URL routing → Django checks urls.py to find the matching view.
- Middleware processing → Optional pre-processing (authentication, logging, sessions, etc.).
- View function execution → Your function handles the request.
- Response returned → Django sends an HttpResponse back.
- Middleware post-processing → Optional modification of the response.
- Browser receives response → Page renders.
- Diagram (simplified):

```js
Browser ----> URL Resolver ----> Middleware (pre) ----> View ----> Middleware (post) ----> Browser
```