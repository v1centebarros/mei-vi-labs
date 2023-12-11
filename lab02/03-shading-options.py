from vtkmodules.all import (
    vtkSphereSource, vtkPolyDataMapper, vtkActor,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor
)

def main():
    # sphere source
    sphereSource = vtkSphereSource()
    sphereSource.SetPhiResolution(12)
    sphereSource.SetThetaResolution(12)

    # Mapper
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # Actor
    sphereActor1 = vtkActor()
    sphereActor1.SetMapper(sphereMapper)
    sphereActor1.GetProperty().SetInterpolationToFlat()

    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper)
    sphereActor2.GetProperty().SetInterpolationToGouraud()

    sphereActor3 = vtkActor()
    sphereActor3.SetMapper(sphereMapper)
    sphereActor3.GetProperty().SetInterpolationToPhong()

    ren1 = vtkRenderer()
    ren1.AddActor(sphereActor1)
    ren1.SetViewport(0.0, 0.0, 0.33, 1.0)
    ren1.SetBackground(0.1, 0.2, 0.4)

    ren2 = vtkRenderer()
    ren2.AddActor(sphereActor2)
    ren2.SetViewport(0.33, 0.0, 0.66, 1.0)
    ren2.SetBackground(0.2, 0.3, 0.4)

    ren3 = vtkRenderer()
    ren3.AddActor(sphereActor3)
    ren3.SetViewport(0.66, 0.0, 1.0, 1.0)
    ren3.SetBackground(0.3, 0.4, 0.5)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.AddRenderer(ren3)
    renWin.SetSize(900, 300)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    iren.Initialize()

    timerId = iren.CreateRepeatingTimer(100)
    def rotatesphere(caller, event):
        sphereActor1.RotateY(10)
        sphereActor2.RotateY(10)
        sphereActor3.RotateY(10)
        renWin.Render()

    iren.AddObserver('TimerEvent', rotatesphere)
    iren.Start()

if __name__ == '__main__':
    main()