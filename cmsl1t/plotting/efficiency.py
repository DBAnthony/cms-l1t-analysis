from __future__ import print_function
from cmsl1t.plotting.base import BasePlotter
from cmsl1t.hist.hist_collection import HistogramCollection
from cmsl1t.hist.factory import HistFactory
import cmsl1t.hist.binning as bn
from cmsl1t.utils.draw import draw, label_canvas
from cmsl1t.utils.fit_efficiency import fit_efficiency
from cmsl1t.io import to_root, from_root

from rootpy.plotting import Legend, HistStack, Efficiency
from rootpy.context import preserve_current_style
from rootpy import asrootpy, ROOT


class EfficiencyPlot(BasePlotter):
    def build(self,
              online_name, offline_name,
              online_title, offline_title,
              pileup_bins, thresholds, n_bins, low, high):
        """ This is not in an init function so that we can by-pass this in the
        case where we reload things from disk """
        self.online_name = online_name
        self.offline_name = offline_name
        self.online_title = online_title
        self.offline_title = offline_title
        self.pileup_bins = bn.Sorted(pileup_bins, "pileup",
                                     use_everything_bin=True)
        self.thresholds = bn.GreaterThan(thresholds, "threshold",
                                         use_everything_bin=True)

        name = [online_name, offline_name,
                "thresh_{threshold}", "pu_{pileup}"]
        name = "__".join(name)
        title = " ".join([online_name, " in PU bin: {pileup}",
                          "and passing threshold: {threshold}"])

        def make_efficiency(labels):
            this_name = "efficiency" + name.format(**labels)
            this_title = title.format(**labels)
            eff = asrootpy(ROOT.TEfficiency(this_name, this_title,
                                            n_bins, low, high))
            eff.drawstyle = "EP"
            return eff
        self.efficiencies = HistogramCollection([self.pileup_bins, self.thresholds],
                                                make_efficiency)
        self.filename_format = "{type}" + name

    def from_root(self, filename):
        """ Reload histograms from existing files on disk """
        print("BEK: self before ",self.__dict__)
        things = from_root(filename)
        print("BEK things:", things)
        print("BEK things[0].efficiencies:", things[0].efficiencies)
        print("BEK things[0].efficiencies.get_bin_contents([0,0]):", things[0].efficiencies.get_bin_contents([0,0]))
        return True
        new = things[0]
        yields = things[1]
        print("BEK: new before ",new.__dict__)
        if hasattr(self, "online_name"):
            if not self.__is_consistent(new):
                return False
            self.__append_yields(yields)
        else:
            final = new.__dict__
            final.update(self.__dict__)
            self.__dict__ = final
            print("BEK: loaded new objects")

            # Boiler plate to convert a given distribution to a turnon
            def clone_hist(labels):
                pileup_bin = labels["pileup"]
                threshold_bin = labels["threshold"]
                a_yield = yields.get_bin_contents([pileup_bin, threshold_bin])
                print("BEK", pileup_bin, threshold_bin, a_yield)
                if not a_yield:
                    return None
                return a_yield.Clone()

            # Actually make the turnons
            new_yields = HistogramCollection([self.pileup_bins, self.thresholds],
                                               clone_hist)
            self.yields = new_yields
        print("BEK: self after ",self.__dict__)
        return True

    def fill(self, pileup, online, offline):
        for bins, hist in self.efficiencies[pileup, online].items():
            threshold = self.thresholds.get_bin_center(bins[1])
            passed = False
            if isinstance(threshold, str) and threshold == bn.Base.overflow:
                passed = True
            elif online > threshold:
                passed = True
            self.efficiencies[pileup, online].fill(passed, offline)

    def draw(self, with_fits=True):
        # Fit the efficiencies if requested
        if with_fits:
            self.__fit_efficiencies()

        # Overlay the "all" pile-up bin for each threshold
        all_pileup_effs = self.efficiencies.get_bin_contents([bn.Base.everything])
        hists = []
        labels = []
        fits = []
        for threshold in all_pileup_effs.iter_all():
            if not isinstance(threshold, int):
                continue
            hists.append(all_pileup_effs.get_bin_contents(threshold))
            labels.append("> " + str(self.thresholds.bins[threshold]))
            if with_fits:
                fits.append(self.fits.get_bin_contents([bn.Base.everything, threshold]))
        self.__make_overlay("all", "all", hists, fits, labels, self.online_title)

        # Overlay individual pile-up bins for each threshold
        for threshold in self.thresholds:
            hists = []
            labels = []
            fits = []
            for pileup in self.pileup_bins:
                if not isinstance(pileup, int):
                    continue
                hists.append(self.efficiencies.get_bin_contents([pileup, threshold]))
                if with_fits:
                    fits.append(self.fits.get_bin_contents([pileup, threshold]))
                labels.append(str(self.pileup_bins.bins[pileup]))
            self.__make_overlay(pileup, threshold, hists, fits, labels, "PU bin")

        # Produce the fit summary plot
        if with_fits:
            self.__summarize_fits()

    def to_root(self, outfile):
        """ Write histograms to disk """
        to_root(self, outfile)

    def __fit_efficiencies(self):
        def make_fit(labels):
            pileup_bin = labels["pileup"]
            threshold_bin = labels["threshold"]
            efficiency = self.efficiencies.get_bin_contents([pileup_bin, threshold_bin])
            params = fit_efficiency(efficiency, self.thresholds.get_bin_center(threshold_bin))
            return params

        # Actually make the efficiencies
        self.fits = HistogramCollection([self.pileup_bins, self.thresholds],
                                        make_fit)

    def __make_overlay(self, pileup, threshold, hists, fits, labels, header):
        with preserve_current_style():
            # Draw each efficiency (with fit)
            canvas = draw(hists, draw_args={"xtitle": self.offline_title,
                                            "ytitle": "Efficiency"})
            if len(fits) > 0:
                for fit, hist in zip(fits, hists):
                    fit["asymmetric"].linecolor = hist.GetLineColor()
                    fit["asymmetric"].Draw("same")

            # Add labels
            label_canvas()

            # Add a legend
            legend = Legend(len(hists), header=header,
                            topmargin=0.35, entryheight=0.035)
            for hist, label in zip(hists, labels):
                legend.AddEntry(hist, label)
            legend.Draw()

            # Save canvas to file
            name = self.filename_format.format(type="efficiency_",
                                               pileup=pileup,
                                               threshold=threshold)
            self.save_canvas(canvas, name)

    def __summarize_fits(self):
        """ Implement this to show fit evolution plots """
        pass

    def __is_consistent(self, new):
        """ 
        Check the two plotters are the consistent, so same binning and same axis names
        """
        return (self.pileup_bins.bins == new.pileup_bins.bins) and \
               (self.thresholds.bins == new.pileup_bins.bins) and \
               (self.online_name == new.online_name) and \
               (self.offline_name == new.offline_name)
