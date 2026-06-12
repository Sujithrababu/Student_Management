import frappe


# TEST API
@frappe.whitelist(allow_guest=True)
def test_api():

    return {
        "message": "API Working"
    }


# CREATE STUDENT
@frappe.whitelist(allow_guest=True)
def create_student(
    student_name,
    email,
    age,
    department,
    status
):

    try:

        student = frappe.new_doc("Student")

        student.student_name = student_name
        student.email = email
        student.age = int(age)
        student.department = department
        student.status = status

        student.insert(
            ignore_permissions=True
        )

        frappe.db.commit()

        return {
            "status": "success",
            "message": "Student Created Successfully",
            "student_id": student.name
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# GET STUDENT
@frappe.whitelist(allow_guest=True)
def get_student(student_name):

    try:

        student = frappe.get_doc(
            "Student",
            student_name
        )

        return {
            "student_name": student.student_name,
            "email": student.email,
            "age": student.age,
            "department": student.department,
            "status": student.status
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# GET EMAIL
@frappe.whitelist(allow_guest=True)
def get_student_email(student_name):

    email = frappe.db.get_value(
        "Student",
        student_name,
        "email"
    )

    return {
        "email": email
    }


# UPDATE STATUS
@frappe.whitelist(allow_guest=True)
def update_student_status(
    student_name,
    status
):

    frappe.db.set_value(
        "Student",
        student_name,
        "status",
        status
    )

    frappe.db.commit()

    return {
        "message": "Status Updated Successfully"
    }


# DELETE STUDENT
@frappe.whitelist(allow_guest=True)
def delete_student(student_name):

    frappe.delete_doc(
        "Student",
        student_name,
        ignore_permissions=True
    )

    frappe.db.commit()

    return {
        "message": "Student Deleted Successfully"
    }


# GET ALL STUDENTS
@frappe.whitelist(allow_guest=True)
def get_all_students():

    students = frappe.get_all(
        "Student",
        fields=[
            "student_name",
            "email",
            "age",
            "department",
            "status"
        ]
    )

    return students


# GET ACTIVE STUDENTS
@frappe.whitelist(allow_guest=True)
def get_active_students():

    students = frappe.get_all(
        "Student",
        filters={
            "status": "Active"
        },
        fields=[
            "student_name",
            "email",
            "department"
        ]
    )

    return students


# STUDENT COUNT
@frappe.whitelist(allow_guest=True)
def student_count():

    count = frappe.db.count(
        "Student"
    )

    return {
        "total_students": count
    }