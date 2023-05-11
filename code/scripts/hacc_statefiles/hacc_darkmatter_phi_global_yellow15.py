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
    renderView1.CenterOfRotation = [32.00001120567322, 31.999998092651367, 31.999998092651367]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [155.63849271297178, 155.63847959994987, 155.63847959994993]
    renderView1.CameraFocalPoint = [32.00001120567322, 31.999998092651367, 31.999998092651367]
    renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 55.42561496777367
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
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 4.0

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
    calculator1.ResultArrayName = 'temp'
    calculator1.Function = 'mu*uu*uu'

    # create a new 'Calculator'
    calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
    calculator2.ResultArrayName = 'phi_p'
    calculator2.Function = 'phi+3445298'

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from calculator2
    calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'phi_p'
    phi_pTF2D = GetTransferFunction2D('phi_p')
    phi_pTF2D.ScalarRangeInitialized = 1
    phi_pTF2D.Range = [1156158.07421875, 3678848.4531250014, 1156158.07421875, 3678848.4531250014]

    # get color transfer function/color map for 'phi_p'
    phi_pLUT = GetColorTransferFunction('phi_p')
    phi_pLUT.TransferFunction2D = phi_pTF2D
    phi_pLUT.RGBPoints = [2.0, 1.0, 1.0, 0.988235, 7359.692906249867, 1.0, 1.0, 0.988235, 183944.32265625006, 0.984314, 0.988235, 0.843137, 367886.6453125001, 0.988235, 0.988235, 0.741176, 551828.9679687502, 0.980392, 0.968627, 0.654902, 735771.2906250003, 0.980392, 0.945098, 0.576471, 919713.6132812502, 0.968627, 0.905882, 0.486275, 1103655.9359375003, 0.968627, 0.862745, 0.388235, 1287598.2585937502, 0.960784, 0.803922, 0.286275, 1471540.58125, 0.94902, 0.741176, 0.219608, 1655482.9039062506, 0.941176, 0.678431, 0.14902, 1839425.2265625, 0.929412, 0.607843, 0.094118, 2023367.5492187508, 0.921569, 0.545098, 0.054902, 2207309.871875, 0.909804, 0.486275, 0.035294, 2391252.194531251, 0.890196, 0.411765, 0.019608, 2575194.5171875004, 0.8, 0.305882, 0.0, 2759136.839843751, 0.760784, 0.239216, 0.0, 2943079.1625000006, 0.678431, 0.180392, 0.011765, 3127021.4851562516, 0.6, 0.121569, 0.023529, 3310963.8078125007, 0.501961, 0.054902, 0.031373, 3494906.130468752, 0.4, 0.039216, 0.058824, 3678848.453125001, 0.301961, 0.047059, 0.090196]
    phi_pLUT.ColorSpace = 'Lab'
    phi_pLUT.NanColor = [0.25, 0.0, 0.0]
    phi_pLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'phi_p'
    phi_pPWF = GetOpacityTransferFunction('phi_p')
    phi_pPWF.Points = [2.0, 0.0, 0.5, 0.0, 3678848.4531250014, 1.0, 0.5, 0.0]
    phi_pPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    calculator2Display.Representation = 'Points'
    calculator2Display.ColorArrayName = ['POINTS', 'phi_p']
    calculator2Display.LookupTable = phi_pLUT
    calculator2Display.Opacity = 0.05
    calculator2Display.SelectTCoordArray = 'None'
    calculator2Display.SelectNormalArray = 'None'
    calculator2Display.SelectTangentArray = 'None'
    calculator2Display.OSPRayScaleArray = 'phi_p'
    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2Display.SelectOrientationVectors = 'None'
    calculator2Display.ScaleFactor = 6.399999618530273
    calculator2Display.SelectScaleArray = 'phi_p'
    calculator2Display.GlyphType = 'Arrow'
    calculator2Display.GlyphTableIndexArray = 'phi_p'
    calculator2Display.GaussianRadius = 0.31999998092651366
    calculator2Display.SetScaleArray = ['POINTS', 'phi_p']
    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2Display.OpacityArray = ['POINTS', 'phi_p']
    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2Display.PolarAxes = 'PolarAxesRepresentation'
    calculator2Display.ScalarOpacityFunction = phi_pPWF
    calculator2Display.ScalarOpacityUnitDistance = 0.4330126169357318
    calculator2Display.OpacityArrayName = ['POINTS', 'phi_p']
    calculator2Display.SelectInputVectors = [None, '']
    calculator2Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2Display.OSPRayScaleFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 51.47661520540714, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3678848.453125, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3678848.453125, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for phi_pLUT in view renderView1
    phi_pLUTColorBar = GetScalarBar(phi_pLUT, renderView1)
    phi_pLUTColorBar.Title = 'phi_p'
    phi_pLUTColorBar.ComponentTitle = ''

    # set color bar visibility
    phi_pLUTColorBar.Visibility = 1

    # show color legend
    calculator2Display.SetScalarBarVisibility(renderView1, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(calculator2)
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
        outputname = "./hacc_phi_yellow15_global_{}.png".format(r)
        saveScreenshot(datapath, dataname, r, outputname)
