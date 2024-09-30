##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Mon Sep 30 16:53:21 2024

##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path 1l2y.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0, npot=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing lpbe...
PBEparm_parseToken:  trying lpbe...
NOsh: parsed lpbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (97, 65, 65)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Parsing PRINT section
NOsh: Done parsing PRINT section
NOsh: Done parsing PRINT section
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 304 atoms
Valist_getStatistics:  Max atom coordinate:  (10.248, 11.868, 6.918)
Valist_getStatistics:  Min atom coordinate:  (-12.769, -8.207, -6.946)
Valist_getStatistics:  Molecule center:  (-1.2605, 1.8305, -0.014)
NOsh_setupCalcMGAUTO(./apbs/src/generic/nosh.c, 1855):  coarse grid center = -1.2605 1.8305 -0.014
NOsh_setupCalcMGAUTO(./apbs/src/generic/nosh.c, 1860):  fine grid center = -1.2605 1.8305 -0.014
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1872):  Coarse grid spacing = 0.447401, 0.606927, 0.43512
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1874):  Fine grid spacing = 0.447401, 0.606927, 0.43512
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1876):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 1, 1, 1 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1970):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1972):  coarse mesh center = -1.2605 1.8305 -0.014
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1977):  coarse mesh upper corner = 20.2147 21.2522 13.9099
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1982):  coarse mesh lower corner = -22.7357 -17.5911 -13.9378
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1987):  initial fine mesh upper corner = 20.2147 21.2522 13.9099
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 1992):  initial fine mesh lower corner = -22.7357 -17.5911 -13.9378
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 2053):  final fine mesh upper corner = 20.2147 21.2522 13.9099
NOsh_setupCalcMGAUTO (./apbs/src/generic/nosh.c, 2058):  final fine mesh lower corner = -22.7357 -17.5911 -13.9378
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 14.7879
Vpbe_ctor2:  solute dimensions = 25.265 x 22.849 x 16.381
Vpbe_ctor2:  solute charge = 1
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 7042.98
Vpbe_ctor2:  Constructing Vclist with 50 x 45 x 32 table
Vclist_ctor2:  Using 50 x 45 x 32 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 1.9 max radius
Vclist_setupGrid:  Grid lengths = (33.8317, 30.8897, 24.6787)
Vclist_setupGrid:  Grid lower corner = (-18.1764, -13.6144, -12.3534)
Vclist_assignAtoms:  Have 471257 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 182.223
Vacc_storeParms:  Using 1844-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.215473
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 5.502790e-01
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (097, 065, 065)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 7.221000e-03
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (049, 033, 033)
Vbuildops: Galer: (025, 017, 017)
Vbuildops: Galer: (013, 009, 009)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 1.255640e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.893000e-01
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.400198e-01
Vprtstp: contraction number = 1.400198e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 2.403690e-02
Vprtstp: contraction number = 1.716679e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 5.053106e-03
Vprtstp: contraction number = 2.102228e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 1.166795e-03
Vprtstp: contraction number = 2.309065e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 2.810055e-04
Vprtstp: contraction number = 2.408353e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 6.938561e-05
Vprtstp: contraction number = 2.469191e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 1.744738e-05
Vprtstp: contraction number = 2.514554e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 4.452944e-06
Vprtstp: contraction number = 2.552213e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 1.152597e-06
Vprtstp: contraction number = 2.588394e-01
Vprtstp: iteration = 10
Vprtstp: relative residual = 3.026920e-07
Vprtstp: contraction number = 2.626174e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 1.437110e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.573500e+00
Vpmg_setPart:  lower corner = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  upper corner = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  actual minima = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  actual maxima = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vpmg_energy:  calculating only q-phi energy
Vpmg_qfEnergyVolume:  Calculating energy
Vpmg_energy:  qfEnergy = 1.394940138970E+04 kT
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.651000e-03
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 2.000000e-06
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 14.7879
Vpbe_ctor2:  solute dimensions = 25.265 x 22.849 x 16.381
Vpbe_ctor2:  solute charge = 1
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 7042.98
Vpbe_ctor2:  Constructing Vclist with 50 x 45 x 32 table
Vclist_ctor2:  Using 50 x 45 x 32 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 1.9 max radius
Vclist_setupGrid:  Grid lengths = (33.8317, 30.8897, 24.6787)
Vclist_setupGrid:  Grid lower corner = (-18.1764, -13.6144, -12.3534)
Vclist_assignAtoms:  Have 471257 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 182.223
Vacc_storeParms:  Using 1844-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -22.7357, -17.5911, -13.9378
VPMG::focusFillBound -- New mesh maxs = 20.2147, 21.2522, 13.9099
VPMG::focusFillBound -- Old mesh mins = -22.7357, -17.5911, -13.9378
VPMG::focusFillBound -- Old mesh maxs = 20.2147, 21.2522, 13.9099
VPMG::extEnergy:  energy flag = 1
Vpmg_setPart:  lower corner = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  upper corner = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  actual minima = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  actual maxima = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
VPMG::extEnergy:   Finding extEnergy dimensions...
VPMG::extEnergy    Disj part lower corner = (-22.7357, -17.5911, -13.9378)
VPMG::extEnergy    Disj part upper corner = (20.2147, 21.2522, 13.9099)
VPMG::extEnergy    Old lower corner = (-22.7357, -17.5911, -13.9378)
VPMG::extEnergy    Old upper corner = (20.2147, 21.2522, 13.9099)
Vpmg_qmEnergy:  Zero energy for zero ionic strength!
VPMG::extEnergy: extQmEnergy = 0 kT
Vpmg_qfEnergyVolume:  Calculating energy
VPMG::extEnergy: extQfEnergy = 0 kT
VPMG::extEnergy: extDiEnergy = 0 kT
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.220024
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 7.137850e-01
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (097, 065, 065)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 6.231000e-03
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (049, 033, 033)
Vbuildops: Galer: (025, 017, 017)
Vbuildops: Galer: (013, 009, 009)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 1.182560e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.993708e+00
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.400198e-01
Vprtstp: contraction number = 1.400198e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 2.403690e-02
Vprtstp: contraction number = 1.716679e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 5.053106e-03
Vprtstp: contraction number = 2.102228e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 1.166795e-03
Vprtstp: contraction number = 2.309065e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 2.810055e-04
Vprtstp: contraction number = 2.408353e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 6.938561e-05
Vprtstp: contraction number = 2.469191e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 1.744738e-05
Vprtstp: contraction number = 2.514554e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 4.452944e-06
Vprtstp: contraction number = 2.552213e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 1.152597e-06
Vprtstp: contraction number = 2.588394e-01
Vprtstp: iteration = 10
Vprtstp: relative residual = 3.026920e-07
Vprtstp: contraction number = 2.626174e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 1.460134e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.588189e+00
Vpmg_setPart:  lower corner = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  upper corner = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  actual minima = (-22.7357, -17.5911, -13.9378)
Vpmg_setPart:  actual maxima = (20.2147, 21.2522, 13.9099)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vpmg_energy:  calculating only q-phi energy
Vpmg_qfEnergyVolume:  Calculating energy
Vpmg_energy:  qfEnergy = 1.394940138970E+04 kT
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.421000e-03
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 3.000000e-06
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
printEnergy:  Performing global reduction (sum)
Vcom_reduce:  Not compiled with MPI, doing simple copy.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 4.715434e+00
