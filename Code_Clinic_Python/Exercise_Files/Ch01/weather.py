# For ranges in time pull out the baramaetric pressure.
# Then determine whether is each value is

# 1. open files
# 2. read date
# 3. read time
# 3. read barametric
# 4. copy read data
#5.  paste data to new file.

class Weather:
    def __init__(self, date, time, pressure):
        self._date = date
        self._time = time
        self._pressure = pressure

    def date(self):
        return self._date

    def time(self):
        return self._time

    def pressure(self):
        return self._pressure


def main():
    # pass
    # code
        f = open(
        '/Users/sedsaid/Documents/Lessons/python_learning_path/Code_Clinic_Python/Exercise_Files/Ch01/resources/Environmental_Data_Deep_Moor_2012.txt', 'rt')
        for line in f:
            print(line.rstrip())
        f.closse()
        print('\ndone.')

if __name__ == "__main__":main()