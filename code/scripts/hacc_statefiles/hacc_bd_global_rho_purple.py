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

# get 2D transfer function for 'rho'
rhoTF2D = GetTransferFunction2D('rho')

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.TransferFunction2D = rhoTF2D
rhoLUT.RGBPoints = [430638591.9999999, 0.247059, 0.0, 0.490196, 1611506259.1148744, 0.288397, 0.07677, 0.525629, 6030468405.317485, 0.32975, 0.153587, 0.561092, 22567043357.86177, 0.373057, 0.236263, 0.600461, 84448844800.49342, 0.416363, 0.319, 0.639923, 316018685968.1523, 0.459669, 0.405613, 0.685198, 1182583493201.9644, 0.503345, 0.491534, 0.730058, 4425382993126.865, 0.562399, 0.54862, 0.757616, 16560464557425.934, 0.621453, 0.606075, 0.785544, 61971717029439.77, 0.680508, 0.674971, 0.824914, 231906317121337.06, 0.739562, 0.743406, 0.863899, 867823944513807.6, 0.798616, 0.800492, 0.893426, 3247511357258401.0, 0.85684, 0.856655, 0.922491, 1.215274248676546e+16, 0.898178, 0.894056, 0.942176, 4.547716100379998e+16, 0.938654, 0.930919, 0.961646, 1.701815187162749e+17, 0.964245, 0.958478, 0.977393, 5.864244579548516e+17, 0.988235, 0.984314, 0.992157]
rhoLUT.UseLogScale = 1
rhoLUT.ColorSpace = 'Lab'
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [430638592.0, 0.0, 0.5, 0.0, 5.864244579548529e+17, 1.0, 0.5, 0.0]
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
calculator1Display.ScalarOpacityFunction = rhoPWF
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


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')