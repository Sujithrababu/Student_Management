# Student Management System

A lightweight Frappe app for managing student records through a custom `Student` DocType and server-side API methods.

## Overview

This project implements a simple Student Management module built on the Frappe Framework. It supports creating, reading, updating, deleting, listing, and counting student records, with basic validation handled at the DocType controller level.

## Implemented Features

- Custom `Student` DocType
- Student fields:
  - Student Name
  - Email
  - Age
  - Department
  - Status
- Student name-based document naming
- Unique student name validation
- Server-side validation for:
  - Mandatory student name
  - Age greater than zero
  - Basic email format check
- Document lifecycle hooks:
  - `validate`
  - `before_save`
  - `after_insert`
  - `on_update`
  - `on_trash`
- Whitelisted API methods for student operations
- Workflow master data fixtures for states and actions

## API Methods

The app includes the following whitelisted methods:

- `test_api` - Checks whether the API is working
- `create_student` - Creates a new student record
- `get_student` - Fetches a student by name
- `get_student_email` - Returns only the student email
- `update_student_status` - Updates the student status
- `delete_student` - Deletes a student record
- `get_all_students` - Lists all students
- `get_active_students` - Lists students with `Active` status
- `student_count` - Returns the total number of students

## Tech Stack

- Frappe Framework
- Python
- MariaDB/MySQL 

