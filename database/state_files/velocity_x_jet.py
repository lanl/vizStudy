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

    # get color transfer function/color map for 'native_fieldsvelocity_x'
    native_fieldsvelocity_xLUT = GetColorTransferFunction('native_fieldsvelocity_x')
    native_fieldsvelocity_xLUT.AutomaticRescaleRangeMode = 'Never'
    native_fieldsvelocity_xLUT.RGBPoints = [-10000000.0, 0.0, 0.0, 0.5625, -7777779.999999999, 0.0, 0.0, 1.0, -2698410.0, 0.0, 1.0, 1.0, -158730.00000000186, 0.5, 1.0, 0.5, 2380950.0, 1.0, 1.0, 0.0, 7460320.0, 1.0, 0.0, 0.0, 10000000.0, 0.5, 0.0, 0.0]
    native_fieldsvelocity_xLUT.ShowDataHistogram = 1
    native_fieldsvelocity_xLUT.AutomaticDataHistogramComputation = 1
    native_fieldsvelocity_xLUT.ColorSpace = 'RGB'
    native_fieldsvelocity_xLUT.NanColor = [1.0, 0.0, 0.0]
    native_fieldsvelocity_xLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'native_fieldsvelocity_x'
    native_fieldsvelocity_xPWF = GetOpacityTransferFunction('native_fieldsvelocity_x')
    native_fieldsvelocity_xPWF.Points = [-10000000.0, 0.0, 0.5, 0.0, 10000000.0, 1.0, 0.5, 0.0]
    native_fieldsvelocity_xPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    resampleToImage1Display.Representation = 'Volume'
    resampleToImage1Display.ColorArrayName = ['POINTS', 'native_fields/velocity_x']
    resampleToImage1Display.LookupTable = native_fieldsvelocity_xLUT
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
    resampleToImage1Display.ScalarOpacityUnitDistance = 1.7354386040415883
    resampleToImage1Display.ScalarOpacityFunction = native_fieldsvelocity_xPWF
    resampleToImage1Display.OpacityArrayName = ['POINTS', 'native_fields/baryon_density']
    resampleToImage1Display.SliceFunction = 'Plane'
    resampleToImage1Display.Slice = 255

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    resampleToImage1Display.ScaleTransferFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 28918.84765625, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    resampleToImage1Display.OpacityTransferFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 28918.84765625, 1.0, 0.5, 0.0]

    # init the 'Plane' selected for 'SliceFunction'
    resampleToImage1Display.SliceFunction.Origin = [256.0, 256.0, 256.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for native_fieldsvelocity_xLUT in view renderView1
    native_fieldsvelocity_xLUTColorBar = GetScalarBar(native_fieldsvelocity_xLUT, renderView1)
    native_fieldsvelocity_xLUTColorBar.Position = [0.84875, 0.015]
    native_fieldsvelocity_xLUTColorBar.Title = 'native_fields/velocity_x'
    native_fieldsvelocity_xLUTColorBar.ComponentTitle = ''
    native_fieldsvelocity_xLUTColorBar.TitleFontFamily = 'Courier'
    native_fieldsvelocity_xLUTColorBar.LabelFontFamily = 'Courier'
    native_fieldsvelocity_xLUTColorBar.TitleColor = (0, 0, 0)
    native_fieldsvelocity_xLUTColorBar.LabelColor = (0, 0, 0)
    native_fieldsvelocity_xLUTColorBar.AddRangeLabels = 0

    # set color bar visibility
    native_fieldsvelocity_xLUTColorBar.Visibility = 1

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