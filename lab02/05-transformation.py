import os

from vtkmodules.all import (vtkPlaneSource, vtkTransform, vtkTransformPolyDataFilter, vtkJPEGReader, vtkTexture,
                            vtkPolyDataMapper, vtkActor, vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor

)


def create_textured_plane(rotation, translation, image_name):
    planeSource = vtkPlaneSource()

    transform = vtkTransform()
    transform.Translate(*translation)
    transform.RotateWXYZ(*rotation)

    filter = vtkTransformPolyDataFilter()
    filter.SetTransform(transform)
    filter.SetInputConnection(planeSource.GetOutputPort())

    JPGReader = vtkJPEGReader()
    JPGReader.SetFileName(os.path.join(os.path.abspath(os.getcwd()), f"images/{image_name}.jpg"))

    texture = vtkTexture()
    texture.SetInputConnection(JPGReader.GetOutputPort())

    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(filter.GetOutputPort())

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.SetTexture(texture)

    return planeActor


def main():
    rotations = [
        (0, 0, 0, 0),
        (180, 0, 1, 0),
        (90, 0, 1, 0),
        (-90, 0, 1, 0),
        (90, 1, 0, 0),
        (-90, 1, 0, 0)
    ]

    translations = [
        (0, 0, 0),
        (0, 0, 1),
        (-0.5, 0, 0.5),
        (0.5, 0, 0.5),
        (0, 0.5, 0.5),
        (0, -0.5, 0.5)
    ]
    image_names = ["Im1", "Im2", "Im3", "Im4", "Im5", "Im6"]

    # Create the renderer
    renderer = vtkRenderer()

    # Create the six planes
    for rotation, translation, image_name in zip(rotations, translations, image_names):
        actor = create_textured_plane(rotation, translation, image_name)
        renderer.AddActor(actor)

    # Create the render window and add the renderer
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Create the render window interactor and initialize it
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    interactor.Initialize()
    interactor.Start()


if __name__ == '__main__':
    main()
