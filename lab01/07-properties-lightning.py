from vtkmodules.all import *


def create_light(color, position):
    light = vtkLight()
    light.SetColor(color)
    light.SetPosition(position)
    light.SetFocalPoint(0, 0, 0)
    return light


def create_sphere_actor(color, position):
    sphereSource = vtkSphereSource()
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(color)
    sphereActor.SetPosition(position)
    sphereActor.GetProperty().LightingOff()
    return sphereActor


def main():
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('Colored Lights and Spheres')
    renWin.SetSize(1280, 720)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
    positions = [(-5, 0, 0), (0, 0, -5), (5, 0, 0), (0, 0, 5)]

    for color, position in zip(colors, positions):
        light = create_light(color, position)
        ren.AddLight(light)
        sphereActor = create_sphere_actor(color, position)
        ren.AddActor(sphereActor)

    primitiveSource = vtkConeSource()
    primitiveSource.SetResolution(120)
    primitiveMapper = vtkPolyDataMapper()
    primitiveMapper.SetInputConnection(primitiveSource.GetOutputPort())
    primitiveActor = vtkActor()
    primitiveActor.SetMapper(primitiveMapper)
    ren.AddActor(primitiveActor)

    ren.SetBackground(0.1, 0.2, 0.3)

    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()
