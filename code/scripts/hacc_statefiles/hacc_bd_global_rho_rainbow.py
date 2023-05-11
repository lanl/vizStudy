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
renderView1.CenterOfRotation = [32.000001668930054, 32.00000190734863, 31.999998092651367]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [155.63848563270327, 155.63848587112182, 155.63848205642458]
renderView1.CameraFocalPoint = [32.000001668930054, 32.00000190734863, 31.999998092651367]
renderView1.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 55.42561606898113
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
rhoLUT.RGBPoints = [430638591.9999999, 0.02, 0.3813, 0.9981, 710544852.4258107, 0.02000006, 0.424267768, 0.96906969, 1172384446.4659991, 0.02, 0.467233763, 0.940033043, 1934410312.9068828, 0.02, 0.5102, 0.911, 3191737377.5813103, 0.02000006, 0.546401494, 0.872669438, 5266301269.941608, 0.02, 0.582600362, 0.83433295, 8689289181.682354, 0.02, 0.6188, 0.796, 14337149094.347036, 0.02000006, 0.652535156, 0.749802434, 23656002217.863613, 0.02, 0.686267004, 0.703599538, 39031918915.61024, 0.02, 0.72, 0.6574, 64401866393.31315, 0.02000006, 0.757035456, 0.603735359, 106261759866.57388, 0.02, 0.794067037, 0.55006613, 175329726330.94086, 0.02, 0.8311, 0.4964, 289290455699.9764, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 477323323947.5558, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 787573703505.2235, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 1299480472320.4382, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 2144116151195.1738, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 3537747713597.328, 0.6439, 0.9773, 0.0469, 5837211234142.651, 0.762401813, 0.984669591, 0.034600153, 9631278923887.432, 0.880901185, 0.992033407, 0.022299877, 15891412866326.31, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 26220505592637.32, 0.999402998, 0.955036376, 0.079066628, 43263296933802.52, 0.9994, 0.910666223, 0.148134024, 71383553416603.11, 0.9994, 0.8663, 0.2172, 117781400390678.98, 0.999269665, 0.818035981, 0.217200652, 194336897142512.38, 0.999133332, 0.769766184, 0.2172, 320651898056123.25, 0.999, 0.7215, 0.2172, 529069061196318.1, 0.99913633, 0.673435546, 0.217200652, 872953109624694.8, 0.999266668, 0.625366186, 0.2172, 1440354742876670.8, 0.9994, 0.5773, 0.2172, 2376555810906341.0, 0.999402998, 0.521068455, 0.217200652, 3921268389113957.5, 0.9994, 0.464832771, 0.2172, 6470012489881505.0, 0.9994, 0.4086, 0.2172, 1.0675388028892656e+16, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 1.7614171494360318e+16, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 2.906302202721087e+16, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 4.795339080379682e+16, 0.949903037, 0.116867171, 0.252900603, 7.91221121956507e+16, 0.903199533, 0.078432949, 0.291800389, 1.3054986380244594e+17, 0.8565, 0.04, 0.3307, 2.1540460012863386e+17, 0.798902627, 0.04333345, 0.358434298, 3.554131762771559e+17, 0.741299424, 0.0466667, 0.386166944, 5.864244579548516e+17, 0.6837, 0.05, 0.4139]
rhoLUT.UseLogScale = 1
rhoLUT.ColorSpace = 'RGB'
rhoLUT.NanColor = [1.0, 0.0, 0.0]
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