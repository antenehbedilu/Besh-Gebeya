from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from firebase_admin import credentials, firestore, initialize_app
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
#import pandas as pd
import datetime

cred = credentials.Certificate('ipm-system-db.json')
default_app = initialize_app(cred) 
db = firestore.client()

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "anteneh": generate_password_hash("passwd"),
    "admin": generate_password_hash("passwd")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-demographic', methods=['POST', 'GET'])
@auth.login_required
def add_demographic():
    if request.method == 'POST':
        UUID = request.form['UUID']
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
        """         import uuid
        UUID = uuid.uuid4()
        UUID = str(UUID)  """    
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
@auth.login_required
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
@auth.login_required
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
@auth.login_required
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

@app.route('/guiding-assessment')
def guiding_assessment():
    return render_template('guiding-assessment.html')

@app.route('/add-smart-goal', methods=['POST', 'GET'])
@auth.login_required
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
@auth.login_required
def view_smart_goals():
    try:
        departments = db.collection('SMART_GOALS').get()
        return render_template('view-smart-goals.html', departments=departments)
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/delete-smart-goal/<string:departmentOf>')
@auth.login_required
def delete_smart_goals(departmentOf):
    try:
        db.collection('SMART_GOALS').document(departmentOf).delete()
        return redirect('/view-smart-goals')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/add-talent-assessment-month', methods=['POST', 'GET'])
@auth.login_required
def add_talent_assessment_month():
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
            db.collection(u'ASSESSMENT-MONTH').document(UUID).set({
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
            return redirect('/view-talent-assessments-month')
        except Exception as e:
            return f'An Error Occured: {e}'
    return render_template('add-talent-assessment-month.html')

@app.route('/add-talent-assessment-year', methods=['POST', 'GET'])
@auth.login_required
def add_talent_assessment_year():
    if request.method == 'POST':
        UUID = request.form['UUID']
        reviewDate = request.form['reviewDate'][0:4]
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
            db.collection(u'ASSESSMENT-YEAR').document(UUID).set({
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
            return redirect('/view-talent-assessments-year')
        except Exception as e:
            return f'An Error Occured: {e}'
    return render_template('add-talent-assessment-year.html')

@app.route('/view-talent-assessments-month', methods=['POST', 'GET'])
def view_talent_assessments_month():
    if request.method == 'POST':
        try:
            query = request.form['query']
            assessments = db.collection('ASSESSMENT-MONTH')
            assessments = assessments.where(u'UUID', u'==', query).stream()
            return render_template('view-talent-assessments-month.html', assessments=assessments)
        except Exception as e:
            return f'An Error Occured: {e}'
    else:
        try:
            assessments = db.collection('ASSESSMENT-MONTH').order_by(u'UUID').get()
            return render_template('view-talent-assessments-month.html', assessments=assessments)
        except Exception as e:
            return f'An Error Occured: {e}'

@app.route('/download-monthly-assessment')
@auth.login_required
def download_monthly_assessment():
    monthly_talent_assessment = db.collection('ASSESSMENT-MONTH')

    docs = monthly_talent_assessment.get()
    data = []

    for doc in docs:
        data.append(doc.to_dict())
        df = pd.DataFrame(data)
    
    path = datetime.datetime.now()
    path = path.strftime('%B_'+'%Y')
    path = f'Monthly_Talent_Assessment_of_{path}'

    df.to_csv(f'{path}.csv', index=False)
    file = f'{path}.csv'
    return send_file(file,as_attachment=True)
    
@app.route('/view-talent-assessments-year', methods=['POST', 'GET'])
@auth.login_required
def view_talent_assessments_year():
    if request.method == 'POST':
        try:
            query = request.form['query']
            assessments = db.collection('ASSESSMENT-YEAR')
            assessments = assessments.where(u'UUID', u'==', query).stream()
            return render_template('view-talent-assessments-year.html', assessments=assessments)
        except Exception as e:
            return f'An Error Occured: {e}'
    else:
        try:
            assessments = db.collection('ASSESSMENT-YEAR').order_by(u'UUID').get()
            return render_template('view-talent-assessments-year.html', assessments=assessments)
        except Exception as e:
            return f'An Error Occured: {e}'

@app.route('/download-yearly-assessment')
@auth.login_required
def download_yearly_assessment():
    yearly_talent_assessment = db.collection('ASSESSMENT-YEAR')

    docs = yearly_talent_assessment.get()
    data = []

    for doc in docs:
        data.append(doc.to_dict())
        df = pd.DataFrame(data)
    
    path = datetime.datetime.now()
    path = path.strftime('%B_'+'%Y')
    path = f'Yearly_Talent_Assessment_of_{path}'

    df.to_csv(f'{path}.csv', index=False)
    file = f'{path}.csv'
    return send_file(file,as_attachment=True)

@app.route('/delete-talent-assessments-month/<string:UUID>')
@auth.login_required
def delete_talent_assessments_month(UUID):
    try:
        db.collection('ASSESSMENT-MONTH').document(UUID).delete()
        return redirect('/view-talent-assessments-month')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/delete-talent-assessments-year/<string:UUID>')
@auth.login_required
def delete_talent_assessments_year(UUID):
    try:
        db.collection('ASSESSMENT-YEAR').document(UUID).delete()
        return redirect('/view-talent-assessments-year')
    except Exception as e:
        return f'An Error Occured: {e}'

@app.route('/view-employee-of-the-year', methods=['POST', 'GET'])
def view_employee_of_the_year():
	try:
	    employees = db.collection('ASSESSMENT-YEAR')
	    employees = employees.where(u'totalScore', u'>', 4.85).stream()
	    return render_template('view-employee-of-the-year.html', employees=employees)
	except Exception as e:
	    return f'An Error Occured: {e}'

@app.route('/view-employee-of-the-month', methods=['POST', 'GET'])
def view_employee_of_the_month():
	try:
	    employees = db.collection('ASSESSMENT-MONTH')
	    employees = employees.where(u'totalScore', u'>', 4.85).stream()
	    return render_template('view-employee-of-the-month.html', employees=employees)
	except Exception as e:
	    return f'An Error Occured: {e}'

@app.route('/docs', methods=['POST', 'GET'])
@auth.login_required
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    app.run(debug=True)