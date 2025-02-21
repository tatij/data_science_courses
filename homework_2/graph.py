import seaborn as sns
import matplotlib.pyplot as plt

def hist(dataset, column):
    sns.histplot(dataset[column], bins=5, kde=False, color='green', alpha=0.6)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.title("Гистограмма")
    plt.xlabel(column)
    plt.ylabel("Частота повторений")
    plt.show()

def line(dataset):
    sns.lineplot(dataset, x = dataset["Screen Size (inch)"], y = dataset["Price ($)"])
    plt.title("Линейный график")
    plt.xlabel("Ширина экрана")
    plt.ylabel("Цена")
    plt.show()   
    
def scatter(dataset):
    sns.scatterplot(dataset, x = dataset["Operating System"], y = dataset["Price ($)"])
    plt.title("Диаграмма рассеяния")
    plt.xlabel("Операционная система")
    plt.ylabel("Цена")
    plt.show()  