### NeuroML2/LEMS version of model 

The model defined in the Python Brian scripts has been converted to a LEMS ComponentType defintion: [IzhikevichFerguson.xml](https://github.com/OpenSourceBrain/FergusonEtAl2014-CA1PyrCell/blob/master/NeuroML2/IzhikevichFerguson.xml).

Note this is different from the existing [Izhikevich model definition in NeuroML2](https://neuroml.org/NeuroML2CoreTypes/Cells.html#izhikevichCell), as outlined in [Ferguson et al. 2014](http://f1000research.com/articles/3-104/v1):

> The model has a fast variable representing the membrane potential, V (mV), 
and a slow “recovery” current given by the variable u (pA).
In order to capture the spike width at threshold, we slightly modified the 
Izhikevich model by using a different “k” parameter above
and below the spike threshold (khigh and klow respectively).

