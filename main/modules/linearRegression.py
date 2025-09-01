import matplotlib.pyplot as plt
from io import StringIO
from scipy import stats

class LinearRegressionModel :
    x = []
    y = []
    
    slope = 0
    intercept = 0
    r = 0
    p = 0
    std_err = 0

    model = None

    def __init__(self, x=[], y=[]):
        self.x = x
        self.y = y
        if len(x) == 0:
            self.x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
        if len(y) == 0:
            self.y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
        
        self.slope, self.intercept, self.r, self.p, self.std_err = stats.linregress(self.x, self.y)
        self.model = list(map(self.genYValue, self.x))
    
    def genYValue(self, x):
        return self.slope * x + self.intercept
    
    def genGraph(self):
        fig = plt.figure()
        plt.scatter(self.x, self.y)
        plt.plot(self.x, self.model)
        
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data