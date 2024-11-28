# **Crowd-Funding-With-Database**  

This project was developed as part of the **ITI 9-Month Program Track (AI & ML)**. Below is a description of the role of each file in the system:

---

## **File Descriptions**  

### **1. Query of Database**  
This file contains the **SQL queries** required to create and manage the database for the system. It ensures that the necessary tables and relationships are properly defined and initialized.

---

### **2. Register**  
This file handles:  
- **Data collection** during user registration.  
- Ensuring that the user’s input adheres to the **required format and validation rules**.  

---

### **3. MyData**  
This file is responsible for:  
- **Securely saving** the registered user data into the database.  
- Ensuring the efficiency of database operations related to user information.  

---

### **4. Login**  
This file facilitates the **user login process** by:  
- Verifying the user's credentials.  
- Granting access to the system upon successful authentication.  

---

### **5. Project**  
This file manages functionalities related to projects, including:  
- Displaying a **list of the user's projects**.  
- Adding **new projects**.  
- Managing **existing projects** (view, update, delete).  
- Viewing all **available projects**.  
- Searching projects based on:  
  - **Start date**.  
  - **End date**.  

---

### **6. Main**  
This is the **entry point** of the system. It:  
- Integrates the functionalities of all other files.  
- Provides a user-friendly interface for interacting with the system.  

---

## **System Requirements**  

To successfully run this system, follow the steps below:  

1. **Install Python**  
   - Ensure Python is installed on your machine. You can use an editor like **VS Code** for development.

2. **Set up a Database Management System (DBMS)**  
   - Use **MySQL** or any other compatible DBMS.  

3. **Install Necessary Python Libraries**  
   - Install the **MySQL connector**:  
     ```bash
     pip install mysql-connector-python
     ```  
   - Install the **re module** for regular expressions:  
     ```bash
     pip install re
     ```  
   - Install the **os module** for operating system-related functions:  
     ```bash
     pip install os
     ```  

