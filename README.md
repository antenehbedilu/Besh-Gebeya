# Besh-Gebeya 

## Performance Management

### Init

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip3 install -U flask firebase_admin
$ pip list
$ touch app.py README.md
$ mkdir templates && cd templates
$ touch index.html base.html add-demographic.html view-demographics.html update-demographic.html add-smart-goal.html view-smart-goals.html update-smart-goal.html rating-scale.html add-talent-assessment.html view-talent-assessments.html update-talent-assessment.html view-employee-of-the-year.html
$ cd ..
```

### Deployment 

```python
$ pip3 install -U gunicorn
$ echo 'web: gunicorn app:app' >> Procfile
$ pip3 freeze > requirements.txt && pip3 freeze
$ heroku login -i
$ heroku create beshgebeya-pm
$ git remote -v
$ git push heroku master
$ heroku logs --app beshgebeya-pm
$ heroku logs -t
$ heroku open
```

### Department

```
CEO office

Category Department 

Marketing Department

Warehouse, Logistic & Inventory Dept.

Modern Trade Dept.

South, East, West Dept.

RS North Dept.

RS W/S Dept.

RS Retail Dept.

Cement & Construction Dept.

Finance Operation Dept.

ICT Department

Admin & Facility Dept.

HR Department
```

### LineManager

```
CEO office

Operation Unit

FMCG Unit

Construction Unit

Finance Unit

Human Resource Unit

Export Division
```
```
Category Department 

Marketing Department

Warehouse, Logistic & Inventory Dept.

Modern Trade Dept.

South, East, West Dept.

RS North Dept.

RS W/S Dept.

RS Retail Dept.

Cement & Construction Dept.

Finance Operation Dept.

ICT Department

Admin & Facility Dept.

HR Department
```

### Position/Job Title

```
Janitor
Security
Messenger/Photocopy
Check Point Security 
Deriver/ Van Deriver 
Security  Guard Head
Graduate Trainee 
Junior Accountant I
Direct Sales Assistant 
In Store Sales Assistant (Besh )
In Store Wear House Clark  (Bash )
Branch Wear House Supervisor
Main Wear  House Clark 
Data Encoder 
Sales Cashier 
Motorist/ Liaison Officer
Online Sales Officer
Call Cennter Oprator 
Junior Accountant II
Instore waerhous clerk II /Branch
Secretary & Archivist
Receptionist
ICT support Officer
Sorousing officer 
Main Cashier
Facility Purchaser
Employee Ingagement Officer
Accountant I
Market Intelegence Officer 
Sales & Deriver 
Customer Service Assistant 
Accountant II
Category Officer
Main Warehouse Supervisor
Market Intelligence & Pricing Officer
In store /Direct Sales Supervisor 
Quality Controle
Instore Warehouse supervisor
DATA/MIS Analyst
E-commerce Supervisor
Senior Accountant I
Import logistics Supervisor
Trade Marketing Officer
Fleet Supervisor
Record Managemet Spesialist
Project Supervisor
Employee Relation Officer (data management)
Market Intelligence & pricing Manager
Compensation and Benefit specialist
Senior Accountant II
Executive assistant ( PA)
Cash and Carry Store Manager
Cash & Carry Area Sales Manager
Main Warehouse Manager
Area Sales Manager
Application Support Specialist
Network Administrator
Training and development S/Officer 
System Admininstrator
Logistics Manager
General Service Head
Sales Information Manager 
Category Manager
Key Account Manager
Treasury, Tax and Budget head 
General Account Head
Warehouse Inventory Manager
Trade Marketing Manager
Brand Manager
PR & Digital Marketing Manager
Warehouse Inventory & Lojestic  Manager
Project Manager
MIS Manager
Internal Auditor
Finance Manager (Project) 
Export Manager
Archaive Management Senior Expert
Regional Sales Manager 
Legal Officer
Senior  Category Manager
Senior Finance Manager
Senior Marketing  Manager
Senior  HR Manager
Senior Admin &Facility Manager
Senior E-commerc Project Manager
Senior ICT Manager
Senior Regional Sales Manager
Senior planning and Monitoring Manager
D/Costruction Officer
D/FMCG Officer
Project Manager
Legal Advisor
Executive Assistance
Chief HR Officer
Chef Finance Officer
Chef Planning & Montering Manager
Chef Operations Officer
Chef Executive Officer 
```

### Average of Evaluation Form

| Status     | Minimum | Maximum |
|------------|---------|---------|
| Excellent  | 4.45    | 5.00    |
| Very Good  | 3.45    | 4.44    |
| Good       | 2.45    | 3.44    |
| Least      | 1.45    | 2.44    |
| Very Least | 1.00    | 1.44    |

### Evaluation Criteria

| Criteria                   | Description                                                     |
|----------------------------|-----------------------------------------------------------------|
| Job Knowledge              | Knows their job and fulfills their JD to the fullest potential. |
| Quality of Work            | Is thorough, accurate, and neat in work.                        |
| Accountability             | Accepts responsibility for actions, answerable to consequences. |
| Attitude/Respectfulness    | Shows initiative, optimism, and politeness.                     |
| Punctuality & Attendance   | Is rarely absent, arrives punctually, works required hours.     |
| Policy & Procedure         | Follows the organization's policies and procedures.             |
| Compellation of Assignment | Successfully completes tasks and meets all deadlines.           |
| Confidentiality            | Does not discuss internal events with coworkers.                |
| Accepts criticism          | Has the ability to learn from suggestions and change behavior.  |
| Appearance of Work Area    | Keeps work area neat and orderly.                               |

### Guiding Assessment