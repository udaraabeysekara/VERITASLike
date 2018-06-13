
from threeML import *
#from threeML.plugins.experimental.VERITASLike import VERITASLike
from VERITASLike import VERITASLike

import matplotlib.pyplot as plt

veritas = VERITASLike('veritas','threemlVEGAS20hrATM21Sys20Substract.root')

data = DataList(veritas)
source1_sp = Log_parabola()
source1 = PointSource("source1", ra=83.6292, dec=22.0144, spectral_shape=source1_sp)
model = Model(source1)
model.source1.spectrum.main.Log_parabola.alpha.bounds = (-3.8, -2.1)
model.source1.spectrum.main.Log_parabola.alpha.value = -2.967
#model.source1.spectrum.main.Log_parabola.alpha.fix = True
model.source1.spectrum.main.Log_parabola.piv.value = 7E9
model.source1.spectrum.main.Log_parabola.K.value = 1.76E-22#3.12E-16
model.source1.spectrum.main.Log_parabola.K.bounds = (2.0E-23,5.0E-22)
model.source1.spectrum.main.Log_parabola.beta.value = 0.15
model.source1.spectrum.main.Log_parabola.beta.fix = False
#model.source1.spectrum.main.Log_parabola.beta.bounds = (0.0, 0.25)
model.display()

jl = JointLikelihood(model, data)
jl.set_minimizer("ROOT")
best_fit_parameters, likelihood_values = jl.fit()
jl.results.display()

#res = jl.get_contours(source1_sp.index, -2.65, -2.25, 60,source1_sp.K, 3.1E-20, 4.2E-20, 60)
#plt.plot([3.632E-20,3.632E-20], [-2.38921,-2.48079], 'k-')
#plt.plot([3.4405E-20,3.8059E-20], [-2.435,-2.435], 'k-')

plt.show()
