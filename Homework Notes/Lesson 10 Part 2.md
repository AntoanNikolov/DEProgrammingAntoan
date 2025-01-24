## Using Templates in Django  
- Template render process  
    - The template with instructions on adding data into it (using curly brackets) is passed into the render engine, along with Render Data (usually a dictionary, provided in the views.py file as context). The Render Engine (a bit of code that puts the stuff together) then produces the html with data passed in it.  
- Slugs are special versions of strings that include letters, numbers, and dashes  

- A django project is made up of one or more applications in folders  

- It is common for different applications to use the same template names  
    - We use a technique called "namespace" to be able to do so (appname/templates/appname/)  

## Using the Django Template Language (DTL)  
- use {{ variable|safe }} to avoid automatic escaping of data