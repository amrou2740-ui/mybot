import matplotlib.pyplot as plt
import os

class DataVizAgent:
    def make(self, topic, output_dir):
        path = os.path.join(output_dir, "chart.png")
        plt.plot([1,2,3,4],[10,20,25,30])
        plt.title(topic)
        plt.savefig(path)
        plt.close()
        return [path]
