# FlaskTask-AWS
FlaskTask AWS is a cloud-powered to-do list application built using Flask, EC2, and RDS on AWS. It provides a simple and efficient way to manage tasks while leveraging AWS infrastructure for scalability and reliability. 🚀

## Features
- Add, edit, and delete tasks
- Track when a task was created and completed
- Store tasks in an RDS (MySQL) database
- Deployed on an AWS EC2 instance
- Modern UI using Bootstrap

## Prerequisites
- AWS Account
- EC2 instance (Amazon Linux)
- RDS MySQL Database
- Python 3 & Flask installed
- GitHub Repository

## Setup Instructions

### 1️⃣ **Set Up AWS EC2 Instance**
1. Launch an **Amazon Linux 2023** EC2 instance.
2. Connect via SSH or AWS CloudShell.

### 2️⃣ **Install Required Packages**
```bash
sudo yum update -y
sudo yum install git python3-pip mysql57 -y
```

### 3️⃣ **Clone the Repository & Set Up Virtual Environment & Install Python Dependencies**
```bash
git clone https://github.com/MarriKarunyaReddy/FlaskTask-AWS.git
cd FlaskTask-AWS
python3 -m venv venv
source venv/bin/activate
pip3 install flask
pip3 install flask-mysql
pip3 install pymysql
```

### 4️⃣ **Set Up MySQL RDS Database**
1. Create an RDS MySQL instance.
2. Connect from EC2:
   ```bash
   mysql -h <RDS-ENDPOINT> -u admin -p
   ```
3. Create database and table:
   ```sql
   CREATE DATABASE todo_db;
   USE todo_db;
   CREATE TABLE todos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       task VARCHAR(255) NOT NULL,
       status ENUM('pending', 'completed') DEFAULT 'pending',
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       completed_at TIMESTAMP NULL
   );
   ```

### 5️⃣ **Update Database Configuration**
Modify `app.py` with the correct RDS credentials:
```python
DB_HOST = "<RDS-ENDPOINT>"
DB_USER = "admin"
DB_PASSWORD = "yourpassword"
DB_NAME = "todo_db"
```

### 6️⃣ **Run the Flask App**
```bash
source venv/bin/activate
python3 app.py
```

### 7️⃣ **Access the App**
- Open a browser and visit: `http://<EC2-PUBLIC-IP>:5000`

## Stopping AWS Resources (To Avoid Charges)
```bash
aws ec2 stop-instances --instance-ids <EC2-ID>
aws rds stop-db-instance --db-instance-identifier <RDS-ID>
```

## Future Improvements
- Authentication & user-specific tasks
- Task priority levels
- CloudWatch logging & monitoring

---
🛠 **Developed by Marri Karunya Reddy**

