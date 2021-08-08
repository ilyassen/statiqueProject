import pandas as pd
import matplotlib.pyplot as plt

list_app = ["wordpress", "moodle", "laravel", "matomo", "phpunit"]
# for ApplicationName in list_app:
ApplicationName = "laravel"

smells_data = pd.read_csv("C:/Project/statiqueProject/results/R1/test/Commits_Analysis_" + ApplicationName + ".csv",
                            index_col=0, parse_dates=True)
smells_data.plot(title="Évolution des codes puants du projet '" + ApplicationName + "'", xlabel = "#Commit" )

# smells_data = pd.read_csv("C:/Project/statiqueProject/results/R1/Analysis_projects.csv",
#                           index_col=0, parse_dates=True)
# smells_data.plot(title="Évolution des codes puants des projet ", xlabel = "#Commit")




# plt.boxplot(box_plot_data, 0, '', labels=['HMC', 'ECL','EML','EPL', 'HNPC', 'HC','ECB', 'EDOI', 'GS'])

# ("HMC", "ECL","EML","EPL","HNPC", "HC","ECB","EDOI", "GS")

plt.savefig("C:/Project/statiqueProject/Results/R1/test/"+ ApplicationName +"_test.png")

plt.show()