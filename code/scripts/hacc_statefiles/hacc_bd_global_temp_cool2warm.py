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
renderView1.CenterOfRotation = [32.00000262260437, 31.999998092651367, 31.999998092651367]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [155.63849518404473, 155.6384906540917, 155.63849065409173]
renderView1.CameraFocalPoint = [32.00000262260437, 31.999998092651367, 31.999998092651367]
renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
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
m000fullmpicosmo624 = vtkGenIOReader(registrationName='m000.full.mpicosmo.624', FileNames=['/Users/jonwang/Downloads/output_sf_l64n256_ce_fire3_cloudy/m000.full.mpicosmo.624'])
m000fullmpicosmo624.PointArrayStatus = ['mask', 'mass', 'mu', 'phi', 'rho', 'uu']
m000fullmpicosmo624.ShowData = 0.8
m000fullmpicosmo624.Scalar = ''
m000fullmpicosmo624.Value = ''
m000fullmpicosmo624.Value2range = ''

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=m000fullmpicosmo624)
threshold1.Scalars = ['POINTS', 'mask']
threshold1.LowerThreshold = 4.0
threshold1.UpperThreshold = 72.0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
calculator1.ResultArrayName = 'temp'
calculator1.Function = 'mass*uu*uu'

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
tempLUT.RGBPoints = [68803838.8538825, 0.0, 0.0, 0.34902, 173809830.80029175, 0.039216, 0.062745, 0.380392, 439072263.78723204, 0.062745, 0.117647, 0.411765, 1109168865.4179456, 0.090196, 0.184314, 0.45098, 2801943264.192831, 0.12549, 0.262745, 0.501961, 7078170241.279976, 0.160784, 0.337255, 0.541176, 17880623995.780342, 0.2, 0.396078, 0.568627, 45169401636.29916, 0.239216, 0.454902, 0.6, 114105349156.87453, 0.286275, 0.521569, 0.65098, 288248908211.10754, 0.337255, 0.592157, 0.701961, 728164224541.8756, 0.388235, 0.654902, 0.74902, 1839462779558.3762, 0.466667, 0.737255, 0.819608, 4646785990494.703, 0.572549, 0.819608, 0.878431, 11738546863471.613, 0.654902, 0.866667, 0.909804, 29653503033663.637, 0.752941, 0.917647, 0.941176, 74909633397965.08, 0.823529, 0.956863, 0.968627, 189234073608344.44, 0.988235, 0.960784, 0.901961, 189234073608344.44, 0.941176, 0.984314, 0.988235, 342432364914916.94, 0.988235, 0.945098, 0.85098, 619655447379494.2, 0.980392, 0.898039, 0.784314, 1207598797813403.8, 0.968627, 0.835294, 0.698039, 3050593487498976.0, 0.94902, 0.733333, 0.588235, 7706301664776259.0, 0.929412, 0.65098, 0.509804, 1.946738744178637e+16, 0.909804, 0.564706, 0.435294, 4.91778274838178e+16, 0.878431, 0.458824, 0.352941, 1.2423129314398658e+17, 0.839216, 0.388235, 0.286275, 3.138287107397244e+17, 0.760784, 0.294118, 0.211765, 7.92783019415312e+17, 0.701961, 0.211765, 0.168627, 2.0027004998739835e+18, 0.65098, 0.156863, 0.129412, 5.059151361684767e+18, 0.6, 0.094118, 0.094118, 1.2780249718840705e+19, 0.54902, 0.066667, 0.098039, 3.228501604299432e+19, 0.501961, 0.05098, 0.12549, 8.155726874098521e+19, 0.45098, 0.054902, 0.172549, 2.060270955303644e+20, 0.4, 0.054902, 0.192157, 5.2045838155129946e+20, 0.34902, 0.070588, 0.211765]
tempLUT.UseLogScale = 1
tempLUT.ColorSpace = 'Lab'
tempLUT.NanColor = [0.25, 0.0, 0.0]
tempLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temp'
tempPWF = GetOpacityTransferFunction('temp')
tempPWF.Points = [68803838.85388254, 0.0, 0.5, 0.0, 5.2045838155130064e+20, 1.0, 0.5, 0.0]
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
calculator1Display.ScalarOpacityFunction = tempPWF
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

# get color legend/bar for tempLUT in view renderView1
tempLUTColorBar = GetScalarBar(tempLUT, renderView1)
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


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')