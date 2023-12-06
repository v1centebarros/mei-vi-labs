import vtk

# Create a sphere
sphere = vtk.vtkSphereSource()
sphere.SetRadius(1.0)
sphere.SetThetaResolution(18)
sphere.SetPhiResolution(18)

sphere_mapper = vtk.vtkPolyDataMapper()
sphere_mapper.SetInputConnection(sphere.GetOutputPort())

sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)

# Create a cylinder
cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(0.5)
cylinder.SetHeight(2.0)
cylinder.SetResolution(18)

cylinder_mapper = vtk.vtkPolyDataMapper()
cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())

cylinder_actor = vtk.vtkActor()
cylinder_actor.SetMapper(cylinder_mapper)

# Renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(sphere_actor)
renderer.AddActor(cylinder_actor)
renderer.SetBackground(0.1, 0.2, 0.4)  # Background color

# Render Window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(800, 600)

# Interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Start
render_window.Render()
render_window_interactor.Start()
