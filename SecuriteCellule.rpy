I-Logix-RPY-Archive version 8.8.0 C++ 6107223
{ IProject 
	- _id = GUID cffe8b29-6c77-4f3b-b8d2-34aa21e85f83;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 2;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "false";
								- _Type = Bool;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ObjectModelGe";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Class";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "0";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Object";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowAttributes";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowOperations";
								- _Value = "All";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "0";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "SecuriteCellule";
	- Stereotypes = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IHandle 
			- _m2Class = "IStereotype";
			- _filename = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy\\SysML.sbs";
			- _subsystem = "SysML";
			- _class = "";
			- _name = "SysML";
			- _id = GUID 052b8171-a32b-4f45-a829-5585f79f9deb;
		}
	}
	- _modifiedTimeWeak = 4.8.2015::13:15:57;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "ActorPkg.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "ActorPkg";
		- _id = GUID 14331ff6-82f2-4db4-8df3-5f659f98c480;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "ModelExecution.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "ModelExecution";
		- _id = GUID 88babf45-b008-4d4a-bafe-10b9ec8ec955;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 8;
		- value = 
		{ IProfile 
			- fileName = "SysML";
			- _persistAs = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy";
			- _id = GUID d9689b73-885e-44c4-896b-de43defa0a33;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "HarmonySE";
			- _persistAs = "$OMROOT\\Profiles\\HarmonySE";
			- _id = GUID 29d4fccc-40d9-4cb3-af8a-d7464f198819;
			- _isReference = 1;
		}
		{ ISubsystem 
			- fileName = "ActorPkg";
			- _id = GUID 14331ff6-82f2-4db4-8df3-5f659f98c480;
		}
		{ ISubsystem 
			- fileName = "FunctionalAnalysisPkg";
			- _id = GUID 5659bb82-d018-447f-abad-18e201048413;
		}
		{ ISubsystem 
			- fileName = "DesignSynthesisPkg";
			- _id = GUID ff38eafb-f744-4d90-ad71-2c94ef801dd5;
		}
		{ ISubsystem 
			- fileName = "RequirementsAnalysisPkg";
			- _id = GUID b9295c68-8c6f-488d-93fb-9c87064e75c2;
		}
		{ ISubsystem 
			- fileName = "TypesPkg";
			- _id = GUID fd6c6d68-bad0-4179-ae0f-04f6476301d1;
		}
		{ ISubsystem 
			- fileName = "InterfacesPkg";
			- _id = GUID 5b87bc2c-3340-44b9-86ff-66ccd26ea8a1;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- MSCS = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "ModelExecution";
			- _id = GUID 88babf45-b008-4d4a-bafe-10b9ec8ec955;
		}
	}
}

