
#Named Selections
#Inlet
ns= Model.AddNamedSelection()
ns.Name='Inlet'
ns.Location
selinfo= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo.Ids= [53]
ns.Location=selinfo

#Opening
ns1= Model.AddNamedSelection()
selinfo1= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo1.Ids= [50, 51, 52]
ns1.Name='Opening'
ns1.Location
ns1.Location=selinfo1

#Shroud_Solid
ns2= Model.AddNamedSelection()
selinfo2= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo2.Ids= [47, 60, 49, 54]
ns2.Name='Shroud_Solid'
ns2.Location
ns2.Location=selinfo2

#Inlet_Solid
ns3= Model.AddNamedSelection()
selinfo3= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo3.Ids= [56]
ns3.Name='Inlet_Solid'
ns3.Location
ns3.Location=selinfo3

#Outlet_Solid
ns4= Model.AddNamedSelection()
selinfo4= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo4.Ids= [61, 55]
ns4.Name='Outlet_Solid'
ns4.Location
ns4.Location=selinfo4

#Shaft_Bosscap
ns4= Model.AddNamedSelection()
selinfo4= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo4.Ids= [48, 57, 58, 59]
ns4.Name='Shaft_Bosscap'
ns4.Location
ns4.Location=selinfo4


#MESHING
mesh=Model.Mesh
mesh.PhysicsPreference=MeshPhysicsPreferenceType.CFD
mesh.SolverPreference=MeshSolverPreferenceType.CFX
mesh.ElementSize=Quantity(25, 'mm')

#adding method
method= mesh.AddAutomaticMethod()
body= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
body.Ids= [66]
method.Location=body
method.Method=MethodType.CFXMesh

#generating mesh
mesh.GenerateMesh()

#variable to check whether meshing is successful
mesh.ObjectState== ObjectState.Solved