# state file generated using paraview version 5.11.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
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
renderView1.CenterOfRotation = [32.00000357627869, 31.999998092651367, 31.999998092651367]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [155.63849490948098, 155.6384894258536, 155.63848942585366]
renderView1.CameraFocalPoint = [32.00000357627869, 31.999998092651367, 31.999998092651367]
renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 55.4256193726058
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
m000fullmpicosmo624 = vtkGenIOReader(registrationName='m000.full.mpicosmo.624', FileNames=['/Users/jonwang/Downloads/output_sf_l64n256_ce_fire3_cloudy/m000.full.mpicosmo.624'])
m000fullmpicosmo624.PointArrayStatus = ['mask', 'mass', 'mu', 'phi', 'rho', 'uu']
m000fullmpicosmo624.ShowData = 0.8
m000fullmpicosmo624.Scalar = ''
m000fullmpicosmo624.Value = ''
m000fullmpicosmo624.Value2range = ''

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=m000fullmpicosmo624)
threshold1.Scalars = ['POINTS', 'mask']
threshold1.LowerThreshold = 1.0
threshold1.UpperThreshold = 6.0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
calculator1.ResultArrayName = 'phi_p'
calculator1.Function = '-phi+3e5'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'phi_p'
phi_pTF2D = GetTransferFunction2D('phi_p')
phi_pTF2D.ScalarRangeInitialized = 1
phi_pTF2D.Range = [1.0, 1272332.099609375, 1.0, 1272332.099609375]

# get color transfer function/color map for 'phi_p'
phi_pLUT = GetColorTransferFunction('phi_p')
phi_pLUT.TransferFunction2D = phi_pTF2D
phi_pLUT.RGBPoints = [1.0, 0.0, 0.0, 0.34902, 117041.46875, 0.039216, 0.062745, 0.380392, 234081.9375, 0.062745, 0.117647, 0.411765, 351122.40625, 0.090196, 0.184314, 0.45098, 468162.875, 0.12549, 0.262745, 0.501961, 585203.34375, 0.160784, 0.337255, 0.541176, 702243.8125, 0.2, 0.396078, 0.568627, 819284.28125, 0.239216, 0.454902, 0.6, 936324.75, 0.286275, 0.521569, 0.65098, 1053365.21875, 0.337255, 0.592157, 0.701961, 1170405.6875, 0.388235, 0.654902, 0.74902, 1287446.15625, 0.466667, 0.737255, 0.819608, 1404486.625, 0.572549, 0.819608, 0.878431, 1521527.09375, 0.654902, 0.866667, 0.909804, 1638567.5625, 0.752941, 0.917647, 0.941176, 1755608.03125, 0.823529, 0.956863, 0.968627, 1872648.5, 0.988235, 0.960784, 0.901961, 1872648.5, 0.941176, 0.984314, 0.988235, 1947554.4000000001, 0.988235, 0.945098, 0.85098, 2022460.3, 0.980392, 0.898039, 0.784314, 2106729.4375, 0.968627, 0.835294, 0.698039, 2223769.90625, 0.94902, 0.733333, 0.588235, 2340810.375, 0.929412, 0.65098, 0.509804, 2457850.84375, 0.909804, 0.564706, 0.435294, 2574891.3125, 0.878431, 0.458824, 0.352941, 2691931.78125, 0.839216, 0.388235, 0.286275, 2808972.25, 0.760784, 0.294118, 0.211765, 2926012.71875, 0.701961, 0.211765, 0.168627, 3043053.1875, 0.65098, 0.156863, 0.129412, 3160093.65625, 0.6, 0.094118, 0.094118, 3277134.125, 0.54902, 0.066667, 0.098039, 3394174.59375, 0.501961, 0.05098, 0.12549, 3511215.0625, 0.45098, 0.054902, 0.172549, 3628255.53125, 0.4, 0.054902, 0.192157, 3745296.0, 0.34902, 0.070588, 0.211765]
phi_pLUT.ColorSpace = 'Lab'
phi_pLUT.NanColor = [0.25, 0.0, 0.0]
phi_pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'phi_p'
phi_pPWF = GetOpacityTransferFunction('phi_p')
phi_pPWF.Points = [1.0, 0.0, 0.5, 0.0, 3745296.0, 1.0, 0.5, 0.0]
phi_pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Points'
calculator1Display.ColorArrayName = ['POINTS', 'phi_p']
calculator1Display.LookupTable = phi_pLUT
calculator1Display.Opacity = 0.05
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'temp'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 6.399999618530273
calculator1Display.SelectScaleArray = 'temp'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'temp'
calculator1Display.GaussianRadius = 0.31999998092651366
calculator1Display.SetScaleArray = ['POINTS', 'temp']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'temp']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = phi_pPWF
calculator1Display.ScalarOpacityUnitDistance = 0.4330126556500771
calculator1Display.OpacityArrayName = ['POINTS', 'temp']
calculator1Display.SelectInputVectors = [None, '']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.06377197802066803, 0.0, 0.5, 0.0, 51.47661520540714, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [68803838.85388254, 0.0, 0.5, 0.0, 5.2045838155130064e+20, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [68803838.85388254, 0.0, 0.5, 0.0, 5.2045838155130064e+20, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for phi_pLUT in view renderView1
phi_pLUTColorBar = GetScalarBar(phi_pLUT, renderView1)
phi_pLUTColorBar.Title = 'phi_p'
phi_pLUTColorBar.ComponentTitle = ''

# set color bar visibility
phi_pLUTColorBar.Visibility = 1

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


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')