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

@app.route('/evaluation-criteria')
def evaluation_criteria():
    return render_template('evaluation-criteria.html')

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
            return redirect('/view-smart-goals')
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

@app.route('/delete-smart-goal/<string:departmentOf>')
def delete_smart_goals(departmentOf):
    try:
        db.collection('SMART_GOALS').document(departmentOf).delete()
        return redirect('/view-smart-goals')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/add-talent-assessment', methods=['POST', 'GET'])
def add_talent_assessment():
    if request.method == 'POST':
        UUID = request.form['UUID']
        reviewDate = request.form['reviewDate']
        jobKnowledge = request.form['jobKnowledge']
        qualityOfWork = request.form['qualityOfWork']
        accountability = request.form['accountability']
        attitudeRespectfulness = request.form['attitudeRespectfulness']
        punctualityAttendance = request.form['punctualityAttendance']
        policyProcedure = request.form['policyProcedure']
        compellationOfAssignment = request.form['compellationOfAssignment']
        confidentiality = request.form['confidentiality']
        acceptsCriticism = request.form['acceptsCriticism']
        appearanceOfWorkArea = request.form['appearanceOfWorkArea']
        comment = request.form['comment']
        total = int(jobKnowledge) + int(qualityOfWork) + int(accountability) + int(attitudeRespectfulness) + int(punctualityAttendance) + int(policyProcedure) + int(compellationOfAssignment) + int(confidentiality) + int(acceptsCriticism) + int(appearanceOfWorkArea)
        total = float(total/10)
        def calPerformerStatus(total):
            if 1.00 >= total or total <= 1.44:
                status = 'Very Least'
                return status
            elif 1.45 >= total or total <= 2.44:
                status = 'Least'
                return status
            elif 2.45 >= total or total <= 3.44:
                status = 'Good'
                return status
            elif 3.45 >= total or total <= 4.44:
                status = 'Very Good'
                return status
            elif 4.45 >= total or total <= 5.00:
                status = 'Excellent'
                return status
        performerStatus = calPerformerStatus(total)
        try:
            db.collection(u'ASSESSMENT').document(UUID).set({
            u'UUID': UUID,
            u'reviewDate': reviewDate,
            u'jobKnowledge': jobKnowledge,
            u'qualityOfWork': qualityOfWork,
            u'accountability': accountability,
            u'attitudeRespectfulness': attitudeRespectfulness,
            u'punctualityAttendance': punctualityAttendance,
            u'policyProcedure': policyProcedure,
            u'compellationOfAssignment': compellationOfAssignment,
            u'confidentiality': confidentiality,
            u'acceptsCriticism': acceptsCriticism,
            u'appearanceOfWorkArea': appearanceOfWorkArea,
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

@app.route('/delete-talent-assessments/<string:UUID>')
def delete_talent_assessments(UUID):
    try:
        db.collection('ASSESSMENT').document(UUID).delete()
        return redirect('/view-talent-assessments')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/view-employee-of-the-year', methods=['POST', 'GET'])
def view_employee_of_the_year():
	try:
	    employees = db.collection('ASSESSMENT')
	    employees = employees.where(u'totalScore', u'>', 4.85).stream()
	    return render_template('view-employee-of-the-year.html', employees=employees)
	except Exception as e:
	    return f'An Error Occured: {e}'







if __name__ == '__main__':
    app.run(debug=True)