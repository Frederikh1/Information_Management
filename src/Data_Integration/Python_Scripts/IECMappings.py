def loadIEC61850Mapping():
    iecMappings = {}

    # tBay
    tBayMapping = {}
    tBayMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tBay.csv"
    tBayMapping["@uniqueId"] = "name"
    tBayMapping["name"] = "name"
    tBayMapping["desc"] = "desc"
    iecMappings["tBay"] = tBayMapping

    # tConductingEquipment 
    tConductingEquipmentMapping = {}
    tConductingEquipmentMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tConductingEquipment.csv"
    tConductingEquipmentMapping["@uniqueId"] = "name"
    tConductingEquipmentMapping["name"] = "name"
    tConductingEquipmentMapping["desc"] = "desc"
    tConductingEquipmentMapping["virtual"] = "virtual"
    tConductingEquipmentMapping["conductingEquipmentType"] = "conductingEquipmentType"
    tConductingEquipmentMapping["tBayId"] = "tBayId"
    iecMappings["tConductingEquipment"] = tConductingEquipmentMapping

    # tGeneralEquipment 
    tGeneralEquipmentMapping = {}
    tGeneralEquipmentMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tGeneralEquipment.csv"
    tGeneralEquipmentMapping["@uniqueId"] = "name"
    tGeneralEquipmentMapping["name"] = "name"
    tGeneralEquipmentMapping["desc"] = "desc"
    tGeneralEquipmentMapping["virtual"] = "virtual"
    tGeneralEquipmentMapping["generalEquipmentEnum"] = "generalEquipmentEnum"
    iecMappings["tGeneralEquipment"] = tGeneralEquipmentMapping

    # tPowerTransformer
    tPowerTransformerMapping = {}
    tPowerTransformerMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tPowerTransformer.csv"
    tPowerTransformerMapping["@uniqueId"] = "name"
    tPowerTransformerMapping["name"] = "name"
    tPowerTransformerMapping["desc"] = "desc"
    tPowerTransformerMapping["virtual"] = "virtual"
    tPowerTransformerMapping["transformerType"] = "transformerType"
    iecMappings["tPowerTransformer"] = tPowerTransformerMapping
    
    # tSubEquipment
    tSubEquipmentMapping = {}
    tSubEquipmentMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tSubEquipment.csv"
    tSubEquipmentMapping["@uniqueId"] = "name"
    tSubEquipmentMapping["name"] = "name"
    tSubEquipmentMapping["desc"] = "desc"
    tSubEquipmentMapping["virtual"] = "virtual"
    tSubEquipmentMapping["phase"] = "phase"
    iecMappings["tSubEquipment"] = tSubEquipmentMapping

    # tSubstation
    tSubstationMapping = {}
    tSubstationMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tSubstation.csv"
    tSubstationMapping["@uniqueId"] = "name"
    tSubstationMapping["name"] = "name"
    tSubstationMapping["desc"] = "desc"
    iecMappings["tSubstation"] = tSubstationMapping
    
    # tTapChanger
    tTapChangerMapping = {}
    tTapChangerMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTapChanger.csv"
    tTapChangerMapping["@uniqueId"] = "name"
    tTapChangerMapping["name"] = "name"
    tTapChangerMapping["desc"] = "desc"
    tTapChangerMapping["tTransformerWindingId"] = "tTransformerWindingId"
    iecMappings["tTapChanger"] = tTapChangerMapping

    # tTerminal
    tTerminalMapping = {}
    tTerminalMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tTerminalMapping["@uniqueId"] = "optionalName"
    tTerminalMapping["neutralPoint"] = "neutralPoint"
    tTerminalMapping["optionalName"] = "optionalName"
    iecMappings["tTerminal"] = tTerminalMapping
    
    # tTransformerWinding
    tTransformerWindingMapping = {}
    tTransformerWindingMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTransformerWinding.csv"
    tTransformerWindingMapping["@uniqueId"] = "name"
    tTransformerWindingMapping["desc"] = "desc"
    tTransformerWindingMapping["name"] = "name"
    tTransformerWindingMapping["virtual"] = "virtual"
    tTransformerWindingMapping["transformerType"] = "transformerType"
    tTransformerWindingMapping["tPowerTransformerId"] = "tPowerTransformerId"
    iecMappings["tTransformerWinding"] = tTransformerWindingMapping
    
    # tVoltage
    tVoltageMapping = {}
    tVoltageMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tVoltage.csv"
    tVoltageMapping["@uniqueId"] = "value"
    tVoltageMapping["value"] = "value"
    iecMappings["tVoltage"] = tVoltageMapping
    
    # tVoltageLevel
    tVoltageLevelMapping = {}
    tVoltageLevelMapping["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tVoltageLevel.csv"
    tVoltageLevelMapping["@uniqueId"] = "name"
    tVoltageLevelMapping["desc"] = "desc"
    tVoltageLevelMapping["name"] = "name"
    tVoltageLevelMapping["tSubstationId"] = "tSubstationId"
    iecMappings["tVoltageLevel"] = tVoltageLevelMapping

    # Relationship Mappings:
    
    tVoltageLevelVoltage  = {}
    tVoltageLevelVoltage["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tVoltageLevel.csv"
    tVoltageLevelVoltage["@domain"] = "tVoltageId"
    tVoltageLevelVoltage["@range"] = "name"
    iecMappings["VoltageLevel.Voltage"] = tVoltageLevelVoltage
    
    tAbstractConductingEquipmentTerminal  = {}
    tAbstractConductingEquipmentTerminal["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tAbstractConductingEquipmentTerminal["@domain"] = "tAbstractConductingEquipmentId"
    tAbstractConductingEquipmentTerminal["@range"] = "name"
    iecMappings["AbstractConductingEquipment.Terminal"] = tAbstractConductingEquipmentTerminal

    tTerminalSubstation  = {}
    tTerminalSubstation["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tTerminalSubstation["@domain"] = "tSubstationId"
    tTerminalSubstation["@range"] = "optionalName"
    iecMappings["Terminal.Substation"] = tTerminalSubstation

    tTransformerWindingTerminal  = {}
    tTransformerWindingTerminal["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTransformerWinding.csv"
    tTransformerWindingTerminal["@domain"] = "tTerminalId"
    tTransformerWindingTerminal["@range"] = "name"
    iecMappings["TransformerWinding.Terminal"] = tTransformerWindingTerminal

    tSubstationVoltageLevel  = {}
    tSubstationVoltageLevel["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tSubstation.csv"
    tSubstationVoltageLevel["@domain"] = "tVoltageLevelId"
    tSubstationVoltageLevel["@range"] = "name"
    iecMappings["Substation.VoltageLevel"] = tSubstationVoltageLevel

    tTerminalVoltageLevel  = {}
    tTerminalVoltageLevel["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tTerminalVoltageLevel["@domain"] = "tVoltageLevelId"
    tTerminalVoltageLevel["@range"] = "optionalName"
    iecMappings["Terminal.VoltageLevel"] = tTerminalVoltageLevel

    tTapChangerSubEquipment  = {}
    tTapChangerSubEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTapChanger.csv"
    tTapChangerSubEquipment["@domain"] = "tSubEquipmentId"
    tTapChangerSubEquipment["@range"] = "name"
    iecMappings["TapChanger.SubEquipment"] = tTapChangerSubEquipment

    tAbstractConductingEquipmentSubEquipment  = {}
    tAbstractConductingEquipmentSubEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tSubEquipment.csv"
    tAbstractConductingEquipmentSubEquipment["@domain"] = "tAbstractConductingEquipmentId"
    tAbstractConductingEquipmentSubEquipment["@range"] = "name"
    iecMappings["AbstractConductingEquipment.SubEquipment"] = tAbstractConductingEquipmentSubEquipment

    tPowerTransformerSubEquipment  = {}
    tPowerTransformerSubEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tPowerTransformer.csv"
    tPowerTransformerSubEquipment["@domain"] = "tSubEquipmentId"
    tPowerTransformerSubEquipment["@range"] = "name"
    iecMappings["PowerTransformer.SubEquipment"] = tPowerTransformerSubEquipment

    tEquipmentContainerGeneralEquipment  = {}
    tEquipmentContainerGeneralEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tGeneralEquipment.csv"
    tEquipmentContainerGeneralEquipment["@domain"] = "tGeneralEquipmentId"
    tEquipmentContainerGeneralEquipment["@range"] = "name"
    iecMappings["EquipmentContainer.GeneralEquipment"] = tEquipmentContainerGeneralEquipment

    tFunctionGeneralEquipment  = {}
    tFunctionGeneralEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tGeneralEquipment.csv"
    tFunctionGeneralEquipment["@domain"] = "tFunctionId"
    tFunctionGeneralEquipment["@range"] = "name"
    iecMappings["Function.GeneralEquipment"] = tFunctionGeneralEquipment

    tSubFunctionGeneralEquipment  = {}
    tSubFunctionGeneralEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tGeneralEquipment.csv"
    tSubFunctionGeneralEquipment["@domain"] = "tSubFunctionId"
    tSubFunctionGeneralEquipment["@range"] = "name"
    iecMappings["SubFunction.GeneralEquipment"] = tSubFunctionGeneralEquipment

    tVoltageLevelFunction  = {}
    tVoltageLevelFunction["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tVoltageLevel.csv"
    tVoltageLevelFunction["@domain"] = "name"
    tVoltageLevelFunction["@range"] = "tFunctionId"
    iecMappings["VoltageLevel.Function"] = tVoltageLevelFunction

    tBayFunction  = {}
    tBayFunction["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tBay.csv"
    tBayFunction["@domain"] = "name"
    tBayFunction["@range"] = "tFunctionId"
    iecMappings["Bay.Function"] = tBayFunction

    tSubstationFunction  = {}
    tSubstationFunction["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tSubstation.csv"
    tSubstationFunction["@domain"] = "name"
    tSubstationFunction["@range"] = "tFunctionId"
    iecMappings["Substation.Function"] = tSubstationFunction

    tTerminalConnectivityNode  = {}
    tTerminalConnectivityNode["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tTerminalConnectivityNode["@domain"] = "name"
    tTerminalConnectivityNode["@range"] = "tConnectivityNodeId"
    iecMappings["Terminal.ConnectivityNode"] = tTerminalConnectivityNode

    tBayConnectivityNode  = {}
    tBayConnectivityNode["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tBay.csv"
    tBayConnectivityNode["@domain"] = "name"
    tBayConnectivityNode["@range"] = "tConnectivityNodeId"
    iecMappings["Bay.ConnectivityNode"] = tBayConnectivityNode

    tFunctionConductingEquipment  = {}
    tFunctionConductingEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tConductingEquipment.csv"
    tFunctionConductingEquipment["@domain"] = "tFunctionId"
    tFunctionConductingEquipment["@range"] = "name"
    iecMappings["Function.ConductingEquipment"] = tFunctionConductingEquipment

    tSubFunctionConductingEquipment  = {}
    tSubFunctionConductingEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tConductingEquipment.csv"
    tSubFunctionConductingEquipment["@domain"] = "tSubFunctionId"
    tSubFunctionConductingEquipment["@range"] = "name"
    iecMappings["SubFunction.ConductingEquipment"] = tSubFunctionConductingEquipment

    tBayConductingEquipment  = {}
    tBayConductingEquipment["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tBay.csv"
    tBayConductingEquipment["@domain"] = "tConductingEquipmentId"
    tBayConductingEquipment["@range"] = "name"
    iecMappings["Bay.ConductingEquipment"] = tBayConductingEquipment
    
    tVoltageLevelBay  = {}
    tVoltageLevelBay["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tVoltageLevel.csv"
    tVoltageLevelBay["@domain"] = "tBayId"
    tVoltageLevelBay["@range"] = "name"
    iecMappings["VoltageLevel.Bay"] = tVoltageLevelBay

    tTerminalBay  = {}
    tTerminalBay["@fileName"] = "https://raw.githubusercontent.com/Frederikh1/cim_ontology/main/IEC_Data/tTerminal.csv"
    tTerminalBay["@domain"] = "tBayId"
    tTerminalBay["@range"] = "optionalName"
    iecMappings["Terminal.Bay"] = tTerminalBay

    return iecMappings