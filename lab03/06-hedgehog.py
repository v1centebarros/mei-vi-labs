from vtkmodules.all import *


def main():
    # tetra
    coords = [[0, 0, 0], [1, 0, 0], [0, 1, 1], [1, 1, 0]]
    vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
    scalars = [0.1, 0.3, 0.5, 0.8]

    # VTKUnstructuredGrid Definition
    Ugrid = vtkUnstructuredGrid()
    points = vtkPoints()

    # Vertex
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])

    # Cell
    for i in range(len(coords)):
        Ugrid.InsertNextCell(VTK_VERTEX, 1, [i])

    Ugrid.SetPoints(points)

    # Vector
    vectorArray = vtkFloatArray()
    vectorArray.SetNumberOfComponents(3)
    for vector in vectors:
        vectorArray.InsertNextTuple(vector)

    Ugrid.GetPointData().SetVectors(vectorArray)

    # Scalar
    scalarArray = vtkFloatArray()
    scalarArray.SetNumberOfComponents(1)
    for scalar in scalars:
        scalarArray.InsertNextValue(scalar)

    Ugrid.GetPointData().SetScalars(scalarArray)

    # HedgeHog
    hedgeHog = vtkHedgeHog()
    hedgeHog.SetInputData(Ugrid)
    hedgeHog.SetScaleFactor(0.1)  # Adjust this value as needed

    # Mapper and actor
    UGriMapper = vtkDataSetMapper()
    UGriMapper.SetInputConnection(hedgeHog.GetOutputPort())

    UgridActor = vtkActor()
    UgridActor.SetMapper(UGriMapper)

    # Creation of renderer, render window, and interactor.
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    ren1.AddActor(UgridActor)
    ren1.SetBackground(1.0, 0.55, 0.41)

    # render
    renWin.Render()

    # Start of interaction
    iren.Start()


if __name__ == '__main__':
    main()
