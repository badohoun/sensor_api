from datetime import date
import numpy as np
import sys

class VisitSensor:
    """
    Simulates a sensor at the entrance of a mall.

    Takes a mean and a standard deviation

    and returns the number of visitors that passed through

    a particular door on a given date

    """



    def __init__(self,avg_visit:int , std_visit:int) -> None :
        """Initialize sensor"""
        self.avg_visit = avg_visit
        self.std_visit = std_visit
    def simulate_visit(self,business_date:date) -> int:
        """"Simulate the number of person detected by the sensor during the day"""


        # Ensure reproductibility of measurements
        np.random.seed(seed=business_date.toordinal())



        week_day = business_date.weekday()


        visit = np.random.normal(self.avg_visit , self.std_visit)

        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.25
        if week_day == 5:
            visit *= 1.35


        # If the business_date is a sunday the store is closed
        if week_day ==6:
            visit = -1


        return np.floor(visit)


if __name__ == "__main__":
    #print(sys.argv[1])
    #print(sys.argv[1].split("-"))
    if len(sys.argv) > 1 :
        year,month,day = [int(v) for v in sys.argv[1].split("-")]
    else:
        year,month,day = 2023,10, 25
    queried_date = date(year,month,day)
    capteur = VisitSensor(1500, 150)
    #print(capteur.simulate_visit(date(year=2023, month=10,day=25)))
    print(capteur.simulate_visit(queried_date))
