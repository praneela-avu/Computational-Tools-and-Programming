from model import StudentModel
from view import StudentView
from controller import StudentController


model = StudentModel()
view = StudentView()

controller = StudentController(model, view)
controller.run()
