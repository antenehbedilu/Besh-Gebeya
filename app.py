from flask import Flask, render_template, request, redirect, url_for, flash
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime

cred = credentials.Certificate('ipm-system-db.json')
default_app = initialize_app(cred) 
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-demographic', methods=['POST', 'GET'])
def add_demographic():
    if request.method == 'POST':
        fullName = request.form['fullName']
        gender = request.form['gender']
        dateOfBirth = request.form['dateOfBirth']
        #emailAddress = request.form['emailAddress']
        #phoneNo = request.form['phoneNo']
        employmentDate = request.form['employmentDate']
        department = request.form['department']
        position = request.form['position']
        grade = request.form['grade']
        lineManager = request.form['lineManager']    
        import uuid
        UUID = uuid.uuid4()
        UUID = str(UUID) 
        try:
            db.collection(u'DEMOGRAPHICS').document(UUID).set({
            u'UUID': UUID,
            u'fullName': fullName,
            u'gender': gender,
            u'dateOfBirth': dateOfBirth,
            #u'emailAddress': emailAddress,
            #u'phoneNo': phoneNo,
            u'employmentDate': employmentDate,
            u'department': department,
            u'position': position,
            u'grade': grade,
            u'lineManager': lineManager})
            return redirect('/view-demographics')
        except Exception as e:
            return f'An Error Occured: {e}'
    return render_template('add-demographic.html')

@app.route('/view-demographics', methods=['POST', 'GET'])
def view_demographics():
    if request.method == 'POST':
        try:
            query = request.form['query']
            employees = db.collection('DEMOGRAPHICS')
            employees = employees.where(u'fullName', u'==', query).stream()
            return render_template('view-demographics.html', employees=employees)
        except Exception as e:
            return f'An Error Occured: {e}'
    else:
        try:
            employees = db.collection('DEMOGRAPHICS').order_by(u'UUID').get()
            return render_template('view-demographics.html', employees=employees)
        except Exception as e:
            return f'An Error Occured: {e}'

@app.route('/update-demographic/<string:UUID>', methods=['POST', 'GET'])
def update_demographic(UUID):
    employees = db.collection('DEMOGRAPHICS')
    employees = employees.where(u'UUID', u'==', UUID).stream()
    if request.method == 'POST':
        fullName = request.form['fullName']
        gender = request.form['gender']
        dateOfBirth = request.form['dateOfBirth']
        #emailAddress = request.form['emailAddress']
        #phoneNo = request.form['phoneNo']
        employmentDate = request.form['employmentDate']
        department = request.form['department']
        position = request.form['position']
        grade = request.form['grade']
        lineManager = request.form['lineManager'] 
        try:
            db.collection('DEMOGRAPHICS').document(UUID).update({u'fullName': fullName,u'gender': gender, u'dateOfBirth': dateOfBirth, u'employmentDate': employmentDate, u'department':department, u'position': position,u'grade':grade,u'lineManager':lineManager})
            return redirect('/view-demographics')
        except:
            return 'There was an issue updating employee'
    else:
        return render_template('update-demographic.html', employees=employees)

@app.route('/delete-demographic/<string:UUID>')
def delete_demographic(UUID):
    try:
        db.collection('DEMOGRAPHICS').document(UUID).delete()
        return redirect('/view-demographics')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/rating-scale')
def rating_scale():
    return render_template('rating-scale.html')

@app.route('/add-smart-goal', methods=['POST', 'GET'])
def add_smart_goal():
    if request.method == 'POST':
        departmentOf = request.form['departmentOf']
        businessObjectives = request.form['businessObjectives']
        distributionCoverage = request.form['distributionCoverage']
        peopleManagement = request.form['peopleManagement']
        customerDistributorManagement = request.form['customerDistributorManagement']
        financialResourcesManagement = request.form['financialResourcesManagement']
        try:
            db.collection(u'SMART_GOALS').document(departmentOf).set({
            u'departmentOf': departmentOf,
            u'businessObjectives': businessObjectives,
            u'distributionCoverage': distributionCoverage,
            u'peopleManagement': peopleManagement,
            u'customerDistributorManagement': customerDistributorManagement,
            u'financialResourcesManagement': financialResourcesManagement})
            return redirect('/smart_goals')
        except Exception as e:
            return f'An Error Occured: {e}'
    return render_template('add-smart-goal.html')

@app.route('/view-smart-goals', methods=['POST', 'GET'])
def view_smart_goals():
    try:
        departments = db.collection('SMART_GOALS').get()
        return render_template('view-smart-goals.html', departments=departments)
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/add-talent-assessment', methods=['POST', 'GET'])
def add_talent_assessment():
    if request.method == 'POST':
        UUID = request.form['UUID']
        reviewDate = request.form['reviewDate']
        businessObjectives = request.form['businessObjectives']
        distributionCoverage = request.form['distributionCoverage']
        peopleManagement = request.form['peopleManagement']
        customerDistributorManagement = request.form['customerDistributorManagement']
        financialResourcesManagement = request.form['financialResourcesManagement']
        comment = request.form['comment']
        total = int(businessObjectives) + int(distributionCoverage) + int(peopleManagement) + int(customerDistributorManagement) + int(financialResourcesManagement)
        def calPerformerStatus(total):
            if 0 > total or total < 49:
                status = 'Under Performer'
            elif 50 > total or total < 69:
                status = 'Needs Development'
            elif 70 > total or total < 79:
                status = 'Full Performer'
            elif 80 > total or total < 89:
                status = 'Strong Performer'
            elif 90 > total or total < 100:
                status = 'Exceptional Performer'
            return status
        performerStatus = calPerformerStatus(total)
        try:
            db.collection(u'ASSESSMENT').document(UUID).set({
            u'UUID': UUID,
            u'reviewDate': reviewDate,
            u'businessObjectives': businessObjectives,
            u'distributionCoverage': distributionCoverage,
            u'peopleManagement': peopleManagement,
            u'customerDistributorManagement': customerDistributorManagement,
            u'financialResourcesManagement': financialResourcesManagement,
            u'comment': comment,
            u'totalScore': total,
            u'scores': performerStatus})
            return redirect('/view-talent-assessments')
        except Exception as e:
            return f'An Error Occured: {e}'
    return render_template('add-talent-assessment.html')

@app.route('/view-talent-assessments', methods=['POST', 'GET'])
def view_talent_assessments():
    try:
        assessments = db.collection('ASSESSMENT').get()
        return render_template('view-talent-assessments.html', assessments=assessments)
    except Exception as e:
        return f'An Error Occured: {e}'







if __name__ == '__main__':
    app.run(debug=True)