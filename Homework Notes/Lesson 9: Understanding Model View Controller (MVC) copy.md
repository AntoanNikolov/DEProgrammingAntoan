## Video  
- "In MVC, the model represents the information (the data) of the application and the business rules used to manipulate the data; the view orresponds to elements of the user interface such as text, checkbox items, and so forth; and the controller manages details involving the communication to the model of user actions." Model: Manage business-logic and data, View: Manage the presentation or the layout of the application, Controller: Connects Model with View, and routes request.  

- Tasks inside the server:  
    - Process user data (i.e. from a form) and store it  
    - Decide what to show the user  
    - Retrieve needed data  
    - Produce HTML response and send it to the browser  

- Views.py is both the controller (making decisions about where to go next) and the production (handling and sending data)  

- urls.py and some of views.py - controller, Models - model, parts of views.py - view  

- Default https port: 8443, default non-secure http port: 80  

## Article  
- Access data passed into the HTML file with double curly brackets  
- Django’s view actually acts as the controller function in typical MVC architecture, and the templates have a similar role as view in MVC.