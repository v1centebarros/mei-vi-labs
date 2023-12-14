import os

from vtkmodules.all import (
    vtkPlaneSource, vtkPolyDataMapper, vtkActor,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor,
    vtkJPEGReader, vtkTexture
)


def main():
    planeSource = vtkPlaneSource()

    # Set the origin and points to define the plane
    # UNCOMMENT THE FOLLOWING LINES TO SEE THE DIFFERENCE
    planeSource.SetOrigin(0, 0, 0)
    planeSource.SetPoint1(2, 0, 3)
    planeSource.SetPoint2(0, 3, 2)

    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)

    JPGReader = vtkJPEGReader()
    JPGReader.SetFileName(os.path.join(os.path.abspath(os.getcwd()), "images/lena.jpg"))
    aText = vtkTexture()
    aText.SetInputConnection(JPGReader.GetOutputPort())

    planeActor.SetTexture(aText)

    ren = vtkRenderer()
    ren.AddActor(planeActor)
    ren.SetBackground(0.1, 0.2, 0.4)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(640, 480)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()
