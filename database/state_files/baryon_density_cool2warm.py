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
    resampleToImage2 = ResampleToImage(registrationName='ResampleToImage2', Input=nVB_C009_l10n512_S12345T692_z54h5)
    resampleToImage2.SamplingDimensions = [512, 512, 512]
    resampleToImage2.SamplingBounds = [0.0, 512.0, 0.0, 512.0, 0.0, 512.0]

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from resampleToImage2
    resampleToImage2Display = Show(resampleToImage2, renderView1, 'UniformGridRepresentation')

    # get color transfer function/color map for 'native_fieldsbaryon_density'
    native_fieldsbaryon_densityLUT = GetColorTransferFunction('native_fieldsbaryon_density')
    native_fieldsbaryon_densityLUT.AutomaticRescaleRangeMode = 'Never'
    native_fieldsbaryon_densityLUT.RGBPoints = [0.0, 0.23137254902, 0.298039215686, 0.752941176471, 231.89654541015625, 0.865, 0.865, 0.865, 500.0, 0.705882352941, 0.0156862745098, 0.149019607843]
    native_fieldsbaryon_densityLUT.ShowDataHistogram = 1
    native_fieldsbaryon_densityLUT.AutomaticDataHistogramComputation = 1
    native_fieldsbaryon_densityLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'native_fieldsbaryon_density'
    native_fieldsbaryon_densityPWF = GetOpacityTransferFunction('native_fieldsbaryon_density')
    native_fieldsbaryon_densityPWF.Points = [0.0, 0.0, 0.5, 0.0, 18.965517044067383, 0.8930481672286987, 0.5, 0.0, 500.0, 1.0, 0.5, 0.0]
    native_fieldsbaryon_densityPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    resampleToImage2Display.Representation = 'Volume'
    resampleToImage2Display.ColorArrayName = ['POINTS', 'native_fields/baryon_density']
    resampleToImage2Display.LookupTable = native_fieldsbaryon_densityLUT
    resampleToImage2Display.SelectTCoordArray = 'None'
    resampleToImage2Display.SelectNormalArray = 'None'
    resampleToImage2Display.SelectTangentArray = 'None'
    resampleToImage2Display.OSPRayScaleArray = 'native_fields/baryon_density'
    resampleToImage2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    resampleToImage2Display.SelectOrientationVectors = 'None'
    resampleToImage2Display.ScaleFactor = 51.199948799999994
    resampleToImage2Display.SelectScaleArray = 'None'
    resampleToImage2Display.GlyphType = 'Arrow'
    resampleToImage2Display.GlyphTableIndexArray = 'None'
    resampleToImage2Display.GaussianRadius = 2.5599974399999996
    resampleToImage2Display.SetScaleArray = ['POINTS', 'native_fields/baryon_density']
    resampleToImage2Display.ScaleTransferFunction = 'PiecewiseFunction'
    resampleToImage2Display.OpacityArray = ['POINTS', 'native_fields/baryon_density']
    resampleToImage2Display.OpacityTransferFunction = 'PiecewiseFunction'
    resampleToImage2Display.DataAxesGrid = 'GridAxesRepresentation'
    resampleToImage2Display.PolarAxes = 'PolarAxesRepresentation'
    resampleToImage2Display.ScalarOpacityUnitDistance = 1.7354386040415883
    resampleToImage2Display.ScalarOpacityFunction = native_fieldsbaryon_densityPWF
    resampleToImage2Display.OpacityArrayName = ['POINTS', 'native_fields/baryon_density']
    resampleToImage2Display.SliceFunction = 'Plane'
    resampleToImage2Display.Slice = 255

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    resampleToImage2Display.OSPRayScaleFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 51.47661520540714, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    resampleToImage2Display.ScaleTransferFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 28918.84765625, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    resampleToImage2Display.OpacityTransferFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 28918.84765625, 1.0, 0.5, 0.0]

    # init the 'Plane' selected for 'SliceFunction'
    resampleToImage2Display.SliceFunction.Origin = [256.0, 256.0, 256.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for native_fieldsbaryon_densityLUT in view renderView1
    native_fieldsbaryon_densityLUTColorBar = GetScalarBar(native_fieldsbaryon_densityLUT, renderView1)
    native_fieldsbaryon_densityLUTColorBar.Position = [0.8936755270394133, 0.014925373134328358]
    native_fieldsbaryon_densityLUTColorBar.Title = 'native_fields/baryon_density'
    native_fieldsbaryon_densityLUTColorBar.ComponentTitle = ''
    native_fieldsbaryon_densityLUTColorBar.TitleFontFamily = 'Courier'
    native_fieldsbaryon_densityLUTColorBar.LabelFontFamily = 'Courier'
    native_fieldsbaryon_densityLUTColorBar.TitleColor = (0, 0, 0)
    native_fieldsbaryon_densityLUTColorBar.LabelColor = (0, 0, 0)
    native_fieldsbaryon_densityLUTColorBar.AddRangeLabels = 0

    # set color bar visibility
    native_fieldsbaryon_densityLUTColorBar.Visibility = 1

    # show color legend
    resampleToImage2Display.SetScalarBarVisibility(renderView1, True)

    SaveScreenshot(outputName, renderView1, ImageResolution=[800, 800], CompressionLevel='0')

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(resampleToImage2)
    # ----------------------------------------------------------------

if __name__ == '__main__':
    print("filename:", sys.argv[1])
    print("registration name:", sys.argv[2])
    print("output filename:", sys.argv[3])

    saveScreenshot(sys.argv[1], sys.argv[2], sys.argv[3])

# if __name__ == '__main__':
#     # generate extracts
#     SaveExtracts(ExtractsOutputDirectory='extracts')