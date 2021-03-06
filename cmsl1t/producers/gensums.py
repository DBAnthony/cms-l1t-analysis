from __future__ import division
import numpy as np
import math
from cmsl1t.energySums import EnergySum, Met
from .base import BaseProducer


class Producer(BaseProducer):

    def __init__(self, inputs, outputs, **kwargs):
        self._expected_input_order = ['jetPt', 'jetEta', 'partId', 'partPhi', 'partPt', 'partEta', ]
        super(Producer, self).__init__(inputs, outputs, **kwargs)

    def produce(self, event):

        calculateMET = True if 'Generator_genMetTrue' not in self._inputs else False
        variables = [event[i] for i in self._inputs]
        prefix = self._outputs[0] + '_'

        if calculateMET:
            jet_pt, jet_eta, part_id, partPhi, partPt, partEta = variables
        else:
            jet_pt, jet_eta, part_id, partPhi, partPt, partEta, genMetTrue = variables
        ht = 0
        for pt, eta in zip(jet_pt, jet_eta):
            if abs(eta) < 2.4:
                ht += pt
        # setattr(event, prefix + 'HT', EnergySum(np.sum(jet_pt)))
        setattr(event, prefix + 'HT', EnergySum(ht))

        if calculateMET:
            part_id = np.absolute(part_id)
            partEta = np.absolute(partEta)
            partPhi = np.array(partPhi)
            partPt = np.array(partPt)

            # nu_e, mu, nu_mu, nu_tau
            particleMask = (part_id == 12) | (part_id == 13) | (part_id == 14) | (part_id == 16)
            eta_mask = partEta < 3.0

            genMetHF = self._calculate_met(partPt, partPhi, particleMask)
            genMetBE = self._calculate_met(partPt, partPhi, particleMask & eta_mask)

            setattr(event, prefix + 'MetHF', genMetHF)
            setattr(event, prefix + 'MetBE', genMetBE)

        else:
            setattr(event, prefix + 'MetBE', Met(genMetTrue, 0))
            setattr(event, prefix + 'MetHF', Met(genMetTrue, 0))

        return True

    def _calculate_met(self, partPt, partPhi, mask):
        met_x = np.dot(partPt[mask], np.cos(partPhi[mask]))
        met_y = np.dot(partPt[mask], np.sin(partPhi[mask]))
        met = np.sqrt(met_x ** 2 + met_y**2)
        met_phi = math.atan(met_y / met_x)
        return Met(met, met_phi)
