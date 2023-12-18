from vtkmodules.all import *

def main():
    # Sphere
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(10)
    sphereSource.SetPhiResolution(10)

    # Create a mapper for the sphere
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # Create an actor for the sphere
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

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
    renderer.SetBackground(0, 0, 0)

    # Render Window
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Begin interaction
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()