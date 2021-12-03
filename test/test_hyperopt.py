from optimize_ROI import TemplateClassifier
import numpy as np
TC = TemplateClassifier()
TC.fit(np.zeros((100,1)), np.zeros(100))
TC.score(np.zeros((100, 1)), np.zeros(100))
