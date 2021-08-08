import pandas as pd
import matplotlib.pyplot as plt

list_app = ["wordpress", "moodle", "laravel", "matomo", "phpunit"]
# for ApplicationName in list_app:
#     # ApplicationName = "laravel"
#
#     smells_data = pd.read_csv("C:/Project/statiqueProject/results/Commits_Analysis_" + ApplicationName + ".csv",
#                               index_col=0, parse_dates=True)
#     smells_data.plot(title="Évolution des codes puants du projet '" + ApplicationName + "'", xlabel = "#Commit")

smells_data = pd.read_csv("C:/Project/statiqueProject/results/R1/Analysis_projects_test.csv",
                          index_col=0, parse_dates=True)
smells_data = smells_data.astype(float)
smells_data.plot(title="Évolution des codes puants des projet ", xlabel = "#Commit")

plt.savefig("C:/Project/statiqueProject/Results/R1/Allprojects TESTS")