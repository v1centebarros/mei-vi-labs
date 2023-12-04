from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource, vtkCylinderSource
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor, vtkRenderer, vtkRenderWindow

def generate_cone():
    cone_source = vtkConeSource()
    cone_source.SetResolution(16)
    cone_mapper = vtkPolyDataMapper()
    cone_mapper.SetInputConnection(cone_source.GetOutputPort())
    cone_actor = vtkActor()
    cone_actor.SetMapper(cone_mapper)
    # resize the cone with height 2 and radius 1
    cone_actor.SetScale(2, 1, 1)

    return cone_actor


def generate_sphere():
    sphere_source = vtkSphereSource()
    sphere_source.SetThetaResolution(18)
    sphere_source.SetPhiResolution(18)
    sphere_source.SetRadius(2.0)

    sphere_mapper = vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere_source.GetOutputPort())

    sphere_actor = vtkActor()
    sphere_actor.SetMapper(sphere_mapper)

    return sphere_actor


def generate_cylinder():
    cylinder_source = vtkCylinderSource()
    cylinder_source.SetResolution(18)
    cylinder_source.SetRadius(2)
    cylinder_source.SetHeight(3)

    cylinder_mapper = vtkPolyDataMapper()
    cylinder_mapper.SetInputConnection(cylinder_source.GetOutputPort())

    cylinder_actor = vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)

    return cylinder_actor


def main():
    ren = vtkRenderer()
    ren.SetBackground(1, 1, 1)
    # ren.AddActor(generate_cone())
    ren.AddActor(generate_sphere())

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.

    ren_win = vtkRenderWindow()
    ren_win.SetSize(300, 300)
    ren_win.AddRenderer(ren)

    ren_win.SetWindowName('Cone')

    # Now we loop over 360 degrees and render the cone each time.
    for _ in range(0, 360):
        # render the image
        ren_win.Render()
        # rotate the active camera by one degree
        ren.GetActiveCamera().Azimuth(1)


if __name__ == '__main__':
    main()
