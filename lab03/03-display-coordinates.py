from vtkmodules.all import *

class MyCallback:
    def __init__(self, picker, sphereActor, textMapper, textActor):
        self.picker = picker
        self.sphereActor = sphereActor
        self.textMapper = textMapper
        self.textActor = textActor

    def __call__(self, caller, eventId):
        pickedPoint = self.picker.GetPickPosition()
        print(f"Picked point coordinates: {pickedPoint}")
        self.sphereActor.SetPosition(pickedPoint)
        self.sphereActor.VisibilityOn()

        # Get the pixel coordinates
        pixelCoords = self.picker.GetSelectionPoint()

        # Update the TextMapper with the pixel coordinates
        self.textMapper.SetInput(str(pixelCoords))

        # Update the TextActor position
        self.textActor.SetPosition(pixelCoords[0], pixelCoords[1])

        # Make the actor visible
        self.textActor.VisibilityOn()

def main():
    # Sphere
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(10)
    sphereSource.SetPhiResolution(10)

    textMapper = vtkTextMapper()
    textActor = vtkActor2D()
    textActor.SetMapper(textMapper)
    textActor.VisibilityOff()
    # Create a mapper for the sphere
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # Create an actor for the sphere
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    # Create another sphere for picking glyphs
    pickSphereSource = vtkSphereSource()
    pickSphereSource.SetRadius(0.05)
    pickSphereSource.SetThetaResolution(10)
    pickSphereSource.SetPhiResolution(10)

    # Create a mapper for the second sphere
    pickSphereMapper = vtkPolyDataMapper()
    pickSphereMapper.SetInputConnection(pickSphereSource.GetOutputPort())

    # Create an actor for the second sphere
    pickSphereActor = vtkActor()
    pickSphereActor.SetMapper(pickSphereMapper)
    pickSphereActor.GetProperty().SetColor(1, 0, 0)

    # Glyph: Cone
    coneSource = vtkConeSource()
    coneSource.SetHeight(1)
    coneSource.SetRadius(0.35)
    coneSource.SetResolution(32)

    # Glyph 3D
    glyph3D = vtkGlyph3D()
    glyph3D.SetSourceConnection(coneSource.GetOutputPort())
    glyph3D.SetInputConnection(sphereSource.GetOutputPort())
    glyph3D.SetScaleFactor(0.25)
    glyph3D.SetVectorModeToUseNormal()

    # Mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph3D.GetOutputPort())

    # Actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Renderer
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.AddActor(sphereActor)
    renderer.AddActor(pickSphereActor)  # Add the second sphere actor to the renderer
    renderer.SetBackground(0, 0, 0)
    renderer.AddActor(textActor)

# Render Window
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Picker
    pointPicker = vtkPointPicker()
    callback = MyCallback(pointPicker, pickSphereActor, textMapper, textActor)
    pointPicker.AddObserver(vtkCommand.EndPickEvent, callback)
    renderWindowInteractor.SetPicker(pointPicker)

    # Begin interaction
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()