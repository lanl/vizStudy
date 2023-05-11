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
    renderView1.CenterOfRotation = [32.00000262260437, 31.999998092651367, 31.999998092651367]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [212.85897115531282, 221.3928507510473, 234.1255134926084]
    renderView1.CameraFocalPoint = [105.60261211933721, 98.14023645470384, 87.00628460923141]
    renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
    renderView1.CameraViewAngle = 5.1
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 55.42561992320987
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

    # get 2D transfer function for 'rho'
    rhoTF2D = GetTransferFunction2D('rho')

    # get color transfer function/color map for 'rho'
    rhoLUT = GetColorTransferFunction('rho')
    rhoLUT.TransferFunction2D = rhoTF2D
    rhoLUT.RGBPoints = [430638591.9999999, 0.247059, 0.0, 0.490196, 1619062439.395849, 0.288397, 0.07677, 0.525629, 6087153430.648497, 0.32975, 0.153587, 0.561092, 22885978344.412712, 0.373057, 0.236263, 0.600461, 86043909242.26614, 0.416363, 0.319, 0.639923, 323497392432.8141, 0.459669, 0.405613, 0.685198, 1216246028712.7922, 0.503345, 0.491534, 0.730058, 4572693434203.964, 0.562399, 0.54862, 0.757616, 17191958311635.56, 0.621453, 0.606075, 0.785544, 64636520719905.51, 0.680508, 0.674971, 0.824914, 243012504812458.03, 0.739562, 0.743406, 0.863899, 913648767561815.6, 0.798616, 0.800492, 0.893426, 3435025169225067.5, 0.85684, 0.856655, 0.922491, 1.2914724843237938e+16, 0.898178, 0.894056, 0.942176, 4.855520684225857e+16, 0.938654, 0.930919, 0.961646, 1.8255194284909146e+17, 0.964245, 0.958478, 0.977393, 6.318162149596202e+17, 0.988235, 0.984314, 0.992157]
    rhoLUT.UseLogScale = 1
    rhoLUT.ColorSpace = 'Lab'
    rhoLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'rho'
    rhoPWF = GetOpacityTransferFunction('rho')
    rhoPWF.Points = [430638592.0, 0.0, 0.5, 0.0, 6.318162149596201e+17, 1.0, 0.5, 0.0]
    rhoPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Points'
    calculator1Display.ColorArrayName = ['POINTS', 'rho']
    calculator1Display.LookupTable = rhoLUT
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
    calculator1Display.ScalarOpacityFunction = rhoPWF
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

    # get color legend/bar for rhoLUT in view renderView1
    rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
    rhoLUTColorBar.Title = 'rho'
    rhoLUTColorBar.ComponentTitle = ''

    # set color bar visibility
    rhoLUTColorBar.Visibility = 1

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
        outputname = "./hacc_rho_purple_intermediate_{}.png".format(r)
        saveScreenshot(datapath, dataname, r, outputname)
