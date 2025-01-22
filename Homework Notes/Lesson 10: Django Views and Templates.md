## URL Routing in Django  
-  Views are the core of the application.  

- Django looks at the incoming request URL and uses urls.py to select a view.  

-  The view from views.py  
    - Handle any incoming data in the request and copy it to the database through the model  
    - Retrieve data to put on the page from the database through the model.  
    - Produce the html that will become the response and return it to the browser.  

-   When Django receives an HTTP request, it parses it and uses some of the URl for routing purposes and some gets passed to your code.  

-  Three patterns for views:  
    - Requests are routed to pre-defined Django classes.  
    - Requests are routed to a function in views.py that takes the http request as a parameter and returns a response.  
    - Requests are routed to a class in views.py that has get() and post() methods that take the http request as a parameter and return a response.  

## Django Views  
- To avoid conflicts, templates are stored in appname/templates/appname/  

- Request object: Data coming in | Response object: Data the application produces in response.  
    - Request object is an object instance of class HttpRequest.  
    - Each view you write is responsible for instantiating, populating, and returning an HttpResponse.  
    - Typical usage is to pass the contents of the page, as a string or bytestring, to the HttpResponse constructor.  