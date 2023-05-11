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
    renderView1.CameraPosition = [155.63842454045738, 155.6384191760393, 155.6384529122683]
    renderView1.CameraFocalPoint = [32.000004291534424, 31.999998927116394, 32.00003266334534]
    renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
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
    tempLUT.RGBPoints = [2.5942752154014084, 0.0, 0.0, 0.34902, 6.034422530360354, 0.039216, 0.062745, 0.380392, 14.036388683336494, 0.062745, 0.117647, 0.411765, 32.6493887821825, 0.090196, 0.184314, 0.45098, 75.94421983452214, 0.12549, 0.262745, 0.501961, 176.65030622017917, 0.160784, 0.337255, 0.541176, 410.8980348429096, 0.2, 0.396078, 0.568627, 955.7707464561332, 0.239216, 0.454902, 0.6, 2223.173737325252, 0.286275, 0.521569, 0.65098, 5171.220697702715, 0.337255, 0.592157, 0.701961, 12028.535177157264, 0.388235, 0.654902, 0.74902, 27979.01442736439, 0.466667, 0.737255, 0.819608, 65080.67996619284, 0.572549, 0.819608, 0.878431, 151381.13302231123, 0.654902, 0.866667, 0.909804, 352120.59012018517, 0.752941, 0.917647, 0.941176, 819051.274826389, 0.823529, 0.956863, 0.968627, 1905156.953661135, 0.988235, 0.960784, 0.901961, 1905156.953661135, 0.941176, 0.984314, 0.988235, 3270147.5512959664, 0.988235, 0.945098, 0.85098, 5613114.964988388, 0.980392, 0.898039, 0.784314, 10307897.691653077, 0.968627, 0.835294, 0.698039, 23976719.856816143, 0.94902, 0.733333, 0.588235, 55771129.31163042, 0.929412, 0.65098, 0.509804, 129726621.62586734, 0.909804, 0.564706, 0.435294, 301751041.5546028, 0.878431, 0.458824, 0.352941, 701889018.1375973, 0.839216, 0.388235, 0.286275, 1632631295.1367698, 0.760784, 0.294118, 0.211765, 3797587477.479849, 0.701961, 0.211765, 0.168627, 8833391036.954012, 0.65098, 0.156863, 0.129412, 20546938727.40522, 0.6, 0.094118, 0.094118, 47793275459.1741, 0.54902, 0.066667, 0.098039, 111169708024.18675, 0.501961, 0.05098, 0.12549, 258586670686.3388, 0.45098, 0.054902, 0.172549, 601486389098.8815, 0.4, 0.054902, 0.192157, 1399089424489.521, 0.34902, 0.070588, 0.211765]
    tempLUT.UseLogScale = 1
    tempLUT.ColorSpace = 'Lab'
    tempLUT.NanColor = [0.25, 0.0, 0.0]
    tempLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'temp'
    tempPWF = GetOpacityTransferFunction('temp')
    tempPWF.Points = [2.5942752154014084, 0.0, 0.5, 0.0, 1399089424489.5227, 1.0, 0.5, 0.0]
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
    SetActiveSource(calculator1)
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
        outputname = "./hacc_temp_cool2warme_global_{}.png".format(r)
        saveScreenshot(datapath, dataname, r, outputname)
