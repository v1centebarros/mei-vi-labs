
from vtkmodules.all import (
    vtkConeSource, vtkPolyDataMapper, vtkActor,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkProperty
)

def main():
    # Cone source
    coneSource = vtkConeSource()
    coneSource.SetResolution(60)

    # Mapper
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    # Actor
    coneActor1 = vtkActor()
    coneActor1.SetMapper(coneMapper)

    coneActor2 = vtkActor()
    coneActor2.SetMapper(coneMapper)

    ren1 = vtkRenderer()
    ren1.AddActor(coneActor1)
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)
    ren1.SetBackground(0.1, 0.2, 0.4)

    ren2 = vtkRenderer()
    ren2.AddActor(coneActor2)
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)
    ren2.SetBackground(0.2, 0.3, 0.4)

    camera2 = ren2.GetActiveCamera()
    camera2.Azimuth(90)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    iren.Initialize()

    timerId = iren.CreateRepeatingTimer(100)
    def rotateCone(caller, event):
        coneActor1.RotateY(10)
        coneActor2.RotateY(10)
        renWin.Render()

    iren.AddObserver('TimerEvent', rotateCone)
    iren.Start()

if __name__ == '__main__':
    main()