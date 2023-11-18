from flask import Flask, Response, request
import pdfkit

app = Flask(__name__)

@app.route('/generate-pdf/grade-calculator', methods=["POST"])
def generateGradeCalculatorPdf():
  body = request.get_json()
  print(body)
  courseData = ""
  for course in body["grades"]:
    courseData += f"""
      <tr>
        <tr>
          <td style="border: 1px solid black">{course["courseName"]}</td>
          <td style="border: 1px solid black">{course["credit"]}</td>
          <td style="border: 1px solid black">{course["grade"]}</td>
        </tr>
      </tr>
    """

  html = f"""
    <html>
      <body>
        <h1>Grade calculator</h1>
        <p>Name: {body["name"]}</p>
        <p>Total credit attempted: {body["credits"]}</p>
        <p>GPA: {body["GPA"]}</p>
        <table style="border: 1px solid black">
          <tr>
            <th style="border: 1px solid black">Courese Name</th>
            <th style="border: 1px solid black">Credit</th>
            <th style="border: 1px solid black">Grade</th>
          </tr>
          {courseData}
        </table>
      </body>
    </html>
  """
  pdf = pdfkit.from_string(html, False)

  headers = {
    'Content-Type': 'application/pdf',
    'Content-Disposition': f"attachment;filename=gradeCalcultor.pdf"
  }

  response = Response(pdf, headers=headers)
  return response

@app.route("/generate-pdf/grade-assessment", methods=["POST"])
def generateGradeAssessmentPdf():
  body = request.get_json()
  print(body)
  gradeSummary = ""
  for grade in body["grades"]:
    gradeSummary += f"""
      <tr>
        <td style="border: 1px solid black">{grade["gradeLetter"]}</td>
        <td style="border: 1px solid black">{grade["ceiling"]}</td>
        <td style="border: 1px solid black">{grade["floor"]}</td>
        <td style="border: 1px solid black">{grade["count"]}</td>
      </tr>
    """
  
  studentData = ""
  for student in body["students"]:
    studentData += f"""
      <tr>
        <td style="border: 1px solid black">{student["name"]}</td>
        <td style="border: 1px solid black">{student["score"]}</td>
        <td style="border: 1px solid black">{student["grade"]}</td>
      </tr>
    """

  html = f"""<html>
                <body>
                  <h1>Grade assessment</h1>
                  <p>Course: {body["course"]}</p>
                  <p>Instrutor: {body["name"]}</p>
                  <p>Grade Average: {body["gradeAverage"]}</p>
                  <h2>Grade Summary</h2>
                  <table style="border: 1px solid black">
                    <tr>
                      <th style="border: 1px solid black">Grade letter</th>
                      <th style="border: 1px solid black">Min</th>
                      <th style="border: 1px solid black">Max</th>
                      <th style="border: 1px solid black">Count</th>
                    </tr>
                    {gradeSummary}
                  </table>
                  <h2>Student Summary</h2>
                  <table style="border: 1px solid black">
                    <tr>
                      <th style="border: 1px solid black">Name</th>
                      <th style="border: 1px solid black">Score</th>
                      <th style="border: 1px solid black">Grade</th>
                    </tr>
                    {studentData}
                  </table>
                </body>
              </html>"""
  pdf = pdfkit.from_string(html, False)

  headers = {
    'Content-Type': 'application/pdf',
    'Content-Disposition': f"attachment;filename=gradeAssessment.pdf"
  }

  response = Response(pdf, headers=headers)
  return response

app.run()