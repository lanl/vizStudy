# state file generated using paraview version 5.10.1
import sys

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

def saveScreenshot(inputFilename, regName, outputName):   
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [800, 800]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [256.0, -1457.1836768696405, 256.0]
    renderView1.CameraFocalPoint = [256.0, 256.0, 256.0]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraViewAngle = 21.916666666666668
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 443.4045633326258
    renderView1.BackEnd = ''

    renderView1.Background = (1., 1., 1.)
    renderView1.UseColorPaletteForBackground = 0

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(800, 800)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'VisItPixieReader'
    nVB_C009_l10n512_S12345T692_z54h5 = VisItPixieReader(registrationName=regName, FileName=inputFilename)
    nVB_C009_l10n512_S12345T692_z54h5.Meshes = ['mesh_512x512x512']
    nVB_C009_l10n512_S12345T692_z54h5.CellArrays = ['native_fields/baryon_density', 'native_fields/dark_matter_density', 'native_fields/temperature', 'native_fields/velocity_x']

    # create a new 'Resample To Image'
    resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=nVB_C009_l10n512_S12345T692_z54h5)
    resampleToImage1.SamplingDimensions = [512, 512, 512]
    resampleToImage1.SamplingBounds = [0.0, 512.0, 0.0, 512.0, 0.0, 512.0]

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from resampleToImage1
    resampleToImage1Display = Show(resampleToImage1, renderView1, 'UniformGridRepresentation')

    # get color transfer function/color map for 'native_fieldstemperature'
    native_fieldstemperatureLUT = GetColorTransferFunction('native_fieldstemperature')
    native_fieldstemperatureLUT.AutomaticRescaleRangeMode = 'Never'
    native_fieldstemperatureLUT.RGBPoints = [0.0, 0.23137254902, 0.298039215686, 0.752941176471, 51562.5, 0.865, 0.865, 0.865, 100000.0, 0.705882352941, 0.0156862745098, 0.149019607843]
    native_fieldstemperatureLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'native_fieldstemperature'
    native_fieldstemperaturePWF = GetOpacityTransferFunction('native_fieldstemperature')
    native_fieldstemperaturePWF.Points = [0.0, 0.0, 0.5, 0.0, 9375.0, 0.5153846144676208, 0.5, 0.0, 100000.0, 1.0, 0.5, 0.0]
    native_fieldstemperaturePWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    resampleToImage1Display.Representation = 'Volume'
    resampleToImage1Display.ColorArrayName = ['POINTS', 'native_fields/temperature']
    resampleToImage1Display.LookupTable = native_fieldstemperatureLUT
    resampleToImage1Display.SelectTCoordArray = 'None'
    resampleToImage1Display.SelectNormalArray = 'None'
    resampleToImage1Display.SelectTangentArray = 'None'
    resampleToImage1Display.OSPRayScaleArray = 'native_fields/baryon_density'
    resampleToImage1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    resampleToImage1Display.SelectOrientationVectors = 'None'
    resampleToImage1Display.ScaleFactor = 51.199948799999994
    resampleToImage1Display.SelectScaleArray = 'None'
    resampleToImage1Display.GlyphType = 'Arrow'
    resampleToImage1Display.GlyphTableIndexArray = 'None'
    resampleToImage1Display.GaussianRadius = 2.5599974399999996
    resampleToImage1Display.SetScaleArray = ['POINTS', 'native_fields/baryon_density']
    resampleToImage1Display.ScaleTransferFunction = 'PiecewiseFunction'
    resampleToImage1Display.OpacityArray = ['POINTS', 'native_fields/baryon_density']
    resampleToImage1Display.OpacityTransferFunction = 'PiecewiseFunction'
    resampleToImage1Display.DataAxesGrid = 'GridAxesRepresentation'
    resampleToImage1Display.PolarAxes = 'PolarAxesRepresentation'
    resampleToImage1Display.ScalarOpacityUnitDistance = 8.957667946113652
    resampleToImage1Display.ScalarOpacityFunction = native_fieldstemperaturePWF
    resampleToImage1Display.OpacityArrayName = ['POINTS', 'native_fields/baryon_density']
    resampleToImage1Display.SliceFunction = 'Plane'
    resampleToImage1Display.Slice = 49

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    resampleToImage1Display.OSPRayScaleFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 51.47661520540714, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    resampleToImage1Display.ScaleTransferFunction.Points = [0.06706630438566208, 0.0, 0.5, 0.0, 1740.4564208984375, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    resampleToImage1Display.OpacityTransferFunction.Points = [0.06706630438566208, 0.0, 0.5, 0.0, 1740.4564208984375, 1.0, 0.5, 0.0]

    # init the 'Plane' selected for 'SliceFunction'
    resampleToImage1Display.SliceFunction.Origin = [256.0, 256.0, 256.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for native_fieldstemperatureLUT in view renderView1
    native_fieldstemperatureLUTColorBar = GetScalarBar(native_fieldstemperatureLUT, renderView1)
    native_fieldstemperatureLUTColorBar.Title = 'native_fields/temperature'
    native_fieldstemperatureLUTColorBar.ComponentTitle = ''
    native_fieldstemperatureLUTColorBar.TitleFontFamily = 'Courier'
    native_fieldstemperatureLUTColorBar.LabelFontFamily = 'Courier'
    native_fieldstemperatureLUTColorBar.TitleColor = (0, 0, 0)
    native_fieldstemperatureLUTColorBar.LabelColor = (0, 0, 0)
    native_fieldstemperatureLUTColorBar.AddRangeLabels = 0

    # set color bar visibility
    native_fieldstemperatureLUTColorBar.Visibility = 1

    # show color legend
    resampleToImage1Display.SetScalarBarVisibility(renderView1, True)

    SaveScreenshot(outputName, renderView1, ImageResolution=[800, 800], CompressionLevel='0')

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(resampleToImage1)
    # ----------------------------------------------------------------



if __name__ == '__main__':
    print("filename:", sys.argv[1])
    print("registration name:", sys.argv[2])
    print("output filename:", sys.argv[3])

    saveScreenshot(sys.argv[1], sys.argv[2], sys.argv[3])

# if __name__ == '__main__':
#     # generate extracts
#     SaveExtracts(ExtractsOutputDirectory='extracts')