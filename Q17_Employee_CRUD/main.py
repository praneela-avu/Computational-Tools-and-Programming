from model import EmployeeModel
from view import EmployeeView
from controller import EmployeeController


model = EmployeeModel()
view = EmployeeView()

controller = EmployeeController(model, view)
controller.run()