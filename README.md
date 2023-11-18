# pdf-generator

Step1: pip3 install -r requirements.txt

Step2: python3 api.py

# Generate pdf for grade calculator

Method: POST

endpoint: /generate-pdf/grade-calculator

example request:

```
{
  "name": "Nitiwat Jongruktrakoon",
  "credits": 9,
  "GPA": "3.90",
  "grades": [
    {
      "courseName": "Software Defined System",
      "grade": "A",
      "credit": 3
    },
    {
      "courseName": "Software Architecture",
      "grade": "B+",
      "credit": 3
    },
    {
      "courseName": "Computer Security",
      "grade": "A",
      "credit": 3
    }
  ]
}
```

# Generate pdf for grade assessment

Method: POST

endpoint: /generate-pdf/grade-assessment

example request:

```
{
    "name": "Kunwadee",
    "course": "Software Defined System",
    "gradeAverage": 3.54,
    "grades": [
        {
            "gradeLetter": "A",
            "count": 10,
            "ceiling": 100,
            "floor": 80
        },
        {
            "gradeLetter": "B+",
            "count": 10,
            "ceiling": 80,
            "floor": 75
        },
        {
            "gradeLetter": "B",
            "count": 10,
            "ceiling": 75,
            "floor": 70
        },
        {
            "gradeLetter": "C+",
            "count": 10,
            "ceiling": 70,
            "floor": 65
        },
        {
            "gradeLetter": "C",
            "count": 10,
            "ceiling": 65,
            "floor": 60
        },
        {
            "gradeLetter": "D+",
            "count": 10,
            "ceiling": 60,
            "floor": 55
        },
        {
            "gradeLetter": "D",
            "count": 10,
            "ceiling": 55,
            "floor": 50
        },
        {
            "gradeLetter": "F",
            "count": 10,
            "ceiling": 50,
            "floor": 0
        }
    ],
    "students": [
        {
            "name": "Nitiwat Jongruktrakoon",
            "score": 50,
            "grade": "D"
        },
        {
            "name": "Pawasis",
            "score": 80,
            "grade": "A"
        }
    ]
}
```
