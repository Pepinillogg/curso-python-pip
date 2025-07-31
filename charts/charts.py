import matplotlib.pyplot as pylot
def generate_pie_chart():
    labels = ["a","b","c"]
    values = [200,423213,1323]

    fig,ax = pylot.subplots()
    ax.pie(values,labels = labels)
    pylot.savefig("pie.png")
    pylot.close()

