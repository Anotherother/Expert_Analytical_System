import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

from scipy.optimize import brentq
from scipy.interpolate import interp1d

def plotROC(true, predicted, ttl = None):
    fpr, tpr, threshold = roc_curve(true, predicted, pos_label = 1)
    roc_auc = auc(fpr, tpr)


    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(ttl)
    plt.legend(loc="lower right")
    plt.show()


def EER_THR(y_test, scores):
    fpr, tpr, threshold = roc_curve(y_test, scores, pos_label=1)
    eer = brentq(lambda x: 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
    thresh = interp1d(fpr, threshold)(eer)

    return eer, thresh
