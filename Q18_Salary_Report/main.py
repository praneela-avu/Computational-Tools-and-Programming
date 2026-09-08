from model import SalaryModel
from view import SalaryView
from controller import SalaryController


model = SalaryModel()
view = SalaryView()

controller = SalaryController(model, view)
controller.run()
