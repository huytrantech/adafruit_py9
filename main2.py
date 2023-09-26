
print("Hello LAB3")
import time
from scheduler import *

from task2 import *
from task3 import *

import view
# import physical
scheduler = Scheduler()
scheduler.SCH_Init()


# taskPhysical = physical.PhysicalTask()

app = view.AppTkinter('IoT Application')
# app.display_chart()
task2 = Task2(tkinter_app=app)
task3 = Task3(tkinter_app=app)

scheduler.SCH_Add_Task(task2.Task2_Run, 1000,2000)
scheduler.SCH_Add_Task(task3.Task3_Run, 3000,3000)
# scheduler.SCH_Add_Task(taskPhysical.soil_moisture,1000,5000)
# scheduler.SCH_Add_Task(taskPhysical.soil_temperature,1000,5000)
while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    app.run_app_update()
    time.sleep(0.1)
