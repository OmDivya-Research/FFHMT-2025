
#Named Selections
#Shroud_Rotor
ns= Model.AddNamedSelection()
ns.Name='Shroud_Rotor'
ns.Location
selinfo= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo.Ids= [481, 482, 480, 486]
ns.Location=selinfo

#Inlet_Rotor
ns1= Model.AddNamedSelection()
selinfo1= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo1.Ids= [484]
ns1.Name='Inlet_Rotor'
ns1.Location
ns1.Location=selinfo1

#Outlet_Rotor
ns2= Model.AddNamedSelection()
selinfo2= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo2.Ids= [483, 485]
ns2.Name='Outlet_Rotor'
ns2.Location
ns2.Location=selinfo2

#Hub
ns3= Model.AddNamedSelection()
selinfo3= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo3.Ids= [566, 478, 487, 488, 565, 549, 542, 479, 543, 489]
ns3.Name='Hub'
ns3.Location
ns3.Location=selinfo3

#Blades
ns4= Model.AddNamedSelection()
selinfo4= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo4.Ids= [490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 544, 545, 546, 547, 548, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616]
ns4.Name='Blades'
ns4.Location
ns4.Location=selinfo4


#MESHING
mesh=Model.Mesh
mesh.PhysicsPreference=MeshPhysicsPreferenceType.CFD
mesh.SolverPreference=MeshSolverPreferenceType.CFX
mesh.ElementSize=Quantity(200, 'mm')

#adding method
#method= mesh.AddAutomaticMethod()
#body= ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
#body.Ids= [732]
#method.Location=body
#method.Method=MethodType.CFXMesh

#generating mesh      
mesh.GenerateMesh()

#variable to check whether meshing is successful
mesh.ObjectState== ObjectState.Solved
'''NOTE : All workflows will not be recorded, as recording is under development.'''
