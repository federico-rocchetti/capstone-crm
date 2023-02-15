# CRM (Client Resource Manager)

Client Resource Manager is a web application designed to be used as a digital agenda to save all of your contacts, regardless of personal/business use since you can specifically save contacts under a "Type of Contact" category. All contacts can be customized with additional unlimited notes to remember for that contact which can include
dates, appointments, customer information/requests, and so on.

![alt text](https://github.com/federico-rocchetti/capstone-crm/blob/main/project/images/HomeCRM.png?raw=true)

![alt text](https://github.com/federico-rocchetti/capstone-crm/blob/main/project/images/LoginCRM.png?raw=true)

![alt text](https://github.com/federico-rocchetti/capstone-crm/blob/main/project/images/DashboardCRM.png?raw=true)

![alt text](https://github.com/federico-rocchetti/capstone-crm/blob/main/project/images/AddContactCRM.png?raw=true)

![alt text](https://github.com/federico-rocchetti/capstone-crm/blob/main/project/images/ContactCRM.png?raw=true)

## Technologies Used

* Python
* Flask
* SQLAlchemy
* PostgreSQL
* Bootstrap
* HTML
* CSS

## Features

* Navbar will change depending on the session status, if user is logged in or logged out will determine the contents of the Navbar and prompt for login/registration.
* User login/registration and session management.
* User can Add Contact with the following fields (Some optional) for each contact: Name, Contact Type, Email, Mobile Phone, Work Phone, Address, Company Name.
* Dashboard will display all of the user's added contacts with a short summary of key information on each contact, along with an option to Delete the contact.
* User can access the full information on each contact by clicking on the Info button on each contact in the Dashboard.
* In the individual contact page, user can Edit contact information, Delete contact, Add Notes for contact, and Edit/Delete notes for contact.