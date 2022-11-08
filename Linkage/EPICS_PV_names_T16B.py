"""
This is dict data of the EPICS PV names in Eline20U soft
"""

#should revised FULL_Channels whenever add new PV names

# PV names for Energy SE=Soft_Energy
SoftEnergy = {
    # set energy
    'PV_SET': "X20U:OP:PGM1:Soft_Energy.VAL",
    # energy read back
    'PV_RBV': "X20U:OP:PGM1:Soft_Energy.RBV",
    # retries
    'PV_MV_RTRY': "X20U:OP:PGM1:Soft_Energy.RTRY"}

# PV names for Mirror motion control
PGM1_Mirror = {
    'PV_SET': "X20U:OP:PGM1:MR.VAL",  # set mirror angle <arcsec>
    'PV_RBV': "X20U:OP:PGM1:MR.RBV",  # Readback mirror angle <arcsec>
    'PV_Motor': "X20U:OP:PGM1:MR.DMOV",  # status mirror motor <0,1>
    'PV_Motor_HLS': "X20U:OP:PGM1:MR.HLS",  # status mirror motor high limit <0,1>
    'PV_Motor_LLS': "X20U:OP:PGM1:MR.LLS",  # status mirror motor high limit <0,1>
    'PV_Motor_MOVN': "X20U:OP:PGM1:MR.MOVN",  # status mirror motor moving <0,1>
    'PV_Motor_DMOV': "X20U:OP:PGM1:MR.DMOV",  # status mirror motor done moving <0,1>
}

# PV names for Grating Rotation
PGM1_Grating = {
    'PV_SET': "X20U:OP:PGM1:GR.VAL",  # set grate angle <arcsec>
    'PV_RBV': "X20U:OP:PGM1:GR.RBV",  # Readback grate angle <arcsec>
    'PV_Type': "X20U:OP:PGM1:GRATE_TYPE",  # set grate type GRATE<1,2,3>
    'PV_Motor': "X20U:OP:PGM1:GR.DMOV",  # status mirror motor <0,1>
    'PV_Motor_HLS': "X20U:OP:PGM1:GR.HLS",  # status mirror motor high limit <0,1>
    'PV_Motor_LLS': "X20U:OP:PGM1:GR.LLS",  # status mirror motor high limit <0,1>
    'PV_Motor_MOVN': "X20U:OP:PGM1:GR.MOVN",  # status mirror motor moving <0,1>
    'PV_Motor_DMOV': "X20U:OP:PGM1:GR.DMOV",  # status mirror motor done moving <0,1>
}

# PV names for BPM X position
BPM_X = {
    'PV_SET': "X20U:SoftEX2:BPM:X.VAL",  # set position
    'PV_RBV': "X20U:SoftEX2:BPM:X.RBV",  # position read back
    'PV_Motor_MOVN': "X20U:SoftEX2:BPM:X.MOVN",  # motor X moving(0,1)
}

# PV names for BPM Z position
BPM_Z = {
    'PV_SET': "X20U:SoftEX2:BPM:Z.VAL",  # set position
    'PV_RBV': "X20U:SoftEX2:BPM:Z.RBV",  # position read back
    'PV_Motor_MOVN': "X20U:SoftEX2:BPM:Z.MOVN",  # motor Z moving (0,1)
}

# Full channels for scan 
FULL_Channels={"SoftEnergy":SoftEnergy,"PGM1_Grating":PGM1_Grating,"BPM_X":BPM_X,"BPM_Z":BPM_Z}