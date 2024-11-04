import os
from Model.schedule_Model import ScheduleModel

class ScheduleViewModel:
    _instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ScheduleViewModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.model = ScheduleModel()
        self.data = self.model.get_data()
        self.schedule = self.extract_schedule()

    def extract_schedule(self):
        schedule = {
            "Lunes": {},
            "Martes": {},
            "Miercoles": {},
            "Jueves": {},
            "Viernes": {},
            "Sábado": {}
        }

        for day, times in self.data.items():
            if day in schedule:
                for time, details in times.items():
                    # Eliminar los corchetes, comillas simples y guiones de los valores obtenidos
                    time = time.replace("-", "")
                    for key, value in details.items():
                        details[key] = str(value).replace("[", "").replace("]", "").replace("'", "")
                    schedule[day][time] = details

        return schedule

    def get_schedule(self):
        return self.schedule

    def get_day_schedule(self, day):
        return self.schedule.get(day, {})

# Ejemplo de uso
#if __name__ == "__main__":
 #   view_model = ScheduleViewModel()
  #  print("Horario del miércoles:", view_model.get_day_schedule("Miercoles"))
   # print("Horario del jueves:", view_model.get_day_schedule("Jueves"))
    #print("Horario del viernes:", view_model.get_day_schedule("Viernes"))