Install Modules
pip install > requirements.txt
pip install django djangorestframework djangorestframework-simplejwt

#https://staproject.pythonanywhere.com/api/
#https://staproject.pythonanywhere.com
#username:admin
#password:admin

I have tested on postman
https://staproject.pythonanywhere.com/api/login/
#username:admin
#password:admin

https://staproject.pythonanywhere.com/api/categories
body:
    name
    description

 output
 {
    "data": [
        {
            "id": 1,
            "name": "Electronics",
            "description": "Mobile, TV, AC Cooler, Freeze"
        },
        {
            "id": 2,
            "name": "Furniture",
            "description": "Wooden furniture"
        }
    ],
    "message": "Categories retrieved successfully."
}


http://127.0.0.1:8000/api/product/



#https://github.com/rajk9200/STAssignment

