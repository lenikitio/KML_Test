import os

project_name = input("Введите шифр проекта: ")

if os.path.isdir('.git') != True:
    os.system('git init')
    os.system(f'git remote add origin https://github.com/lenikitio/{project_name}.git')
    os.system('git branch -M main')
    os.system('git push -u origin main')
flights = "flight_data.kml"
points = "point_data.kml"
os.system(f'git add {flights}')
os.system(f'git add {points}')
os.system(f'git commit -m "flight"')
os.system('git push')