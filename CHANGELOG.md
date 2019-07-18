# Change Log

## [v0.6.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.6.0)

[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.5.1...v0.6.0)

**Implemented enhancements:**

- Simplify the event loop by using a context manager [\#10](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/10)

**Closed issues:**

- Update setup to work under CentOS7 [\#164](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/164)
- Problem running jobs with HTCondor [\#162](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/162)
- HTCondor on lxplus [\#160](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/160)
- Printout number of objects passing thresholds when estimating rates [\#150](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/150)
- Speed up CI by using a smarter docker image [\#148](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/148)

**Merged pull requests:**

- Remove pileup selection in jetMetAnalyzer [\#172](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/172) ([bundocka](https://github.com/bundocka))
- Global filters for events [\#170](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/170) ([kreczko](https://github.com/kreczko))
- Roll back LCG version to workaround matplotlib efficiency bug [\#168](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/168) ([bundocka](https://github.com/bundocka))
- Trig plots [\#166](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/166) ([benkrikler](https://github.com/benkrikler))
- added setup.sh and added CentOS 7 support [\#165](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/165) ([kreczko](https://github.com/kreczko))
- Add the home variable for condor jobs which was causing issues [\#163](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/163) ([benkrikler](https://github.com/benkrikler))
- Workaround for HTCondor on lxplus [\#161](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/161) ([kreczko](https://github.com/kreczko))
- Fixing current travis build issues [\#158](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/158) ([kreczko](https://github.com/kreczko))
- Sort reco jets by etCorr, check jet bx == 0, fix batch sub [\#156](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/156) ([bundocka](https://github.com/bundocka))
- Printout number of objects passing thresholds when estimating rates [\#153](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/153) ([kreczko](https://github.com/kreczko))
- \[WIP\] Python 3 compatibility [\#152](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/152) ([kreczko](https://github.com/kreczko))
- Speeding up CI [\#149](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/149) ([kreczko](https://github.com/kreczko))

## [v0.5.1](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.5.1) (2018-08-03)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.5.0...v0.5.1)

**Implemented enhancements:**

- Config scope reduction for analysers [\#47](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/47)

**Closed issues:**

- Extend CI to include running analyzers over a small test sample [\#146](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/146)
- Master branch HW vs Emu jet rates analyser crashes [\#115](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/115)

**Merged pull requests:**

- Integration testing for data worfllow & fixes for \#144 [\#147](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/147) ([kreczko](https://github.com/kreczko))
- Config scope reduction for analyzers and producers [\#144](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/144) ([kreczko](https://github.com/kreczko))

## [v0.5.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.5.0) (2018-07-25)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.4.4...v0.5.0)

**Implemented enhancements:**

- Moving analysers to the new eventReader & producers [\#140](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/140) ([kreczko](https://github.com/kreczko))

## [v0.4.4](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.4.4) (2018-07-25)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.4.3...v0.4.4)

**Merged pull requests:**

- Improving "make release" scripts [\#143](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/143) ([kreczko](https://github.com/kreczko))
- Dynamic binning for efficiencies [\#141](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/141) ([bundocka](https://github.com/bundocka))

## [v0.4.3](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.4.3) (2018-05-15)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.4.2...v0.4.3)

**Fixed bugs:**

- Bug: travis is returning false positives! [\#137](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/137)

**Merged pull requests:**

- Fixing travis false positives [\#138](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/138) ([kreczko](https://github.com/kreczko))
- Add hardware vs emu rate comparisons [\#136](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/136) ([bundocka](https://github.com/bundocka))

## [v0.4.2](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.4.2) (2018-05-15)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.4.1...v0.4.2)

**Closed issues:**

- Producers need better configuration language [\#134](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/134)
- Error reporting when importing a broken analyzer is lousy. [\#88](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/88)

**Merged pull requests:**

- More plot formatting [\#142](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/142) ([bundocka](https://github.com/bundocka))
- BaseProducer, input & output checks [\#135](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/135) ([kreczko](https://github.com/kreczko))
- Added error reporting to utils.module.exists \(issue \#88\) [\#133](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/133) ([kreczko](https://github.com/kreczko))

## [v0.4.1](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.4.1) (2018-05-14)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.4.0...v0.4.1)

**Merged pull requests:**

- Implement offline cuts for resolution plots [\#132](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/132) ([bundocka](https://github.com/bundocka))

## [v0.4.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.4.0) (2018-05-07)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.3.0...v0.4.0)

**Implemented enhancements:**

- Generalisation of analyzers/producers [\#53](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/53)
- Tighter integration of config and processing [\#40](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/40)
- Enabling new event reader in cmsl1t\_future [\#129](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/129) ([kreczko](https://github.com/kreczko))

**Closed issues:**

- Provide option to produce emulator plots  [\#102](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/102)
- Offline MET Analyser tries to access Phi attribute of HTT \(no such thing\) [\#95](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/95)
- New EventReader [\#80](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/80)
- Configuration files for mapping L1TNtuple content [\#79](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/79)

**Merged pull requests:**

- Separate central and forward jets for fixed rate comparisons [\#131](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/131) ([bundocka](https://github.com/bundocka))
- Tidying up configuration files and removing obsolete analysers [\#130](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/130) ([kreczko](https://github.com/kreczko))

## [v0.3.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.3.0) (2018-05-02)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.2.0...v0.3.0)

**Fixed bugs:**

- Root files no longer exist [\#64](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/64)

**Closed issues:**

- Validation of old vs new [\#6](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/6)

**Merged pull requests:**

- Replacing `do\_X` with `load\_trees` in configs, analysers and eventReader [\#128](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/128) ([kreczko](https://github.com/kreczko))
- Remaining new files from PR \#85 [\#127](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/127) ([kreczko](https://github.com/kreczko))
- Speeding up docker build for travis [\#126](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/126) ([kreczko](https://github.com/kreczko))
- Bug fix to efficiencies [\#125](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/125) ([bundocka](https://github.com/bundocka))
- Few bug fixes, corrections, remove deprecated cfgs/analyzers [\#124](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/124) ([bundocka](https://github.com/bundocka))
- Add config yamls for 4 main modes [\#123](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/123) ([bundocka](https://github.com/bundocka))
- Add ability to run performance studies using generator quantities from MC [\#122](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/122) ([bundocka](https://github.com/bundocka))
- Add rate vs pileup plotting [\#121](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/121) ([bundocka](https://github.com/bundocka))
- Fix calo jets efficiencies and logic for emulator thresholds [\#120](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/120) ([bundocka](https://github.com/bundocka))
- Fix lumi filter in jetMet\_analyzer [\#119](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/119) ([bundocka](https://github.com/bundocka))
- Convert output of cum sum back to array to build cum hist [\#118](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/118) ([bundocka](https://github.com/bundocka))
- Remove @cached and corresponding import [\#117](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/117) ([bundocka](https://github.com/bundocka))
- Add rebase command to README [\#116](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/116) ([bundocka](https://github.com/bundocka))
- \[IO\] Moving code from create-map-file to cmsl1t.io.mapfile for easier testing [\#113](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/113) ([kreczko](https://github.com/kreczko))
- Replacing nose with pytest [\#112](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/112) ([kreczko](https://github.com/kreczko))

## [v0.2.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.2.0) (2018-03-27)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.1.2...v0.2.0)

**Implemented enhancements:**

- YAML NTuple config file for documentation and aliasing [\#82](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/82) ([kreczko](https://github.com/kreczko))

**Closed issues:**

- Add JSON filter for \(run, lumi\) [\#105](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/105)
- Failed job resubmission & log files for investigating job failure on batch [\#99](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/99)
- JetET & \*\_Emu\_phi\_res plotters not being created in Offline MET analyser [\#97](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/97)

**Merged pull requests:**

- Adding luminosity filter [\#111](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/111) ([kreczko](https://github.com/kreczko))
- Plotting updates from \#106 [\#110](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/110) ([kreczko](https://github.com/kreczko))
- Config, Event and hist related parts of \#106 [\#108](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/108) ([kreczko](https://github.com/kreczko))
- Breaking down \#106 [\#107](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/107) ([kreczko](https://github.com/kreczko))
- A "cleaner" batch submission [\#104](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/104) ([kreczko](https://github.com/kreczko))
- After the long slumber, cmsl1t wakes up [\#103](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/103) ([kreczko](https://github.com/kreczko))
- Added JetET plotters to offline MET analyser, no longer crashes [\#98](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/98) ([professor-calculus](https://github.com/professor-calculus))
- Fixing the readthedocs errors [\#94](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/94) ([kreczko](https://github.com/kreczko))
- Breakdown of PR 89 - part 4 [\#93](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/93) ([kreczko](https://github.com/kreczko))
- Breakdown of PR 89 - part 3 [\#92](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/92) ([kreczko](https://github.com/kreczko))
- Breakdown of PR 89 - part 2 [\#91](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/91) ([kreczko](https://github.com/kreczko))
- Breakdown of PR 89 - part 1 [\#90](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/90) ([kreczko](https://github.com/kreczko))
- Minor fixes for Makefile and bin/\* [\#87](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/87) ([kreczko](https://github.com/kreczko))
- Github templates for issues and pull requests [\#86](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/86) ([kreczko](https://github.com/kreczko))

## [v0.1.2](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.1.2) (2017-09-18)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.1.1...v0.1.2)

**Implemented enhancements:**

- Batch submission [\#58](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/58)
- Merging weekly checks into master [\#81](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/81) ([kreczko](https://github.com/kreczko))
- Allow multiple wildcards with root\_glob [\#68](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/68) ([benkrikler](https://github.com/benkrikler))

**Closed issues:**

- cmsl1t\_dirty\_batch command broken for click-log 0.2.0 [\#71](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/71)
- Weekly monitoring confiuration [\#66](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/66)

**Merged pull requests:**

- Clarifications on how to use changelog generator [\#78](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/78) ([kreczko](https://github.com/kreczko))
- "Final" PR to add all changes for weekly checks [\#77](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/77) ([benkrikler](https://github.com/benkrikler))
- Add two more plotters for resolution [\#76](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/76) ([benkrikler](https://github.com/benkrikler))
- Efficiency plots: Fill all pile-up bins [\#75](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/75) ([benkrikler](https://github.com/benkrikler))
- Fix reporting of errors when merging histograms together  [\#74](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/74) ([benkrikler](https://github.com/benkrikler))
- Fix another issue with the efficiency curves [\#73](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/73) ([benkrikler](https://github.com/benkrikler))
- Fix issue 71 and other aspects of the bin/cmsl1t\* commands [\#72](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/72) ([benkrikler](https://github.com/benkrikler))
- Add a generic 2D online vs offline quantity plotter [\#70](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/70) ([benkrikler](https://github.com/benkrikler))
- Add users' site packages directory to PYTHONPATH [\#69](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/69) ([benkrikler](https://github.com/benkrikler))
- Fix the Efficiency plotter which was giving non-physical looking turnons [\#67](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/67) ([benkrikler](https://github.com/benkrikler))
- First version of weekly checks config [\#65](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/65) ([kreczko](https://github.com/kreczko))

## [v0.1.1](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.1.1) (2017-09-04)
[Full Changelog](https://github.com/cms-l1t-offline/cms-l1t-analysis/compare/v0.1.0...v0.1.1)

**Implemented enhancements:**

- Support to run legacy analysers in the new framework [\#48](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/48) ([kreczko](https://github.com/kreczko))
- skeleton for documentation [\#33](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/33) ([kreczko](https://github.com/kreczko))
- Fixing issue 23 [\#27](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/27) ([kreczko](https://github.com/kreczko))
- Fixing issue \#22 [\#26](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/26) ([kreczko](https://github.com/kreczko))

**Closed issues:**

- Configuration tutorial [\#50](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/50)
- cmsl1t can only be executed in cms-l1t-analysis project directory [\#41](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/41)
- Config validation [\#29](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/29)
- demo\_analyzer can not be run [\#24](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/24)
- Setting up the environment twice fails [\#23](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/23)
- Can not run benchmark [\#22](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/22)
- rootpy's TreeChain doesn't work with globbing and xrootd access [\#16](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/16)
- Suggestion for plotting and histogram collections [\#14](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/14)
- Introduce 'modifiers' [\#9](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/9)
- Migrate remaining macros [\#8](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/8)
- Replacement of ntuple\_config [\#5](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/5)
- Improvements to base histogram collection [\#4](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/4)
- Plotting in cmsl1t [\#3](https://github.com/cms-l1t-offline/cms-l1t-analysis/issues/3)

**Merged pull requests:**

- Get bsub batch submission working [\#63](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/63) ([benkrikler](https://github.com/benkrikler))
- Docker for HTCondor testing [\#62](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/62) ([kreczko](https://github.com/kreczko))
- WIP: Add a dirty batch submission script, for issue \#58 [\#60](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/60) ([benkrikler](https://github.com/benkrikler))
- Add the ability to reload histograms from files [\#59](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/59) ([benkrikler](https://github.com/benkrikler))
- Make proper use of TEfficiency [\#57](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/57) ([benkrikler](https://github.com/benkrikler))
- Resolve the warnings seen when more than 10 files are loaded [\#56](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/56) ([benkrikler](https://github.com/benkrikler))
- Make {emuC,c}aloTowers pluralised consistently [\#55](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/55) ([benkrikler](https://github.com/benkrikler))
- Improve Base classes for Analyzers and Plotters [\#52](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/52) ([benkrikler](https://github.com/benkrikler))
- Moving configuration description into config tutorial [\#51](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/51) ([kreczko](https://github.com/kreczko))
- Implement fitting of turnon curves [\#49](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/49) ([benkrikler](https://github.com/benkrikler))
- Fixing issue 41: execute cmsl1t from anywhere [\#46](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/46) ([kreczko](https://github.com/kreczko))
- Add jet matching algorithm [\#45](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/45) ([kreczko](https://github.com/kreczko))
- Handle L1NTuples without certain trees [\#43](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/43) ([benkrikler](https://github.com/benkrikler))
- Say something when validation fails due to missing section [\#42](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/42) ([benkrikler](https://github.com/benkrikler))
- Add final polish to efficiency plotter and related code [\#38](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/38) ([benkrikler](https://github.com/benkrikler))
- WIP: implement first real plotter [\#37](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/37) ([benkrikler](https://github.com/benkrikler))
- Config validation [\#36](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/36) ([kreczko](https://github.com/kreczko))
- Fixes for documentation on readthedocs. [\#35](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/35) ([kreczko](https://github.com/kreczko))
- Improve interface to allow working with multiple hists for one key [\#34](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/34) ([benkrikler](https://github.com/benkrikler))
- General histogram collection [\#32](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/32) ([benkrikler](https://github.com/benkrikler))
- Migrating legacy analyzers [\#30](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/30) ([kreczko](https://github.com/kreczko))
- Config draft [\#28](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/28) ([kreczko](https://github.com/kreczko))
- Split timerfunc decorator for different call-signatures [\#25](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/25) ([benkrikler](https://github.com/benkrikler))
- Fixes for decorator and flake8 [\#21](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/21) ([kreczko](https://github.com/kreczko))
- Update README.md [\#20](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/20) ([benkrikler](https://github.com/benkrikler))
- Add an initial draft of the sort of 'analyzer' I would suggest we use [\#19](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/19) ([benkrikler](https://github.com/benkrikler))
- Add first working version of a root\_glob object [\#18](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/18) ([benkrikler](https://github.com/benkrikler))
- Add the tower widths in eta to geometry. [\#17](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/17) ([benkrikler](https://github.com/benkrikler))
- Move timerfunc from run\_benchmark into a util file [\#15](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/15) ([benkrikler](https://github.com/benkrikler))
- Ignore vim and emacs backup files [\#13](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/13) ([benkrikler](https://github.com/benkrikler))
- Changes to makefile [\#12](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/12) ([benkrikler](https://github.com/benkrikler))
- Changes to Makefile to pull data files as proper makefile targets [\#11](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/11) ([benkrikler](https://github.com/benkrikler))
- Documentation [\#7](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/7) ([kreczko](https://github.com/kreczko))

## [v0.1.0](https://github.com/cms-l1t-offline/cms-l1t-analysis/tree/v0.1.0) (2017-03-24)
**Merged pull requests:**

- Adding continuous integration [\#2](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/2) ([kreczko](https://github.com/kreczko))
- First draft [\#1](https://github.com/cms-l1t-offline/cms-l1t-analysis/pull/1) ([kreczko](https://github.com/kreczko))


## details of first-draft
 - Include Shane's macros as 'legacy' for comparison
 - Read L1TNtuples in python
 - Transfer 1 Macro to python (makeJetResolutions)
 - Benchmark legacy vs new
 - Add histogram collections for easier creation & handling
   - Added multidimensional dictionary based on defaultdict
  custom dicts or objects in certain dimensions
   - Added HistogramByPileUpCollection
     - Automatic selection of PU bin based on pileup value. E.g. `histograms[11]` will fill the 2nd bin if `pileupBins=[0,10,20,30,999]`
   - Added ResolutionCollection
     - Specialisation of HistogramByPileUpCollection
     - Automatic selection of detector region based on `cmsl1t.geometry`
 - Implement Ben's MET turnons to check if the package is going the right way
 - Explore ways to recalculate MET
 - Implement EfficiencyCollection
 - First PR to main repo
 - Request feedback from other analysers
   - See what is easy, what is not

\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*