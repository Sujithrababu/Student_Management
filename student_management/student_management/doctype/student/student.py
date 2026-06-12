# Copyright (c) 2026, Sujithra and contributors

import frappe
from frappe.model.document import Document
from frappe.utils import cint


class Student(Document):

    def validate(self):

        # Student Name Validation
        if not self.student_name:
            frappe.throw("Student Name is mandatory")

        # Age Validation
        if cint(self.age) <= 0:
            frappe.throw(
                "Age must be greater than 0"
            )

        # Email Validation
        if self.email and "@" not in self.email:
            frappe.throw(
                "Please enter a valid Email Address"
            )

    def before_save(self):

        frappe.msgprint(
            "before_save() executed"
        )

    def after_insert(self):

        frappe.msgprint(
            "Student Record Created Successfully"
        )

    def on_update(self):

        frappe.msgprint(
            "Student Record Updated"
        )

    def on_trash(self):

        frappe.msgprint(
            "Student Record Deleted"
        )