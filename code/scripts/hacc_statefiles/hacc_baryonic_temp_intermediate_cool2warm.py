# state file generated using paraview version 5.11.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

LoadPlugin('/Applications/ParaView-5.11.0.app/Contents/Plugins/GenericIOReader.so', remote=False, ns=globals())

def saveScreenshot(datapath, dataname, ratio, outputname):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [800, 800]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [32.000004291534424, 31.999998927116394, 32.00003266334534]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [2029.7001456568403, 2623.40265627863, 3412.097763266337]
    renderView1.CameraFocalPoint = [115.3779009833209, 117.51907053495684, 121.79226084836881]
    renderView1.CameraViewUp = [-0.39991532774447025, 0.8263616066622278, -0.3964772700542296]
    renderView1.CameraViewAngle = 0.257975859375
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 55.42558750639515
    renderView1.OSPRayMaterialLibrary = materialLibrary1

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

    # create a new 'vtkGenIOReader'
    m000fullmpicosmo624 = vtkGenIOReader(registrationName=dataname, FileNames=[datapath+dataname]) # m000.full.mpicosmo.624
    m000fullmpicosmo624.PointArrayStatus = ['mask', 'mu', 'phi', 'rho', 'uu']
    m000fullmpicosmo624.ShowData = ratio
    m000fullmpicosmo624.Scalar = ''
    m000fullmpicosmo624.Value = ''
    m000fullmpicosmo624.Value2range = ''

    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=m000fullmpicosmo624)
    threshold1.Scalars = ['POINTS', 'mask']
    threshold1.LowerThreshold = 6.0
    threshold1.UpperThreshold = 71.0

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
    calculator1.ResultArrayName = 'temp'
    calculator1.Function = 'mu*uu*uu'

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from calculator1
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'temp'
    tempTF2D = GetTransferFunction2D('temp')

    # get color transfer function/color map for 'temp'
    tempLUT = GetColorTransferFunction('temp')
    tempLUT.TransferFunction2D = tempTF2D
    tempLUT.RGBPoints = [0.20882642225908338, 0.23137254902, 0.298039215686, 0.752941176471, 575752.1873733271, 0.865, 0.865, 0.865, 1587397694597.7725, 0.705882352941, 0.0156862745098, 0.149019607843]
    tempLUT.UseLogScale = 1
    tempLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'temp'
    tempPWF = GetOpacityTransferFunction('temp')
    tempPWF.Points = [0.20882642225908335, 0.0, 0.5, 0.0, 1587397694597.7751, 1.0, 0.5, 0.0]
    tempPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Points'
    calculator1Display.ColorArrayName = ['POINTS', 'temp']
    calculator1Display.LookupTable = tempLUT
    calculator1Display.Opacity = 0.05
    calculator1Display.SelectTCoordArray = 'None'
    calculator1Display.SelectNormalArray = 'None'
    calculator1Display.SelectTangentArray = 'None'
    calculator1Display.OSPRayScaleArray = 'temp'
    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator1Display.SelectOrientationVectors = 'None'
    calculator1Display.ScaleFactor = 6.399997925758362
    calculator1Display.SelectScaleArray = 'temp'
    calculator1Display.GlyphType = 'Arrow'
    calculator1Display.GlyphTableIndexArray = 'temp'
    calculator1Display.GaussianRadius = 0.3199998962879181
    calculator1Display.SetScaleArray = ['POINTS', 'temp']
    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator1Display.OpacityArray = ['POINTS', 'temp']
    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator1Display.PolarAxes = 'PolarAxesRepresentation'
    calculator1Display.ScalarOpacityFunction = tempPWF
    calculator1Display.ScalarOpacityUnitDistance = 0.7217754920968269
    calculator1Display.OpacityArrayName = ['POINTS', 'temp']
    calculator1Display.SelectInputVectors = [None, '']
    calculator1Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator1Display.OSPRayScaleFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 51.47661520540714, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [2.5942752154014084, 0.0, 0.5, 0.0, 1399089424489.5227, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [2.5942752154014084, 0.0, 0.5, 0.0, 1399089424489.5227, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for tempLUT in view renderView1
    tempLUTColorBar = GetScalarBar(tempLUT, renderView1)
    tempLUTColorBar.Position = [0.855, 0.015]
    tempLUTColorBar.Title = 'temp'
    tempLUTColorBar.ComponentTitle = ''

    # set color bar visibility
    tempLUTColorBar.Visibility = 1

    # show color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(m000fullmpicosmo624)
    # ----------------------------------------------------------------

    # save screenshot
    SaveScreenshot(outputname, layout1, ImageResolution=[800, 800],
        # PNG options
        CompressionLevel='0')

if __name__ == "__main__":
    datapath = "/Users/jonwang/Downloads/output_sf_l64n256_ce_fire3_cloudy/"
    dataname = "m000.full.mpicosmo.624"
    ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]
    for r in ratio:
        outputname = "./hacc_temp_cool2warm_intermediate_{}.png".format(r)
        saveScreenshot(datapath, dataname, r, outputname)

