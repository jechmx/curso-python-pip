import utils
import read_csv
import charts

def run():
  data=read_csv.read_csv('data.csv')
  country=input('Type Country=>')
  results=utils.population_by_country(data,country)
  if len(results)>0:
    country=results[0]
    labels,values=utils.get_population(country)
    charts.gnerate_bar_chart(country['Country/Territory'],labels,values)
    charts.generate_pie_chart(country['Country/Territory'],labels,values)

if __name__=='__main__':
  run()
