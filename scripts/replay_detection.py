import numpy as np
import scipy

from scipy.stats import moment
from collections import Counter
import scipy.io.wavfile as wav
#import pywt

class ReplayDetection():

    """
    Class with main function for signal processing
    """

    def __init__(self, inputFile):

        self.rate, self.audio = wav.read(inputFile)

        #############
        # if we want work with wavelet - use this code:
        # self.audio = pywt.downcoef('d', self.audio, 'db8', mode='symmetric', level = 8)
        #############

        self.histogram = list(Counter(self.audio).values())


    #def signalToNoise(self):
    #    """
    #    Signal to Noise Ratio.
    #    """
    #    singleChannel = self.audio
    #    try:
    #        singleChannel = numpy.sum(self.audio, axis=1)
    #    except:
    #        pass
    #    norm = singleChannel / float(max(np.amax(singleChannel), -1 * np.amin(singleChannel)))
    #    return stats.signaltonoise(norm)

    def sigmaAudio(self):
        """
        Standart devianios (sqrt(variance)). Euclidian metrics
        """
        return np.sqrt(sum((self.histogram - np.mean(self.histogram))**2) / len(self.histogram))

    def excess(self):
        """
        Measure the sharpness of the peak of the distribution of a random variable
        """
        # alternalive formulas
        # mu = moment(audio, 4)
        mu = np.sum((self.histogram-np.mean(self.histogram))**4) / len(self.histogram)
        return mu /(ReplayDetection.sigmaAudio(self)**4) - 3

    def rangeSignal(self):
        """
        Difference between maximum and minimun values of Signal
        """
        return np.max(self.histogram) - np.min(self.histogram)

    def rangeSignalMean(self):
        """
        Range from the mean
        """
        return (np.max(self.histogram) - np.min(self.histogram)) / np.mean(self.histogram)

    def variance (self):
        """
        Variance of signal
        """
        # alternative formulas
        # var = (audio - np.mean(audio))/ audio.shape[0]
        return np.var(self.audio)

    def asimetryCoefficient (self):
        """
        Skewness - nonsymmetry destribution of random variable
        """
        return moment(self.histogram,3) / ReplayDetection.sigmaAudio(self) ** 3

    def variation(self):
        """
        Measure of relative variation
        """
        return ReplayDetection.sigmaAudio(self) / np.mean(self.histogram)
