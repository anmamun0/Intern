


```python
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

## 1️⃣ Request in Django

When a user visits a URL, the browser sends an HTTP request to the server.
#### Django wraps this into a request object containing:
- Method: GET, POST, PUT, DELETE, etc.
- Path: The requested URL path (e.g., /home/)
- Headers: Browser and client info (User-Agent, Cookie, Authorization)
- GET Parameters: Query data from URL (?q=python)
- POST Data: Form submissions
- Cookies: Client-side cookies
- Meta: Server/environment info (REMOTE_ADDR, HTTP_HOST)

---


<br>
<br>

#  2️⃣ Request-Response Cycle in Django

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

---


<br>
<br>

# 3️⃣ Django HTTP Status Codes Guide

This guide explains **HTTP status codes** and how to use them in **Django**.

---

## 1️⃣ 1xx – Informational

**Meaning:** Request received, continuing process.  

**Common codes:**
- `100 Continue`
- `101 Switching Protocols`  

## 2️⃣ 2xx – Success

**Meaning:** Request was successfully received, understood, and accepted.  

**Common codes:**
- `200 OK` → Standard success
- `201 Created` → New resource created
- `202 Accepted` → Request accepted but not processed yet
 
## 3️⃣ 3xx – Redirection 
**Meaning:** Client must take additional action to complete the request (usually follow another URL).  

**Common codes:**
- `301 Moved Permanently` → URL has changed permanently  
- `302 Found` → Temporary redirect  
- `304 Not Modified` → Cached version is valid  

## 4️⃣ 4xx – Client Error

**Meaning:** The client sent a bad request.  
**Common codes:**
- `400 Bad Request` → Invalid syntax or missing data  
- `401 Unauthorized` → Authentication required  
- `403 Forbidden` → Access denied  
- `404 Not Found` → Resource not found  
 

## 5️⃣ 5xx – Server Error

**Meaning:** Server failed to fulfill a valid request.  
**Common codes:**
- `500 Internal Server Error` → Generic server error  
- `502 Bad Gateway` → Invalid response from upstream server  
- `503 Service Unavailable` → Server overloaded or down  
 
Every response in Django comes with an HTTP status code.

| Code | Meaning                    | Example in Django                         |
| ---- | -------------------------- | ----------------------------------------- |
| 200  | OK                         | `HttpResponse("Success")`                 |
| 301  | Moved Permanently          | `HttpResponseRedirect("/new-url/")`       |
| 302  | Found / Temporary Redirect | `HttpResponseRedirect("/temp-url/")`      |
| 400  | Bad Request                | `HttpResponseBadRequest("Missing data")`  |
| 403  | Forbidden                  | `HttpResponseForbidden("Access denied")`  |
| 404  | Not Found                  | `HttpResponseNotFound("Page not found")`  |
| 500  | Internal Server Error      | `HttpResponseServerError("Server error")` |


| Class | Range   | Meaning       |
| ----- | ------- | ------------- |
| 1xx   | 100–199 | Informational |
| 2xx   | 200–299 | Success       |
| 3xx   | 300–399 | Redirection   |
| 4xx   | 400–499 | Client Error  |
| 5xx   | 500–599 | Server Error  |
