###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical
# and can be found in most VTK programs

# Imports

# Import all VTK modules
from vtkmodules.all import *

# Import only needed modules
# import vtkmodules.vtkInteractionStyle
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

def main():
    sphere = vtkSphereSource()
    sphere.SetRadius(2.0)
    sphere.SetThetaResolution(18)
    sphere.SetPhiResolution(18)

    sphere_mapper = vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere.GetOutputPort())

    sphere_actor = vtkActor()
    sphere_actor.SetMapper(sphere_mapper)

    # Create a cylinder
    cylinder = vtkCylinderSource()
    cylinder.SetRadius(2)
    cylinder.SetHeight(3)
    cylinder.SetResolution(18)

    cylinder_mapper = vtkPolyDataMapper()
    cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())

    cylinder_actor = vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)


    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    # ren.AddActor(sphere_actor)
    ren.AddActor(cylinder_actor)
    ren.SetBackground(0.1, 0.2, 0.3)

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetWindowName('Cone')
    renWin.SetSize(300,300)



    # Now we loop over 360 degrees and render the cone each time.
    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()