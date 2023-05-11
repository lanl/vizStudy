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
phi_pLUT.RGBPoints = [1.0, 0.403922, 0.0, 0.05098, 234999.53477499998, 0.525967, 0.029527, 0.066728, 469998.06954999996, 0.647643, 0.058962, 0.082476, 704998.4769725, 0.722445, 0.076678, 0.098224, 939997.0117474999, 0.797186, 0.095194, 0.114187, 1174995.5465225, 0.868051, 0.164091, 0.143714, 1409994.0812975, 0.937809, 0.233541, 0.173933, 1644992.6160725, 0.96143, 0.326059, 0.232987, 1879992.2182565748, 0.984375, 0.418147, 0.292657, 2114991.5582700004, 0.986344, 0.496886, 0.371396, 2349990.093045, 0.988235, 0.575702, 0.450673, 2584988.62782, 0.988235, 0.656409, 0.543191, 2819987.162595, 0.98842, 0.736747, 0.635894, 3054987.5700175, 0.992357, 0.809581, 0.732349, 3289986.1047925, 0.996186, 0.880692, 0.826759, 3524984.6395675004, 0.998155, 0.92203, 0.885813, 3745296.0, 1.0, 0.960784, 0.941176]
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