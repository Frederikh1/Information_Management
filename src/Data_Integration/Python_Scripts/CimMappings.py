def loadCIMMapping():

    cimMappings = {}

    # BaseFrequency
    baseFrequencyMapping = {}
    baseFrequencyMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/BaseFrequency.csv"
    baseFrequencyMapping["@uniqueId"] = "mRID"
    baseFrequencyMapping["mRID"] = "mRID"
    baseFrequencyMapping["aliasName"] = "aliasName"
    baseFrequencyMapping["description"] = "description"
    baseFrequencyMapping["name"] = "name"
    baseFrequencyMapping["frequency"] = "baseFrequency"
    cimMappings["BaseFrequency"] = baseFrequencyMapping

    # BasePower
    basePowerMapping = {}
    basePowerMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/BasePower.csv"
    basePowerMapping["@uniqueId"] = "mRID"
    basePowerMapping["mRID"] = "mRID"
    basePowerMapping["aliasName"] = "aliasName"
    basePowerMapping["description"] = "description"
    basePowerMapping["name"] = "name"
    basePowerMapping["basePower"] = "basePower"
    cimMappings["BasePower"] = basePowerMapping

    # BaseVoltage
    baseVoltageMapping = {}
    baseVoltageMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/BaseVoltage.csv"
    baseVoltageMapping["@uniqueId"] = "mRID"
    baseVoltageMapping["mRID"] = "mRID"
    baseVoltageMapping["aliasName"] = "aliasName"
    baseVoltageMapping["description"] = "description"
    baseVoltageMapping["name"] = "name"
    baseVoltageMapping["nominalVoltage"] = "nominalVoltage"
    cimMappings["BaseVoltage"] = baseVoltageMapping

    # Bay
    bayMapping = {}
    bayMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Bay.csv"
    bayMapping["@uniqueId"] = "mRID"
    bayMapping["mRID"] = "mRID"
    bayMapping["aliasName"] = "aliasName"
    bayMapping["description"] = "description"
    bayMapping["name"] = "name"
    bayMapping["bayEnergyMeasFlag"] = "bayEnergyMeasFlag"
    bayMapping["bayPowerMeasFlag"] = "bayPowerMeasFlag"
    bayMapping["VoltageLevelId"] = "VoltageLevelId"
    bayMapping["SubstationId"] = "SubstationId"
    cimMappings["Bay"] = bayMapping

    # Breaker
    breakerMapping = {}
    breakerMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Breaker.csv"
    breakerMapping["@uniqueId"] = "mRID"
    breakerMapping["mRID"] = "mRID"
    breakerMapping["aliasName"] = "aliasName"
    breakerMapping["description"] = "description"
    breakerMapping["name"] = "name"
    breakerMapping["aggregate"] = "aggregate"
    breakerMapping["inService"] = "inService"
    breakerMapping["networkAnalysisEnabled"] = "networkAnalysisEnabled"
    breakerMapping["normallyInService"] = "normallyInService"
    breakerMapping["normalOpen"] = "normalOpen"
    breakerMapping["retained"] = "retained"
    breakerMapping["open"] = "open"
    breakerMapping["locked"] = "locked"
    breakerMapping["switchOnCount"] = "switchOnCount"
    breakerMapping["switchOnDate"] = "switchOnDate"
    breakerMapping["inTransitTime"] = "inTransitTime"
    cimMappings["Breaker"] = breakerMapping

    # ConductingEquipment
    conductingEquipmentMapping = {}
    conductingEquipmentMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConductingEquipment.csv"
    conductingEquipmentMapping["@uniqueId"] = "mRID"
    conductingEquipmentMapping["mRID"] = "mRID"
    conductingEquipmentMapping["aliasName"] = "aliasName"
    conductingEquipmentMapping["description"] = "description"
    conductingEquipmentMapping["name"] = "name"
    conductingEquipmentMapping["aggregate"] = "aggregate"
    conductingEquipmentMapping["inService"] = "inService"
    conductingEquipmentMapping["networkAnalysisEnabled"] = "networkAnalysisEnabled"
    conductingEquipmentMapping["normallyInService"] = "normallyInService"
    conductingEquipmentMapping["BaseVoltageId"] = "BaseVoltageId"
    cimMappings["ConductingEquipment"] = conductingEquipmentMapping

    # ConnectivityNode
    connectivityNodeMapping = {}
    connectivityNodeMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConnectivityNode.csv"
    connectivityNodeMapping["@uniqueId"] = "mRID"
    connectivityNodeMapping["mRID"] = "mRID"
    connectivityNodeMapping["aliasName"] = "aliasName"
    connectivityNodeMapping["description"] = "description"
    connectivityNodeMapping["name"] = "name"
    cimMappings["ConnectivityNode"] = connectivityNodeMapping

    # Equipment
    equipmentMapping = {}
    equipmentMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Equipment.csv"
    equipmentMapping["@uniqueId"] = "mRID"
    equipmentMapping["mRID"] = "mRID"
    equipmentMapping["aliasName"] = "aliasName"
    equipmentMapping["description"] = "description"
    equipmentMapping["name"] = "name"
    equipmentMapping["aggregate"] = "aggregate"
    equipmentMapping["inService"] = "inService"
    equipmentMapping["networkAnalysisEnabled"] = "networkAnalysisEnabled"
    equipmentMapping["normallyInService"] = "normallyInService"
    equipmentMapping["PSRTypeId"] = "PSRTypeId"
    cimMappings["Equipment"] = equipmentMapping

    # GeographicalRegion
    geographicalRegionMapping = {}
    geographicalRegionMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/GeographicalRegion.csv"
    geographicalRegionMapping["@uniqueId"] = "mRID"
    geographicalRegionMapping["mRID"] = "mRID"
    geographicalRegionMapping["aliasName"] = "aliasName"
    geographicalRegionMapping["description"] = "description"
    geographicalRegionMapping["name"] = "name"
    cimMappings["GeographicalRegion"] = geographicalRegionMapping

    # Name
    nameMapping = {}
    nameMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Name.csv"
    nameMapping["@uniqueId"] = "name"
    nameMapping["name"] = "name"
    cimMappings["Name"] = nameMapping

    # PSRType
    psrTypeMapping = {}
    psrTypeMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/PSRType.csv"
    psrTypeMapping["@uniqueId"] = "mRID"
    psrTypeMapping["mRID"] = "mRID"
    psrTypeMapping["aliasName"] = "aliasName"
    psrTypeMapping["description"] = "description"
    psrTypeMapping["name"] = "name"
    cimMappings["PSRType"] = psrTypeMapping

    # PhaseCode
    phaseCodeMapping = {}
    phaseCodeMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/PhaseCode.csv"
    phaseCodeMapping["@uniqueId"] = "literal"
    phaseCodeMapping["literal"] = "literal"
    phaseCodeMapping["value"] = "value"
    phaseCodeMapping["description"] = "description"
    cimMappings["PhaseCode"] = phaseCodeMapping    

    # ProtectedSwitch
    protectedSwitchMapping = {}
    protectedSwitchMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ProtectedSwitch.csv"
    protectedSwitchMapping["@uniqueId"] = "mRID"
    protectedSwitchMapping["mRID"] = "mRID"
    protectedSwitchMapping["aliasName"] = "aliasName"
    protectedSwitchMapping["description"] = "description"
    protectedSwitchMapping["name"] = "name"
    protectedSwitchMapping["aggregate"] = "aggregate"
    protectedSwitchMapping["inService"] = "inService"
    protectedSwitchMapping["networkAnalysisEnabled"] = "networkAnalysisEnabled"
    protectedSwitchMapping["normallyInService"] = "normallyInService"
    protectedSwitchMapping["normalOpen"] = "normalOpen"
    protectedSwitchMapping["retained"] = "retained"
    protectedSwitchMapping["open"] = "open"
    protectedSwitchMapping["locked"] = "locked"
    protectedSwitchMapping["switchOnCount"] = "switchOnCount"
    protectedSwitchMapping["switchOnDate"] = "switchOnDate"
    protectedSwitchMapping["breakingCapacity"] = "breakingCapacity"
    cimMappings["ProtectedSwitch"] = protectedSwitchMapping

    # SubGeographicalRegion
    subGeographicalRegionMapping = {}
    subGeographicalRegionMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/SubGeographicalRegion.csv"
    subGeographicalRegionMapping["@uniqueId"] = "mRID"
    subGeographicalRegionMapping["mRID"] = "mRID"
    subGeographicalRegionMapping["aliasName"] = "aliasName"
    subGeographicalRegionMapping["description"] = "description"
    subGeographicalRegionMapping["name"] = "name"
    subGeographicalRegionMapping["GeographicalRegionId"] = "GeographicalRegionId"
    cimMappings["SubGeographicalRegion"] = subGeographicalRegionMapping

    # Substation
    substationMapping = {}
    substationMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Substation.csv"
    substationMapping["@uniqueId"] = "mRID"
    substationMapping["mRID"] = "mRID"
    substationMapping["aliasName"] = "aliasName"
    substationMapping["description"] = "description"
    substationMapping["name"] = "name"
    substationMapping["subGeographicalRegionId"] = "subGeographicalRegionId"
    cimMappings["Substation"] = substationMapping

    # Switch
    switchMapping = {}
    switchMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Switch.csv"
    switchMapping["@uniqueId"] = "mRID"
    switchMapping["mRID"] = "mRID"
    switchMapping["aliasName"] = "aliasName"
    switchMapping["description"] = "description"
    switchMapping["name"] = "name"
    switchMapping["aggregate"] = "aggregate"
    switchMapping["inService"] = "inService"
    switchMapping["networkAnalysisEnabled"] = "networkAnalysisEnabled"
    switchMapping["normallyInService"] = "normallyInService"
    switchMapping["normalOpen"] = "normalOpen"
    switchMapping["switchOnCount"] = "switchOnCount"
    switchMapping["switchOnDate"] = "switchOnDate"
    switchMapping["retained"] = "retained"
    switchMapping["open"] = "open"
    switchMapping["locked"] = "locked"
    cimMappings["Switch"] = switchMapping

    # TapChanger
    tapChangerMapping = {}
    tapChangerMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/TapChanger.csv"
    tapChangerMapping["@uniqueId"] = "mRID"
    tapChangerMapping["mRID"] = "mRID"
    tapChangerMapping["aliasName"] = "aliasName"
    tapChangerMapping["description"] = "description"
    tapChangerMapping["name"] = "name"
    tapChangerMapping["controlEnabled"] = "controlEnabled"
    tapChangerMapping["highStep"] = "highStep"
    tapChangerMapping["initialDelay"] = "initialDelay"
    tapChangerMapping["lowStep"] = "lowStep"
    tapChangerMapping["ltcFlag"] = "ltcFlag"
    tapChangerMapping["normalStep"] = "normalStep"
    tapChangerMapping["neutralStep"] = "neutralStep"
    tapChangerMapping["subsequentDelay"] = "subsequentDelay"
    tapChangerMapping["step"] = "step"
    cimMappings["TapChanger"] = tapChangerMapping

    # Terminal
    terminalMapping = {}
    terminalMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    terminalMapping["@uniqueId"] = "mRID"
    terminalMapping["mRID"] = "mRID"
    terminalMapping["aliasName"] = "aliasName"
    terminalMapping["description"] = "description"
    terminalMapping["name"] = "name"
    terminalMapping["connected"] = "connected"
    terminalMapping["sequenceNumber"] = "sequenceNumber"
    terminalMapping["phasesId"] = "phasesId"
    terminalMapping["ConductingEquipmentId"] = "ConductingEquipmentId"
    terminalMapping["ConnectivityNodeId"] = "ConnectivityNodeId"
    cimMappings["Terminal"] = terminalMapping

    # VoltageLevel
    voltageLevelMapping = {}
    voltageLevelMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/VoltageLevel.csv"
    voltageLevelMapping["@uniqueId"] = "mRID"
    voltageLevelMapping["mRID"] = "mRID"
    voltageLevelMapping["aliasName"] = "aliasName"
    voltageLevelMapping["description"] = "description"
    voltageLevelMapping["name"] = "name"
    voltageLevelMapping["highVoltageLimit"] = "highVoltageLimit"
    voltageLevelMapping["lowVoltageLimit"] = "lowVoltageLimit"
    voltageLevelMapping["BaseVoltageId"] = "BaseVoltageId"
    voltageLevelMapping["SubstationId"] = "SubstationId"
    cimMappings["VoltageLevel"] = voltageLevelMapping

    # Relationship Mappings

    VoltageLevelBays  = {}
    VoltageLevelBays["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Bay.csv"
    VoltageLevelBays["@domain"] = "mRID"
    VoltageLevelBays["@range"] = "VoltageLevelId"
    cimMappings["VoltageLevel.Bays"] = VoltageLevelBays

    BaysVoltageLevel  = {}
    BaysVoltageLevel["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Bay.csv"
    BaysVoltageLevel["@domain"] = "VoltageLevelId"
    BaysVoltageLevel["@range"] = "mRID"
    cimMappings["Bay.VoltageLevel"] = BaysVoltageLevel

    #

    SubstationBays = {}
    SubstationBays["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Bay.csv"
    SubstationBays["@domain"] = "mRID"
    SubstationBays["@range"] = "SubstationId"
    cimMappings["Substation.Bays"] = SubstationBays

    BaysSubstation = {}
    BaysSubstation["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Bay.csv"
    BaysSubstation["@domain"] = "SubstationId"
    BaysSubstation["@range"] = "mRID"
    cimMappings["Bay.Substation"] = BaysSubstation

    #

    BaseVoltageConductingEquipment = {}
    BaseVoltageConductingEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConductingEquipment.csv"
    BaseVoltageConductingEquipment["@domain"] = "mRID"
    BaseVoltageConductingEquipment["@range"] = "BaseVoltageId"
    cimMappings["BaseVoltage.ConductingEquipment"] = BaseVoltageConductingEquipment

    ConductingEquipmentBaseVoltage = {}
    ConductingEquipmentBaseVoltage["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConductingEquipment.csv"
    ConductingEquipmentBaseVoltage["@domain"] = "BaseVoltageId"
    ConductingEquipmentBaseVoltage["@range"] = "mRID"
    cimMappings["ConductingEquipment.BaseVoltage"] = ConductingEquipmentBaseVoltage

    #

    ConnectivityNodeContainerConnectivityNode = {}
    ConnectivityNodeContainerConnectivityNode["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConnectivityNode.csv"
    ConnectivityNodeContainerConnectivityNode["@domain"] = "mRID"
    ConnectivityNodeContainerConnectivityNode["@range"] = "ConnectivityNodeContainerId"
    cimMappings["ConnectivityNodeContainer.ConnectivityNodes"] = ConnectivityNodeContainerConnectivityNode

    ConnectivityNodeConnectivityNodeContainer = {}
    ConnectivityNodeConnectivityNodeContainer["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/ConnectivityNode.csv"
    ConnectivityNodeConnectivityNodeContainer["@domain"] = "ConnectivityNodeContainerId"
    ConnectivityNodeConnectivityNodeContainer["@range"] = "mRID"
    cimMappings["ConnectivityNode.ConnectivityNodeContainer"] = ConnectivityNodeConnectivityNodeContainer

    #

    EquipmentContainerEquipment = {}
    EquipmentContainerEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Equipment.csv"
    EquipmentContainerEquipment["@domain"] = "mRID"
    EquipmentContainerEquipment["@range"] = "EquipmentContainerId"
    cimMappings["EquipmentContainer.Equipments"] = EquipmentContainerEquipment

    EquipmentEquipmentContainer = {}
    EquipmentEquipmentContainer["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Equipment.csv"
    EquipmentEquipmentContainer["@domain"] = "EquipmentContainerId"
    EquipmentEquipmentContainer["@range"] = "mRID"
    cimMappings["Equipment.EquipmentContainer"] = EquipmentEquipmentContainer

    #

    PSRTypePowerSystemResource = {}
    PSRTypePowerSystemResource["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/PowerSystemResource.csv"
    PSRTypePowerSystemResource["@domain"] = "mRID"
    PSRTypePowerSystemResource["@range"] = "PSRTypeId"
    cimMappings["PSRType.PowerSystemResources"] = PSRTypePowerSystemResource

    PowerSystemResourcePSRType = {}
    PowerSystemResourcePSRType["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/PowerSystemResource.csv"
    PowerSystemResourcePSRType["@domain"] = "PSRTypeId"
    PowerSystemResourcePSRType["@range"] = "mRID"
    cimMappings["PowerSystemResource.PSRType"] = PowerSystemResourcePSRType

    #

    GeographicalRegionSubGeographicalRegion = {}
    GeographicalRegionSubGeographicalRegion["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/SubGeographicalRegion.csv"
    GeographicalRegionSubGeographicalRegion["@domain"] = "mRID"
    GeographicalRegionSubGeographicalRegion["@range"] = "GeographicalRegionId"
    cimMappings["GeographicalRegion.Regions"] = GeographicalRegionSubGeographicalRegion

    SubGeographicalRegionGeographicalRegion = {}
    SubGeographicalRegionGeographicalRegion["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/SubGeographicalRegion.csv"
    SubGeographicalRegionGeographicalRegion["@domain"] = "GeographicalRegionId"
    SubGeographicalRegionGeographicalRegion["@range"] = "mRID"
    cimMappings["SubGeographicalRegion.Region"] = SubGeographicalRegionGeographicalRegion

    #

    SubGeographicalRegionSubstation = {}
    SubGeographicalRegionSubstation["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Substation.csv"
    SubGeographicalRegionSubstation["@domain"] = "mRID"
    SubGeographicalRegionSubstation["@range"] = "subGeographicalRegionId"
    cimMappings["SubGeographicalRegion.Substations"] = SubGeographicalRegionSubstation

    SubstationSubGeographicalRegion = {}
    SubstationSubGeographicalRegion["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Substation.csv"
    SubstationSubGeographicalRegion["@domain"] = "subGeographicalRegionId"
    SubstationSubGeographicalRegion["@range"] = "mRID"
    cimMappings["Substation.Region"] = SubstationSubGeographicalRegion

    #

    TerminalPhase = {}
    TerminalPhase["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    TerminalPhase["@domain"] = "phasesId"
    TerminalPhase["@range"] = "mRID"
    cimMappings["Terminal.phases"] = TerminalPhase

    #

    ConductingEquipmentTerminal = {}
    ConductingEquipmentTerminal["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    ConductingEquipmentTerminal["@domain"] = "mRID"
    ConductingEquipmentTerminal["@range"] = "ConductingEquipmentId"
    cimMappings["ConductingEquipment.Terminals"] = ConductingEquipmentTerminal

    TerminalConductingEquipment = {}
    TerminalConductingEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    TerminalConductingEquipment["@domain"] = "ConductingEquipmentId"
    TerminalConductingEquipment["@range"] = "mRID"
    cimMappings["Terminal.ConductingEquipment"] = TerminalConductingEquipment

    #

    ConnectivityNodeTerminal = {}
    ConnectivityNodeTerminal["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    ConnectivityNodeTerminal["@domain"] = "mRID"
    ConnectivityNodeTerminal["@range"] = "ConnectivityNodeId"
    cimMappings["ConnectivityNode.Terminals"] = ConnectivityNodeTerminal

    TerminalConnectivityNode = {}
    TerminalConnectivityNode["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/Terminal.csv"
    TerminalConnectivityNode["@domain"] = "ConnectivityNodeId"
    TerminalConnectivityNode["@range"] = "mRID"
    cimMappings["Terminal.ConnectivityNode"] = TerminalConnectivityNode

    #

    BaseVoltageVoltageLevel = {}
    BaseVoltageVoltageLevel["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/VoltageLevel.csv"
    BaseVoltageVoltageLevel["@domain"] = "mRID"
    BaseVoltageVoltageLevel["@range"] = "BaseVoltageId"
    cimMappings["BaseVoltage.VoltageLevel"] = BaseVoltageVoltageLevel

    VoltageLevelBaseVoltage = {}
    VoltageLevelBaseVoltage["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/VoltageLevel.csv"
    VoltageLevelBaseVoltage["@domain"] = "BaseVoltageId"
    VoltageLevelBaseVoltage["@range"] = "mRID"
    cimMappings["VoltageLevel.BaseVoltage"] = VoltageLevelBaseVoltage

    #

    SubstationVoltageLevel = {}
    SubstationVoltageLevel["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/VoltageLevel.csv"
    SubstationVoltageLevel["@domain"] = "mRID"
    SubstationVoltageLevel["@range"] = "SubstationId"
    cimMappings["Substation.VoltageLevels"] = SubstationVoltageLevel

    VoltageLevelSubstation = {}
    VoltageLevelSubstation["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/CIM_Data/VoltageLevel.csv"
    VoltageLevelSubstation["@domain"] = "SubstationId"
    VoltageLevelSubstation["@range"] = "mRID"
    cimMappings["VoltageLevel.Substation"] = VoltageLevelSubstation

    return cimMappings