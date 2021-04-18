![license MIT](https://img.shields.io/github/license/kamal0013/PowNet) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4040851.svg)](https://doi.org/10.5281/zenodo.4040851)
# PowNet-Thailand: Network-constrained Unit Commitment / Economic Dispatch model for the Thai power system with sample data
PowNet-Thailand is an implementation of [PowNet](https://github.com/kamal0013/PowNet) model on the Thai power system. The model is developed based on the load (domestic and exports) and infrastructure (power plants, substations, and high-voltage transmission lines) of the Thai power system operated in 2016, including a number of Laotian hydro and thermal power plants that supply to Thailand. The power systems’ data are mostly collected from publicly available reports, published by Electricity Generating Authority of Thailand (EGAT), Energy Policy and Planning Office (EPPO) – Thai Ministry of Energy, Electricite Du Laos (EDL), and the Department of Energy Policy and Planning (DEPP) – Laotian Ministry of Energy and Mine. The hydropower budgets are simulated with [VIC-Res](https://github.com/thanhiwer/VICRes). Please refer to [Chowdhury et al. (2020a)](https://www.essoar.org/doi/abs/10.1002/essoar.10504393.1) for additional details on the power system and model setup.

For 2016, the repository contains input data, output data, and a Python script for a sample analysis. In addition, climate-dependent input data (e.g., hydropower budget) for a 30-year (1976-2005) simulation period, used in [Chowdhury et al. (2020a)](https://www.essoar.org/doi/abs/10.1002/essoar.10504393.1), are also provided. Outputs for any of these years can be obtained by running PowNet-Thailand through the following two steps: (1) change simulation year in ‘pownet_thai_datasetup.py’, and (2) run ‘pownet_thai_solver.py’.

The basic functionalities and input-output structure of PowNet are described in [Chowdhury et al. (2020b)](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.302/). Step-by-step instructions on how to run and customize PowNet for any power system are provided in this [GitHub repository](https://github.com/kamal0013/PowNet).

# Citation
If you use PowNet-Thailand and/or the data for your research, please cite the following papers:

Chowdhury, A.K., Dang, T.D., Nguyen, H.T., Koh, R., and Galelli, S., (2021). The Greater Mekong's climate-water-energy nexus: how ENSO-triggered regional droughts affect power supply and CO2 emissions. Earth’s Future, 9, e2020EF001814, DOI: https://doi.org/10.1029/2020EF001814.

Chowdhury, A.K., Kern, J., Dang, T.D. and Galelli, S., (2020b). PowNet: A Network-Constrained Unit Commitment/Economic Dispatch Model for Large-Scale Power Systems Analysis. Journal of Open Research Software, 8(1), p.5. DOI: http://doi.org/10.5334/jors.302.

In addition, each release of PowNet-Thailand is achieved on Zenodo with a DOI, that can be found [here](https://zenodo.org/record/4040851#.X2iFQWhKguU).

# Contact
For questions and feedback related to PowNet-Thailand, please send an email to afm.chowdhury@uon.edu.au (AFM Kamal Chowdhury) or stefano_galelli@sutd.edu.sg (Stefano Galelli).

# License
PowNet-Thailand and the data are released under the MIT license.

# Acknowledgment	
PowNet-Thailand development is supported by Singapore's Ministry of Education (MoE) through the Tier 2 project “Linking water availability to hydropower supply – an engineering systems approach” (Award No. MOE2017-T2-1-143).
